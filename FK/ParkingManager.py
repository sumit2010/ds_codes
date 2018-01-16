import heapq
from collections import defaultdict

from FK.Car import Car
from FK.ParkingSlot import ParkingSlot
from FK.Ticket import Ticket


class ParkingManager:
    def __init__(self):
        pass

    def createParkingLot(self, capacity=0):
        self.capacity = capacity
        self.slots = [ParkingSlot(i) for i in range(capacity)]
        self.registrationNumberCarMap = defaultdict(Car)
        self.colorWithCarMap = defaultdict(list)
        self.emptySlots_Heap = []
        for s in self.slots:
            heapq.heappush(self.emptySlots_Heap, (s.getSlotNumber(), s))

        print "Created Parking with capacity %s" % (capacity)

    def getCarsWithColor(self, color):
        return self.colorWithCarMap[color]

    def getCarWithRegistrationNumber(self, regNo):
        return self.registrationNumberCarMap[regNo]

    def getRegistrationNumbersWithColor(self, color):
        return [c.getRegistrationNumber() for c in self.getCarsWithColor(color)]

    def getSlotNumberWithRegistrationNumber(self, regNo):
        return self.getCarWithRegistrationNumber(regNo).getSlot().getSlotNumber()

    def park(self, tkt):
        if tkt == None:
            return "Sorry, parking lot is full"
        slot = tkt.getSlot()
        car = tkt.getCar()

        self.colorWithCarMap[car.getColor()].append(car)
        self.registrationNumberCarMap[car.getRegistrationNumber()] = car
        car.setSlot(slot)
        slot.park(car)

    def getTicket(self, car):

        slot = self.getNearestParkingSlot()
        return Ticket(car, slot) if slot else None

    def getNearestParkingSlot(self):

        if len(self.emptySlots_Heap) == 0:
            return None
        nearestSlot = heapq.heappop(self.emptySlots_Heap)

        return nearestSlot[1]

    def leave(self, tkt):
        car = tkt.getCar()
        slot = tkt.getSlot()
        self.registrationNumberCarMap.pop(car.getRegistrationNumber())
        for i, o in enumerate(self.colorWithCarMap[car.getColor()]):
            if o == car:
                del self.colorWithCarMap[i]
                break
        # self.colorWithCarMap[car.getColor()].pop(car)
        heapq.heappush(self.emptySlots_Heap, (slot.getSlotNumber(), slot))
        return True

    def getStatus(self):

        occupiendSlots = [s for s in self.slots if not s.isEmpty()]

        for s in occupiendSlots:
            print s.getSlotNumber(), s.getCar().getRegistrationNumber(), s.getCar().getColor()
