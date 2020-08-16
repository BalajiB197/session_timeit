import math
import time


def time_it(fn, *args, repetitons= 1, **kwargs):
    start_time = time.time()
    for _ in range(repetitons):
        if fn.__name__ == 'print':
            print(*args, **kwargs)
        elif fn.__name__ == 'squared_power_list':
            squared_power_list(*args, **kwargs)
        elif fn.__name__ == 'polygon_area':
            polygon_area(*args, **kwargs)
        elif fn.__name__ == 'temp_converter':
            temp_converter(*args, **kwargs)
        elif fn.__name__ == 'speed_converter':
            speed_converter(*args, **kwargs)
        else:
            print("Not defined")
    end_time = time.time()
    seconds = end_time - start_time
    print('Time Taken:', seconds/repetitons)


def squared_power_list(*args, **kwargs):
    value = args[0]
    start = kwargs['start']
    end = kwargs['end']
    a = []
    for j in range(start, end+1):
        a.append(pow(value,j)) 

def polygon_area(*args, **kwargs):
    value = args[0]
    sides = kwargs['sides']
    if sides>=3 and sides<7:
        if sides == 3:
            A = (math.sqrt(3)/4)*value*value
        elif sides == 4:
            A = 2 * value
        elif sides == 5:
            P = sides * value
            a = value / 15.5
            A = P*a/ 2
        elif sides == 6:
            P = 6 * value
            a = value / -12.81
            A = P*a/ 2

def temp_converter(*args, **kwargs):
    value = args[0]
    temp_given_in = kwargs['temp_given_in']
    if temp_given_in == 'f':
        Celsius = (value - 32) * 5/9
    elif temp_given_in == 'c':
        Fahrenheit = (value * 9/5) + 32

def speed_converter(*args, **kwargs):
    value = args[0]
    _ = kwargs['dist']
    time = kwargs['time']
    if time == 'm': # ms/s/m/hr/day,
        conv = value / 60  
    elif time == 's':
        conv = value / 3600
    elif time == 'ms':
        conv = value / 3600000
    elif time == 'day':
        conv = value * 24
