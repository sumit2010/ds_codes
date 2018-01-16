from FK.ParkingManager import ParkingManager


class ParkingFactory:
    __instance = None

    def __init__(self):
        if ParkingFactory.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ParkingFactory.__instance = self

    @staticmethod
    def getInstance():
        if ParkingFactory.__instance is None:
            ParkingFactory()
        return ParkingFactory.__instance

    @staticmethod
    def getParkingManager():
        return ParkingManager()
