from importlib import reload
from os import getcwd
import czas
import time

current_path = getcwd()
print(current_path)
print(czas.aktualny_czas)
time.sleep(20)
print(czas.aktualny_czas)
reload(czas)
print(czas.aktualny_czas)