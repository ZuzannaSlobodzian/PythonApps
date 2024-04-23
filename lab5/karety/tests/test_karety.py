import pytest

from fleet.ambulance import Ambulance
from operations.incident import Incident
from personnel.driver import Driver


def test_ambulance():
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    assert ambulance1 is not None


def test_incydent():
    incident1 = Incident("Power outage in sector 4", 1, "16:20", "Tom", "White", 879654789)
    assert incident1 is not None

def test_personnel():
    driver1 = Driver("Mike", "Johnson", 10000.0, "DL12345", ["BLS"])
    assert driver1 is not None


