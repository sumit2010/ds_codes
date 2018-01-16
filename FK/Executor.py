from FK.Car import Car, Color
from FK.ParkingFactory import ParkingFactory

if __name__ == '__main__':
    pk = ParkingFactory.getInstance()
    parkingManager = pk.getParkingManager()

    parkingManager.createParkingLot(6)

    t1 = parkingManager.getTicket(Car("KA01HH1234", Color.WHITE))
    parkingManager.park(t1)
    t2 = parkingManager.getTicket(Car("KA01HH9999", Color.WHITE))
    parkingManager.park(t2)
    t3 = parkingManager.getTicket(Car("KA01HH0001", Color.BLACK))
    parkingManager.park(t3)
    parkingManager.leave(t2)

    parkingManager.getStatus()
