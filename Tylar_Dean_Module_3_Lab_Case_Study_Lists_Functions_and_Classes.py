# ------------------------------------------------------------------------------------------
# Tylar Dean
# File name: Automobile app
# Description: This program defines two classes:
#              Vehicle (superclass)
#              Automobile (subclass of vehicle)
#              This program accepts user input to create an Automobile object,
#              then displays the entered details in a east to read format.
#
# Variables:
#     vehicle_type: str
#     year:         str
#     make:         str
#     model:        str
#     doors:        str
#     roof:         str
# -------------------------------------------------------------------------------------------

# Superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Subclass
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def display_info(self):
        """Prints automobile details in a easy to read format."""
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# ------------Main App--------------
def main():
    print("Enter the following details for your car:")

    # Get user input
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")

    # Create an Automobile object
    car = Automobile(year, make, model, doors, roof)

    print("\nHere are the details of your vehicle:\n")
    car.display_info()


# run the program
if __name__ == "__main__":
    main()