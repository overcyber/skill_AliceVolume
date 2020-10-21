
from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler
import subprocess

class AliceVolume(AliceSkill):
	"""
	Author: lazza
	Description: A simple skill to Control the volume of Alice
	"""

	@IntentHandler('adjustVolume')
	@IntentHandler('setSoundLevel')
	def listenForVolumeRequest(self, session: DialogSession, **_kwargs):
		level = ""

		if 'setSoundLevel' in session.intentName:
			level = f'{session.slotValue("volume")}%'

		elif 'adjustVolume' in session.intentName:

			if 'lowerVolume' in session.slots:
				level = f'{session.slotValue("volume")}%-'
			elif 'raiseVolume' in session.slots:
				level = f'{session.slotValue("volume")}%+'

		portName = self.getConfig("portName")

		self.adjustVolumePi(level=level, portName=portName)
		self.endDialog(
			sessionId=session.sessionId,
			text=self.randomTalk(text="dialogMessage1", replace=[level])
		)

	@staticmethod
	def adjustVolumePi(level: str, portName: str):
		subprocess.run(['amixer', '-M', '-q', 'set', portName, level])


