from abc import ABC, abstractmethod

# --- Реализация (Device) ---
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class TV(Device):
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")


class Radio(Device):
    def turn_on(self):
        print("Radio is ON")

    def turn_off(self):
        print("Radio is OFF")


# --- Абстракция (Remote) ---
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self, on: bool):
        if on:
            self.device.turn_on()
        else:
            self.device.turn_off()


# --- Использование ---
tv = TV()
radio = Radio()

remote1 = RemoteControl(tv)
remote2 = RemoteControl(radio)

remote1.toggle_power(True)   # TV is ON
remote2.toggle_power(True)   # Radio is ON
remote1.toggle_power(False)  # TV is OFF
remote2.toggle_power(False)  # Radio is OFF
