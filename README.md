# Eine Vorlage für ein Projekt in Flask

## Installation

In der Folge wird eine Möglichkeit beschrieben, das Projekt auf einem eigenen Computer zum Laufen zu bringen. Auf einem Schulrechner kannst du das Projekt nur bearbeiten, wenn auf diesen Python bereits installiert ist. Allerdings gibt es auch die Möglichkeit, das Projekt online zu bearbeiten und auszuführen. (Wird noch ergänzt.)

Installiere python [https://www.python.org/downloads/](https://www.python.org/downloads/). Öffne dann eine Kommandozeilenanwendung (z.B. PowerShell oder einem Terminal in VSCode), wechsle in das Projektverzeichnis und führe den Befehl
```
$ pip install -r requirements.txt
```

aus, um Flask zu installieren. 


## Start und Test

Um Flask zu starten und den lokalen Webserver zu starten, führe den folgenden Befehl aus:

```
flask --debug run
```

Öffne dann in einem Browser die Adresse [127.0.0.1:5000/](127.0.0.1:5000/).


