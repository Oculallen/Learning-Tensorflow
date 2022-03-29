#Decorators used for ADA structure
import time
from housepricegeneration import *

def timer(func):
    """
    This is a default and flexible timer decorator for all functions

    Notes
    -----
     - Called by placing @timer above a function or class (when classes are instantiated only or when
       the __new__ function of a class is called)
     - Prints a value in seconds
    """

    def wrapper_timer(*args, **kwargs):
        startTime = time.perf_counter()
        value = func(*args, **kwargs)
        endTime = time.perf_counter()
        runTime = endTime - startTime
        print(f'{func.__name__!r}() Completed in: {runTime}s')
        return value
    return wrapper_timer

def debug(func):
    """
    A flexible debug function for classes and functions (see above for specifics)

    Notes
    -----
     - Called by placing @debug above a function or class
     - Prints the arguments supplied to a function as well as status messages
     - Comes with built in fancy error handling
    """
    def wrapper_debug(*args, **kwargs):
        argsRepr = [f'{x!r}' for x in args]
        kwargsRepr = [f'{kword!r}={val!r}' for kword, val in kwargs.values()]
        signature = ' ,'.join(argsRepr + kwargsRepr)
        print(f'Function {func.__name__!r} called with: ({signature})')
        try:
            value = func(*args, **kwargs)
            print(f'Function {func.__name__!r} successfully run')
            return value
        except BaseException as err:
            print(f'Function {func.__name__!r} failed with error: {err!r}')
            return None
    return wrapper_debug
            