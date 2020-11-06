<span style="color: #ff0000;"><strong>Use this skill to adjust the volume of Alice on the fly</strong></span>

just say something like 

- Hey Alice/Snips
- 40 percent, or set volume to 60 percent or adjust volume to 10 percent etc

Alternatively increase or decrease the volume with 

- Hey Alice/Snips
- raise the volume 5 percent, or decrease volume by 20 percent etc

#SETUP

In the pi's terminal type 

 - ```aplay -l```
 
   and see what your card number is. Then select that from the drop list in the skill settings

EG: respeaker 2 is likely card 1 
   
 NOTE: if you choose nothing it will default to card0

### forceAudioPort field

In normal operation your audio output field will get auto detected. However if you require 
a different port than what it detects you can enter the port name into this field.

- leave this blank to auto detect the port
- Add port name EG: Headphones to Specifically use the Headphones port


Please discuss in discord any additions you find that need added.

- 
