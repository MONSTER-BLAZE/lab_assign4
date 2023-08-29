class Flight:
    def __init__(self, flight_id, source, destination, price):
            self.flight_id = flight_id
            self.source = source
            self.destination = destination
            self.price = price

class FlightDatabase:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_flight_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
                return None

    def search_by_source(self, source):
        result = []
        for flight in self.flights:
            if flight.source == source:
                result.append(flight)
            return result

    def search_by_destination(self, destination):
        result = []
        for flight in self.flights:
            if flight.destination == destination:
                result.append(flight)
                return result

def main():
    flight_db = FlightDatabase()

    # Adding flights to the database
    flight_db.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_db.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_db.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_db.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_db.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_db.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    user_input = int(input("Enter search type (1 for Flight ID, 2 for source, 3 for destination): "))

    if user_input == 1:
        flight_id = input("Enter Flight ID: ")
        flight = flight_db.search_by_flight_id(flight_id)
        if flight:
            print("Flight found!")
            print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
        else:
            print("Flight not found.")
    elif user_input == 2:
        source = input("Enter Source city: ")
        flights = flight_db.search_by_source(source)
        if flights:
            print("Flights found!")
            for flight in flights:
                print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
        else:
            print("No flights found.")

    elif user_input == 3:
        destination = input("Enter Destination city: ")
        flights = flight_db.search_by_destination(destination)
        if flights:
            print("Flights found!")
        for flight in flights:
            print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
        else:
            print("No flights found.")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()