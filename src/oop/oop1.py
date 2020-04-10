# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#Base Class
class Vehicle:
    pass

#Child of Vehicle - Derived Class

class FlightVehicle(Vehicle):
    pass

class GroundVehicle(Vehicle):
    pass

#Child of FlightVehicle - Derived Class

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass
#Child of GroundVehicle - Derived Class

class Car(GroundVehicle):
    pass 

class Motorcycle(GroundVehicle):
    pass
