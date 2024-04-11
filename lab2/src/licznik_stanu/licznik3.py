class Licznik:
    z = 0

    def __init__(self):
        Licznik.z += 1

    def __call__(self, *args, **kwargs):
        print(str(self.z))


