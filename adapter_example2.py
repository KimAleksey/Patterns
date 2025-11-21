# --- Старый интерфейс ---
class OldInterface:
    def request(self):
        return "Старый интерфейс: request()"


# --- Новый несовместимый класс ---
class NewSystem:
    def specific_request(self):
        return "Новый интерфейс: specific_request()"


# --- Адаптер ---
class Adapter(OldInterface):
    def __init__(self, new_system: NewSystem):
        self.new_system = new_system

    def request(self):
        # адаптируем новый метод под старое имя
        return self.new_system.specific_request()


# --- Клиентский код ---
def client_code(obj: OldInterface):
    print(obj.request())


# --- Использование ---
old = OldInterface()
client_code(old)   # Старый интерфейс: request()

adapter = Adapter(NewSystem())
client_code(adapter)  # Новый интерфейс: specific_request()
