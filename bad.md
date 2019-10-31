Das ist eine Kombi aus selbst vorinstalliertem Raspbian Buster lite und einem vorbereiteten Skript welches notwendige Schritte ausführt

## Obacht
Wie immer bei fremden Skripten, vorher angucken was die machen und/oder jeden einzelnen Schritt von Hand ausführen

1. Dieses [Archiv](https://github.com/White-SAndS/Mikrosko-Pi/releases/download/v0.994r/UnzipToBootPartition.zip) in die Bootpartition der mit Raspbian Buster lite erstellten uSD entpacken
2. Den Raspberry von der uSD booten und entsprechend der eigenen Bedürfnisse anpassen also:
 
   Keyboard
   
   WLan
   
   Autologin
   
   ...

3. das [install.script](https://github.com/White-SAndS/Mikrosko-Pi/blob/master/ZIP%20Archive/install.script) mit

        sudo /boot/install.script

   aufrufen. Dabei wird der Pi upgedatet und erforderliche Pakete installiert. Ausserdem wird das tarpi9xx.py ins Home Verzeichnis entpackt      und Anpassungen vorgenommen. 
   Am Schluss wird der Pi neu gebootet.
   Jetzt sollte schon Tarpi starten. 
