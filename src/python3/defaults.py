from time import time

# decorator to measure the time of a function
def measure_time(func):
    def wrapper(*args, **kwargs):
        start: int = time()
        output = func(*args, **kwargs)
        end_in_str: int = str(time() - start)
        print(f"Time elapsed: {end_in_str} s for '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        return output
    return wrapper


class Timer:
    def __init__(self):
        self.start: float = None
        self.last: float = None
    
    def __enter__(self):
        self.start = time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.last = time() - self.start
        print(f'Time elapsed: {str(self.last)}s')

timer = Timer()