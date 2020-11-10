import re
from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class AliceVolume(AliceSkill):
	"""
	Author: lazza
	Description: A simple skill to Control the volume of Alice
	"""

	_ADJUSTED_VOLUME = 0


	@IntentHandler('adjustVolume')
	@IntentHandler('setSoundLevel')
	def listenForVolumeRequest(self, session: DialogSession, **_kwargs):

		level = ""

		card = self.getConfig('audioOut')

		# if no card selected default to card0
		if not card:
			card = '-c0'

		if 'setSoundLevel' in session.intentName:
			level = f'{session.slotValue("volume")}%'

		elif 'adjustVolume' in session.intentName:

			if 'lowerVolume' in session.slots:
				level = f'{session.slotValue("volume")}%-'
				AliceVolume._ADJUSTED_VOLUME = 1
			elif 'raiseVolume' in session.slots:
				level = f'{session.slotValue("volume")}%+'
				AliceVolume._ADJUSTED_VOLUME = 2

		self.adjustVolumePi(level=level, card=card, sessionId=session.sessionId)


	def adjustVolumePi(self, level: str, card: str, sessionId):

		# return the system message so we can extract portName
		portResult = self.Commons.runSystemCommand(f'amixer')
		# extract the portName
		if self.getConfig('forceAudioPort'):
			portName = [self.getConfig('forceAudioPort')]
		else:
			portName = re.findall(r"'(.*?)'", portResult.stdout.decode('utf-8'))

		# run the volume changing system command
		result = self.Commons.runSystemCommand(f'amixer {card} -M -q set {portName[0]} {level}'.split())

		# if no error code
		if not result.returncode:
			# get the true volume level for the dialog output
			amixerResult = self.Commons.runSystemCommand(f'amixer {card} -M get {portName[0]}'.split())
			spokenLevel = re.findall(r"\[(.*?)]", amixerResult.stdout.decode('utf-8'))

			action = ['set', 'lowered', 'raised']

			self.endDialog(
				sessionId=sessionId,
				text=self.randomTalk(text="dialogMessage2", replace=[action[AliceVolume._ADJUSTED_VOLUME], spokenLevel[0]])
			)

			AliceVolume._ADJUSTED_VOLUME = 0


		else:
			self.endDialog(
				sessionId=sessionId,
				text=self.randomTalk(text="dialogMessage1")
			)
			AliceVolume._ADJUSTED_VOLUME = 0
			return self.logError(f'Error with {self.name} configuration. Have you selected the right card ?: {result.stderr}')
