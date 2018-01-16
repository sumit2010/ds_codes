class ParkingSlot:
    def __init__(self, slotNo):
        self.slotNumber = slotNo
        self.isAvailable = True
        self.car = None

    def park(self, c):
        self.car = c
        self.isAvailable = False

    def getSlotNumber(self):
        return self.slotNumber

    def removeCar(self):
        self.isAvailable = True

    def isEmpty(self):
        return self.isAvailable

    def getCar(self):
        return self.car
