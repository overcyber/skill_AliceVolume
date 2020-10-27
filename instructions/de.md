
<Span style = "color: #ff0000;"> <strong> Passe die Lautstärke von Alice an! </strong> </span>

Sag nur etwas, wie:

- Hey Alice / Snips
- Lautstärke auf 40 Prozent

erhöhen oder verringern Alternativ die Lautstärke mit

- Hey Alice / Snips
- Erhöhe die Lautstärke um 5 Prozent, oder Verringere die Lautstärke um 20 Prozent

#KONFIGURATION

Wähle dich per SSH im terminal ein und gib ein:

- `` `amixer```

Jetzt solltest du eine Einstellung finden wie:

- ```Simple mixer control 'Headphone',0```

Aus dieser Zeile benötigen wir 'Headphone' oder was auch immer bei dir steht!

Gib diesen Wert in den Skill-Einstellungen unter "portname" ein.

Zurück im Terminal:

 - `` `aplay -l```
 
Schau nach was deine Kartennummer ist. Wähle sie im Dropdown-Menü der Skilleinstellungen aus!

Beispiel: respeaker2 ist wahrscheinlich Karte 1
   
Für weitere Features, Änderungen oder Fehler, sprich uns in Discord an!
