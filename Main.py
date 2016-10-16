from flask import Flask, render_template
from geopy.geocoders import Nominatim
import random
import pyredb
import time

app = Flask(__name__)
geolocator = Nominatim()

def hexadecimalf():
    hexadecimal = "#"
    sumi = 0
    for i in range(0, 6):
        a = random.randint(48, 70)
        while 58 <= a <= 64:
            a = random.randint(48,70)
        hexadecimal += chr(a)
        sumi += a
    if sumi < 700:
        return hexadecimal
    else:
        return hexadecimalf()

@app.route("/")
def index():
    data = pyredb.WaitNoMore().getAll()
    names = []
    print(data)
    findWaitTime(data)
    clinicNames= []
    for obj1 in range(len(data)):
        clinicInfo = {
            'clinic_name' : data[obj1][4],
            'end_time' : data[obj1][1],
            'location' : data[obj1][3],
            'start_time': data[obj1][0]
        }
        clinicNames.append(data[obj1][4])

        names.append(clinicInfo);

    clinicNames = list(set(clinicNames))
    print(clinicNames)

    return render_template("index.html", names = names)

def findWaitTime(data):
    print("c")
    print(time.strftime("%H:%M", time.gmtime()))

if __name__ == "__main__":
    pyredb.WaitNoMore().start()
    app.run()



