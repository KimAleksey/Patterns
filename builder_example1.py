from abc import ABC, abstractmethod

# Строитель может создавать различные продукты, используя один
# и тот же процесс строительства.
class Car:
    """
    Автомобили могут отличаться комплектацией: типом
    двигателя, количеством сидений, могут иметь или не иметь
    GPS и систему навигации и т. д. Кроме того, автомобили
    могут быть городскими, спортивными или внедорожниками.
    """
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = None
        self.gps = None

    def __str__(self):
        return (f"Car(seats={self.seats}, engine={self.engine}, "
                f"trip_computer={self.trip_computer}, gps={self.gps})")


class Manual:
    """
    Руководство пользователя для данной конфигурации автомобиля.
    """
    def __init__(self):
        self.text = []

    def add(self, content):
        self.text.append(content)

    def __str__(self):
        return "\n".join(self.text)


class Builder(ABC):
    """
    Интерфейс строителя объявляет все возможные этапы и шаги
    конфигурации продукта.
    """
    @abstractmethod
    def reset(self): pass

    @abstractmethod
    def set_seats(self, number): pass

    @abstractmethod
    def set_engine(self, engine): pass

    @abstractmethod
    def set_trip_computer(self, enabled): pass

    @abstractmethod
    def set_gps(self, enabled): pass



class CarBuilder(Builder):
    """
    Все конкретные строители реализуют общий интерфейс по-своему.
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def set_seats(self, number):
        self.car.seats = number

    def set_engine(self, engine):
        self.car.engine = engine

    def set_trip_computer(self, enabled):
        self.car.trip_computer = enabled

    def set_gps(self, enabled):
        self.car.gps = enabled

    def get_result(self):
        return self.car


# В отличие от других порождающих паттернов, где продукты
# должны быть частью одной иерархии классов или следовать
# общему интерфейсу, строители могут создавать совершенно
# разные продукты, которые не имеют общего предка.

class CarManualBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.manual = Manual()

    def set_seats(self, number):
        self.manual.add(f"Car has {number} seats.")

    def set_engine(self, engine):
        self.manual.add(f"Engine type: {engine}.")

    def set_trip_computer(self, enabled):
        if enabled:
            self.manual.add("Trip computer installed.")
        else:
            self.manual.add("No trip computer.")

    def set_gps(self, enabled):
        if enabled:
            self.manual.add("GPS is available.")
        else:
            self.manual.add("GPS is not installed.")

    def get_result(self):
        return self.manual


class Director:
    """
    Директор знает, в какой последовательности нужно заставлять
    работать строителя, чтобы получить ту или иную версию
    продукта. Заметьте, что директор работает со строителем через
    общий интерфейс, благодаря чему он не знает тип продукта,
    который изготовляет строитель.
    """
    def construct_sports_car(self, builder: Builder):
        builder.reset()
        builder.set_seats(2)
        builder.set_engine("SportEngine")
        builder.set_trip_computer(True)
        builder.set_gps(True)


class Application:
    def make_car(self):
        director = Director()

        # Создание спортивной машины
        car_builder = CarBuilder()
        director.construct_sports_car(car_builder)
        car = car_builder.get_result()
        print("Car created:")
        print(car)
        print()

        # Создание руководства для спортивной машины
        manual_builder = CarManualBuilder()
        director.construct_sports_car(manual_builder)
        manual = manual_builder.get_result()

        print("Manual created:")
        print(manual)



if __name__ == "__main__":
    app = Application()
    app.make_car()
