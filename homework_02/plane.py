"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
# в модуле plane создайте класс Plane
# класс Plane должен быть наследником Vehicle
# добавьте атрибуты cargo и max_cargo классу Plane
# добавьте max_cargo в инициализатор (переопределите родительский)
# объявите метод load_cargo, который принимает число, проверяет, что в сумме с текущим cargo не будет перегруза, и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload
# объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo, которое было до обнуления

class Plane(Vehicle):
    cargo = 0
    cargo_max = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo_load):
        sum_cargo = self.cargo + cargo_load
        if sum_cargo <= self.max_cargo:
            self.cargo = sum_cargo
        else:
            raise CargoOverload
        
    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo