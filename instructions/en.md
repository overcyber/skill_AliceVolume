<span style="color: #ff0000;"><strong>Use this skill to adjust the volume of Alice on the fly</strong></span>

just say something like 

- Hey Alice/Snips
- 40 percent, or set volume to 60 percent or adjust volume to 10 percent etc

Alternatively increase or decrease the volume with 

- Hey Alice/Snips
- raise the volume 5 percent, or decrease volume by 20 percent

#SETUP

In the pi's terminal type 

- ```amixer```

You should see a line similar to this :

- ```Simple mixer control 'Headphone',0```

What your looking for is the 'Headphone' or maybe you have "Headphones" or 'Master' etc 

Enter what ever it is that you have when doing that command, into the "portName" field 
of the skill settings

then do
 - ```aplay -l```
 
   and see what your card number is. Then select that from the drop list in the skill settings

EG: respeaker 2 could be card 1
   
 Currently HDMI or USB are not configured so i know they don't work 

Please discuss in discord for additions you find that need added
