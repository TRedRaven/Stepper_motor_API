#! /usr/bin/env python3.8
# import RPi.GPIO as io
import numpy as np

class motor():
    """this is the motor class this will allow control of any connected stepper motors."""
    @property
    def pins(self):
        """pins property, what pins have you connected to the pi"""
        if hasattr(self, "_pins"):
            return self._pins
        self._pins = [7,11,13,15]
        return self._pins


    @pins.setter
    def pins(self, value):
        """setter takes array like[int, int, int, int]"""
        self._pins = value


    def setup(self):
        """this will setup the pins set in """
        for pin in self.pins:
            io.setup(pin, io.OUTPUT)
            io.output(pin, 0)

    def clean(self):
        """just a easy way to call the cleanup method of RPi.GPIO"""
        io.cleanup()

    def spin(self, amount=360):
        """this will spin the motor by the given degree"""
        degree = (amount * 100 / 360) * 0.01




if __name__ == "__main__":
    mot = motor()
    mot.spin
