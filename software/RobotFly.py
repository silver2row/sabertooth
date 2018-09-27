#!/usr/bin/python

from pysabertooth import Sabertooth
from flask import Flask, render_template

import time

# on the beaglebone related boards, use P9_21 for UART2 and set up config-pin.

# attach P9_21 to S1 on the sabertooth 2 x 12 and attach GND on the sabertooth to GND on your BBB.

saber = Sabertooth("/dev/ttyO2", baudrate=9600, address=128, timeout=0.1)

# for instance, sudo config-pin P9.21 uart, that cmd will do it.

# start and enable a service, start a cron job, or make an executable .sh file.

app = Flask(__name__)
@app.route("/")
@app.route("/<state>")

def updates(state=None):
    if state == "F":
        print "Robot Moving Forward"
        saber.drive(1, 100)
        saber.drive(2, 100)
        #time.sleep(.2)
    if state == "R":
        print "Robot Turning Right"
        saber.drive(1, 75)
        saber.drive(2, 25)
        #time.sleep(.2)
    if state == "L":
        print "Robot Turning Left"
        saber.drive(1, 25)
        saber.drive(2, 75)
        #time.sleep(.2)
    if state == "S":
        print "Robot Stopped"
        saber.drive(1, 0)
        saber.drive(2, 0)
        saber.stop()
        #time.sleep(.2)
    template_data = {
        "title" : state,
    }
    return render_template("Saber.html", **template_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
