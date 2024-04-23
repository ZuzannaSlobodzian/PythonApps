from fleet.ambulance import Ambulance
from fleet.station import Station
from karety.utils.parse_cli_args import parse_args
from operations import *
from personnel import *
from karety.utils.get_logger import get_logger

def run_application():
    logger = get_logger(__name__)

    args = parse_args()
    print(args.verbosity)
    print(args)

    if args.karety == args.woznice == args.stajenni == args.stajnie:
        print("masz wystarczajaco zasobów")
    else:
        logger.error("brak zasobów")

    # zdefiniowanie naszych zasobów
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 12000.0)
    employee2 = Employee("Jane", "Smith", 8000.0)

    driver1 = Driver("Mike", "Johnson", 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 11500.0, "DL12346", ["ALS", "PHTLS"])

    # sprawdzenie czy to czasem nie są te same karetki
    #error - te same karetki
    if ambulance1 == ambulance2:
        logger.error("To są te same karetki!")
        # raise ValueError("To są te same karetki!")

    # sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    # ile mamy pracowników i kierowców
    print("number of employees:")
    print(Employee.get_max_id())
    print(employee1.display_info())
    print(employee2.display_info())
    print(driver1.display_info())
    print(driver2.display_info())

    #robimy stację
    print("Station")
    station1 = Station((50.095340, 18.920282), ambulance1, driver1, employee1)
    station1.display_info()
    print(station1.is_ambulance_at_station())

    # stworzenie kolejki
    queue = IncidentQueue()

    # zaraportowanie 2 zgłoszeń
    incident1 = Incident("Power outage in sector 4", 1, "16:20", "Tom", "White", 879654789)
    incident2 = Incident("Fire alarm in building 21", 2, "17:40", "Eve", "Cooper", 768998765)
    # queue += incident1
    # queue += incident2

    #warning pusta kolejka
    if not queue:
        logger.warning("kolejka jest pusta")

    # wypisz wszystkie zgłoszenia
    print("Aktualne zgłoszenia:")
    print(queue)

    # daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")

if __name__ == "__main__":
    run_application()