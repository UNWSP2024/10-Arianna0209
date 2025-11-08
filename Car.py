# Program # 2: Car Class
# Write a class named Car that has the following data attributes:

# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's
# year model and make as arguments.  These values should be assigned to
# the object's __year_model and __make data attributes.  It should also assign
# 0 to the __speed data attribute.

# The class should also have the following methods:

# The accelerate method should add 5 to the speed data attribute each time it it called.
# The brake method should subtract 5 from the speed data attribute each time it is called.
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five times.
# After each call to the accelerate method, get the current speed of the car and display it.
# The call the brake method.  After each call to the brake method, get the current speed of
# the car and display it.

# Title: Car Class
# Author: Arianna Endres
# Date: 11/07/2025

class Car:
    # Define the attributes of the Car class.
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # The accelerate method adds 5 to the car's speed.
    def accelerate(self):
        self.__speed += 5

    # The brake method subtracts 5 from the car's speed.
    # The speed cannot be negative, so if the initial speed is less
    # than 5 an error message will show.
    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            print('Error: Insufficient speed')

    # The get_speed method simply returns the current speed.
    def get_speed(self):
        return self.__speed

def main():

    # Create a car object and print its current speed.
    car1 = Car('year_model', 'make')
    print(f'The current speed of the car is {car1.get_speed()}')

    # Accelerate 5 times and print speed each time.
    for speed in range(0, 5):
        car1.accelerate()
        print(f'I accelerated the car. The current speed is now {car1.get_speed()}')

    # Brake 5 times and print speed each time.
    for speed in range(0, 5):
        car1.brake()
        print(f'I braked the car. The current speed is now {car1.get_speed()}')

# Call the main function.
if __name__ == '__main__':
    main()