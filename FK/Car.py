from enum import Enum


class Color(Enum):
    WHITE = 0
    BLACK = 1
    RED = 2
    BLUE = 3


class Car:
    def __init__(self, regNo, color):
        self.regNo = regNo
        self.color = color
        self.parked = False
        self.slot = None

    def isParked(self):
        return self.parked

    def setSlot(self, slot):
        self.sslot = slot
        return

    def getRegistrationNumber(self):
        return self.regNo

    def getColor(self):
        return self.color

    def getSlot(self):
        return self.slot
