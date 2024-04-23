import time

def measure(unit):
    def wrapper(func):
        def inner():
            start = time.time()
            func()
            end = time.time()
            duration = end-start
            if unit == 'seconds':
                print(f"duration: {duration:.6f} seconds")
            if unit == 'microseconds':
                print(f"duration: {duration * 1e6:.2f} microseconds")
        return inner
    return wrapper

@measure(unit='microseconds')
def example():
    for i in range(1, 1000):
        print(i)
example()