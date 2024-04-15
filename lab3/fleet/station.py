class Station:
    __max_id = 0

    def __init__(self, location, ambulance, driver, employee):
        Station.__max_id += 1
        self.id = Station.__max_id
        self.location = location # as (northing, easting)
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee

    def display_info(self):
        print("Station ID: " + str(self.id) + ", Location: " + str(self.location))
        print(self.ambulance.__str__())
        print(self.driver.display_info())
        print(self.employee.display_info())

    def is_ambulance_at_station(self):
        if self.location == self.ambulance.location:
            return True
        return False

