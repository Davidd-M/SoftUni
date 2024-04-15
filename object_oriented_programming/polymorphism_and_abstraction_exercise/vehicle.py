from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    ADDITIONAL_CONSUMPTION = 0.9  # liters per km

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if distance * (self.fuel_consumption+ self.ADDITIONAL_CONSUMPTION) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption+ self.ADDITIONAL_CONSUMPTION)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    ADDITIONAL_CONSUMPTION = 1.6  # liters per km

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if distance * (self.fuel_consumption+ self.ADDITIONAL_CONSUMPTION) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption+ self.ADDITIONAL_CONSUMPTION)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
