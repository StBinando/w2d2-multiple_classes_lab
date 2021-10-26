class Bus:
    def __init__(self, route, destination):
        self.route_number = route
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        self.passengers.extend(bus_stop.queue)
        bus_stop.clear()