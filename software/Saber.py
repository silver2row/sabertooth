#!/usr/bin/python

from pysabertooth import Sabertooth
import time

saber = Sabertooth("/dev/ttyS1", baudrate=9600, address=128, timeout=0.1)

saber.drive(1, 85)
saber.drive(2, 85)
saber.stop()
time.sleep(15)

saber.drive(1, -60)
saber.drive(2, -60)
time.sleep(5)

saber.stop()
saber.close()
