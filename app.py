from flask import Flask, render_template, request 
import requests # Um APi-Aufrufe tätigen zu können 
import json # Zum Verarbeiten von JSON-Objekten

app = Flask(__name__)


"""
Basisroute: Im Browser erreichbar, wenn einfach die Adresse der Webseite eingegeben wird
Im lokalen Test: 127.0.0.1:5000/
Im Internet könnte das z.B. www.mein-tolle-webseite.de/ sein.
Beachte: Der Pfad der Basisroute '/' wird vom Browser automatisch ergänzt.
Die 5000 im lokalen Fall ist der "Port", an dem der Webserver "lauscht".
Dieser muss nur angegeben werden, wenn nicht der Standard-Port verwendet wird. (80 für http bzw. 443 für https) 

Es kann ein sogenannter "Request-Parameter" angegeben werden, z.B.:
127.0.0.1:5000/?name=Anna
Probier aus, wie sich die Webseite dann ändert.
"""
@app.route("/", methods=['GET'])
def start():
    params = request.args
    if ('name' in params.keys()):
        name = params['name']
    else:
        name = 'Fremder'

    # Rendere das Template index.html mit den gegebenen Werten für title und name und gib das Ergebnis zurück.   
    return render_template("index.html", title="Starterprojekt für Flask", name=name)


"""
Unter dieser Route werden Wetter informationen angezeigt.
Beispiel im lokalen Fall: 127.0.0.1:5000/weather/Bamberg

city ist eine Fall eine Pfadvariable und hat im obigen Fall den Wert "Bamberg"
"""
@app.route("/weather/<city>", methods=['GET'])
def weather(city: str):
    current_temp = getCurrentTemp(city) # Hole die aktuelle Temperatur und speichere den Wert in der Variable current_temp
    title = 'Wetter in {0}'.format(city) # Der Titel der Webseite. Zum Formatieren von Zeichenkette siehe https://docs.python.org/3/tutorial/inputoutput.html

    # Rendere das Template weather.html mit den gegebenen Werten für title, city und current_temp und gib das Ergebnis zurück.
    return render_template("weather.html", title = title, city=city, current_temp = current_temp)


"""
Diese Methode gibt die geographische Lage als Paar (latitude, longitude) zurück
ACHTUNG: Momentan gibt diese immer die geographische Lage von Bamberg zurück.
TODO:   Ermittle die geographische Lage der Stadt city und gib diese zurück.
        Entweder über eine weitere API oder indem du für eine gewisse Menge 
        von Städten die Werte manuell zusammenträgst.
        Überlege dir, was passieren soll, wenn die Stadt nicht gefunden wird.
"""
def getGeoPos(city) :
    return (49.89873, 10.90067)


"""
Bestimm die aktuelle Temperatur in city mit Hilfe einer API

Beachte: Im Gegensatz zum Java (siehe spring-starter) sind wir in python nicht verpflichtet eventuelle Fehler zu behandeln. Was passiert hier, wenn du z.B. keine Verbindung zum Internet hast und die API also nicht verfügbar ist?
"""
def getCurrentTemp(city):
    lat, long = getGeoPos(city) # Bestimme geographische Breite und Länger von city
    r = requests.get("https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&current_weather=true".format(lat, long)) # Beschaffe Information zum Wetter über API
    res = json.loads(r.text) # Das Ergebnis ist ein JSON-Objekt, Informationen zum Aufbau der Antwort gibt es auf https://open-meteo.com/
    return res["current_weather"]["temperature"] # Die aktuelle Temperatur wird zurückgegeben. 
