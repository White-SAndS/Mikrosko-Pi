# Mikrosko-Pi
RaspberryPi als elektronisches Betrachtungs- und Bestückungsmikroskop mit kleinen Gimmicks 

Die grosse Zahl an USB-Mikroskopen mit sehr simplen Keyhole-Optiken macht es vor. Auch wenn ich die Vergrösserungen immer nicht so recht glauben kann, sie funktionieren und das recht akzeptabel. Mir aber leider nicht gut genug.

# Warum:

Ich brauchte ein "Arbeitsplatzmikroskop" mit flexibler Vergrösserung und relativ grossem Arbeitsabstand. Die Preise für echte Mikroskope sind auch echt gesalzen, vor allem bei grossem Arbeitsabstand, und wirklich handlich sind sie nicht. Da ich mal irgendwann in meiner Vergangenheit über Makroobjektive für Kameras gestolpert bin ( https://de.wikipedia.org/wiki/Makro-Objektiv ) und ich schon ein bisschen Erfahrung mit dem RaspberryPi und dessen Kamera sammeln durfte, vor allem dessen Echtzeitfähigkeit, was lag da näher als genau dieses System zu benutzen.
Nebenbei hat sich noch ein anderer Zweck ergeben, die Digiskopie ( https://de.wikipedia.org/wiki/Digiskopie ). Beide gemeinsam haben den Hardware- und Softwareunterbau. Interessanterweise benötigen sie die selben Features. 

# Features:

-nahezu Echtzeitanzeige mit sehr geringer Latenz, etwa 130ms, so das selbst das Bestücken von Leiterplatten funktioniert

-Bildausschnitt flexibel anpassbar (Softwarezoom) und natürlich vorwählbar über die Objektivauswahl

-verschiebbarer Bildausschnitt/Shift des gezoomten Bereiches innerhalb des Gesamtabbildes

-Belichtungskorrektur, Helligkeit, Kontrast, Schärfe sind über Tastatur einstellbar und werden gesichert

-Aufnahme des angezeigten Bildausschnittes zu Dokumentationszwecken

-das Programm passt sich an das angeschlossene Display (HDMI) an und wählt immer die maximal darstellbare native Auflösung

-rudimentäres sehr einfaches OSD für die Bedienung

# Was wird benötigt:

-RaspberryPi, nahezu egal was für einer. Ein PiZero geht hervorragend. (PiZero 15-20€)

-uSD Karte ab 4GB (~5-10€)

-Netzteil für den RaspberryPi oder andere Stromversorgung (10€)

-Tastatur für den RaspberryPi ( Zehnertastatur mit Kabel ab 10€, Kabellos ab 15€)

-Bildschirm für den RaspberryPi (vorhandener Bildschirm 0€, kleiner HD Bildschirm mit HDMI so ab 100€)

-natürlich eine Kamera passend zum RaspberryPi (etwa ab 25€, wenn etwas bessere Auflösung gefragt ist dann Arducam https://www.arducam.com/product/arducam-raspberry-pi-camera-v2-8mp-ixm219-b0103/ allerdingens dann auch teurer für etwa 80€)

    Optimal ist eine Kamera mit hoher Auflösung UND der Möglichkeit das Objektiv zu wechseln.
    Ich verwende Objektive im Bereich zwischen 8mm und 25mm Brennweite. Diese Objektive sollten, im Sinne von müssen, ein UV/IR-Sperrfilter 
    besitzen oder der Objektivhalter bzw. die Kamera sollte, im Sinne von müssen, ein Sperrfilter eingebaut haben.
    
-Objektiv passend zur Kamera (Gewinde) und den Einsatzzweck (Brennweite) und evtl. ein IR/UV-Sperrfilter (ab 8€ aufwärts)

-ein PC mit dem man die uSD Karte beschreiben kann (unbezahlbar und hoffentlich vorhanden)

-ein wenig Geduld und Einfühlungsvermögen (eh unbezahlbar aber meist nicht in ausreichendem Masse vorhanden)

Gesamtkosten: ab 75€ und nach oben offen

# Installation

Es gibt 3 Wege:

1. selber zusammen tippern

2. vorbereitetes Archiv auf eine selbst vorbereitete uSD mit Raspbian Buster lite kopieren und ein bisschen tippern

3. vorbereitete angepasste Raspbian Buster lite Images auf eine uSD Karte kopieren, in den Raspi stecken, Kamera anschliessen, Netzteil, Display, Tastatur anschliessen und booten, nochmal booten lassen nach der Filesystemexpansion und fertig

    https://github.com/White-SAndS/Mikrosko-Pi/releases/download/v0.994r/MikroskopiSetupRevisedSplash.img.gz
    
    https://github.com/White-SAndS/Mikrosko-Pi/releases/download/v0.994r/TarpiSetupRevisedSplash.img.gz

