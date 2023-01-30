class AirVehicle:
    ...
    def fly(self):
        ...

class Aircraft(AirVehicle):
    def fly(self):
        ...


class Airplane(Aircraft):
    def fly(self):
        ...


class Helicopter(Aircraft):
    def fly(self):
        ...


class AircraftPart:
    ...


class Wing(AircraftPart):
    ...


class Flap(AircraftPart):
    ...
