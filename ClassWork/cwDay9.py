class Vehicle:
    def display_details(self):
        print("Vehicle ID:", self._vehicle_id)
        print("Base Rate:", self._base_rate)

    def rental_charge(self):
        return 0.0


class Car(Vehicle):
    def rental_charge(self):
        return self._base_rate * self.num_seats


class Bike(Vehicle):
    def rental_charge(self):
        return self._base_rate * 0.5


def calculate_rental(vehicle):
    return vehicle.rental_charge()


car1 = Car()
car1._vehicle_id = "CAR001"
car1._base_rate = 100
car1.num_seats = 4


bike1 = Bike()
bike1._vehicle_id = "BIKE001"
bike1._base_rate = 80
bike1.bike_type = "Scooter"


print("----- Car Details -----")
car1.display_details()
print("Rental Charge:", calculate_rental(car1))

print()

print("----- Bike Details -----")
bike1.display_details()
print("Rental Charge:", calculate_rental(bike1))
