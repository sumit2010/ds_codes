import itertools


class Ticket:
    newid = itertools.count().next

    def __init__(self, car, slot):
        self.id = Ticket.newid()
        self.car = car
        self.slot = slot

    def setSlot(self, s):
        self.slot = s

    def getSlot(self):
        return self.slot

    def getCar(self):
        return self.car
