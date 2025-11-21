from abc import ABC, abstractmethod

# --- Продукт ---
class Transport(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Transport):
    def drive(self):
        return "Еду на машине"


class Bike(Transport):
    def drive(self):
        return "Еду на велосипеде"


# --- Создатель (Creator) ---
class TransportCreator(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def start_trip(self):
        transport = self.create_transport()
        return transport.drive()


# --- Конкретные создатели ---
class CarCreator(TransportCreator):
    def create_transport(self) -> Transport:
        return Car()


class BikeCreator(TransportCreator):
    def create_transport(self) -> Transport:
        return Bike()


# --- Использование ---
car_creator = CarCreator()
print(car_creator.start_trip())   # Еду на машине

bike_creator = BikeCreator()
print(bike_creator.start_trip())  # Еду на велосипеде
