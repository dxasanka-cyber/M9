import random


# Car class
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Speed change
    def accelerate(self, change_in_speed):
        self.current_speed = self.current_speed + change_in_speed

# Check speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

# Car distance
    def drive(self, hours):

        distance_covered = self.current_speed * hours
        self.travelled_distance = self.travelled_distance + distance_covered

# Main
new_car = Car("ABC-123", 142)
print(f"Reg: {new_car.registration_number}, Max Speed: {new_car.maximum_speed}, "
      f"Current Speed: {new_car.current_speed}, Distance: {new_car.travelled_distance}")

# Acceleration
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(f"Speed after increases: {new_car.current_speed} km/h")
new_car.accelerate(-200)

# Emergency brake
print(f"Speed after emergency brake: {new_car.current_speed} km/h")

# Drive Method
new_car.current_speed = 60
new_car.travelled_distance = 2000
new_car.drive(1.5)
print(f"New distance after 1.5 hours: {new_car.travelled_distance} km")


# Car list
cars = []

# 10 Cars
for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_s = random.randint(100, 200)
    cars.append(Car(reg_num, max_s))

# Start the race loop
race_on = True

while race_on:
    for car in cars:

        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)

# Drive for 1 hour
        car.drive(1)

# Check if this car reached 10,000 km
        if car.travelled_distance >= 10000:
            race_on = False

# Result
print(f"{'Reg No':<10}  {'Max Speed':<12}  {'Final Speed':<12}  {'Distance'}")
print("-" * 55)

for car in cars:
    print(f"{car.registration_number:<10}  "f"{car.maximum_speed:<9} km/h  "f"{car.current_speed:<9} km/h  "f"{int(car.travelled_distance):<6} km")