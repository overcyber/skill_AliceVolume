
import re
from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class AliceVolume(AliceSkill):
	"""
	Author: lazza
	Description: A simple skill to Control the volume of Alice
	"""

	_SPOKEN_LEVEL = int

	@IntentHandler('adjustVolume')
	@IntentHandler('setSoundLevel')
	def listenForVolumeRequest(self, session: DialogSession, **_kwargs):

		level = ""
		AliceVolume._SPOKEN_LEVEL = int(float(f'{session.slotValue("volume")}'))
		card = self.getConfig('audioOut')

		# if no card selected defaultt to card0
		if not card:
			card = '-c0'

		if 'setSoundLevel' in session.intentName:
			level = f'{session.slotValue("volume")}%'

		elif 'adjustVolume' in session.intentName:

			if 'lowerVolume' in session.slots:
				level = f'{session.slotValue("volume")}%-'
			elif 'raiseVolume' in session.slots:
				level = f'{session.slotValue("volume")}%+'


		self.adjustVolumePi(level=level,card=card, sessionId=session.sessionId)



	def adjustVolumePi(self, level: str, card: str, sessionId):

		# return the system message so we can extract portName
		portResult = self.Commons.runSystemCommand(f'amixer')
		# extract the portName
		portName = re.findall(r"'(.*?)'", portResult.stdout.decode('utf-8'))
		# run the volume changing system command
		result = self.Commons.runSystemCommand(f'amixer {card} -M -q set {portName[0]} {level}'.split())

		# if no error code
		if not result.returncode:

			self.endDialog(
				sessionId=sessionId,
				text=self.randomTalk(text="dialogMessage2", replace=[AliceVolume._SPOKEN_LEVEL])
			)


		else:
			self.endDialog(
				sessionId=sessionId,
				text=self.randomTalk(text="dialogMessage1")
			)

			return self.logError(f'Error with {self.name} configuration. Have you selected the right card ?: {result.stderr}')

