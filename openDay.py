#! /usr/bin/env python3.8

import RPi.GPIO as io
import numpy as np
import time

class motor():
    """this is the motor class this will allow control of any connected stepper motors."""

    def __init__(self):
        io.setmode(io.BOARD)

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

    @property
    def activations(self):
        """this will contain the activations of the pins"""
        if hasattr(self, "_activations"):
            return self._activations
        self._activations = [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]
        ]
        return self._activations

    def setup(self):
        """this will setup the pins set in """
        for pin in self.pins:
            io.setup(pin, io.OUT)
            io.output(pin, 0)

    def clean(self):
        """just a easy way to call the cleanup method of RPi.GPIO"""
        io.cleanup()

    def spin(self, amount=360):
        """this will spin the motor by the given degree"""
        degree = (amount * 100 / 360) * 0.01
        turn = int(512 * degree)
        # turning left
        if turn < 0:
            for i in range(abs(turn)):
                for activation in range(len(self.activations)):
                    for pin in range(len(self.pins)):
                        io.output(self.pins[-1][pin], self.activations[::-1][activation][pin])
                    time.sleep(0.001)
        # truning right
        else:
            for i in range(abs(turn)):
                for activation in range(len(self.activations)):
                    for pin in range(len(self.pins)):
                        io.output(self.pins[-1][pin], self.activations[-1][activation][pin])
                    time.sleep(0.001)

        # turning the pins off so the motor doesn't burn to a crisp
        for pin in self.pins:
            io.output(pin, 0)


if __name__ == "__main__":
    mot = motor()
    mot.setup()
    mot.spin()
