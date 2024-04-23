import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Zasoby do karety")
    parser.add_argument("--karety", "-k", required=True, help="Ilosc karet:")
    parser.add_argument("--woznice", "-w", required=True, help="Ilosc woznic:")
    parser.add_argument("--stajenni", "-p", required=True, help="Ilosc stajennych:")
    parser.add_argument("--stajnie", "-s", required=True, help="Ilosc stajni:")

    parser.add_argument("--verbosity", "-v", help="Zwiększa szczegółowość logowania", action="store_true")
    
    return parser.parse_args()