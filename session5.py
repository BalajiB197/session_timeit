import math
import time


def time_it(fn, *args, repetitons= 1, **kwargs):
    '''
    *args - accept all the positional value
    **kwargs - accept all named arguments
    repetitons - run the method to execute for the specified number
    of times.
    fn - function name
    '''
    start_time = time.time()
    if fn:
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
        raise ValueError("No function call")
    end_time = time.time()
    seconds = end_time - start_time
    return seconds/repetitons

def squared_power_list(*args, **kwargs):
    value = args[0]
    start = kwargs['start']
    end = kwargs['end']
    a = []
    if value > 0:
        if start >= 0:
            for j in range(start, end+1):
                a.append(pow(value,j)) 
    else:
        raise ValueError("No negative")

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
    else:
        raise ValueError("Sides should be between 3 to 6")

def temp_converter(*args, **kwargs):
    value = args[0]
    temp_given_in = kwargs['temp_given_in']
    if temp_given_in == 'f':
        Celsius = (value - 32) * 5/9
    elif temp_given_in == 'c':
        Fahrenheit = (value * 9/5) + 32

def speed_converter(*args, **kwargs):
    value = args[0]
    dist = kwargs['dist']
    time = kwargs['time']
    if value >= 0:
        if dist == 'km':
            if time == 'm': 
                conv = value / 60  
            elif time == 's':
                conv = value / 3600
            elif time == 'ms':
                conv = value * 0.0417
            elif time == 'day':
                conv = value * 24
        elif dist == 'm':
            if time == 'm': 
                conv = value * 0.277778 
            elif time == 's':
                conv = value * 0.277778
            elif time == 'ms':
                conv = value / 3600000
            elif time == 'day':
                conv = value * 24
        elif dist == 'ft':
            if time == 'hr':
                conv = value * 3280.83
            elif time == 's':
                conv = value * 0.91134442
        elif dist == 'yrd':
            if time == 'hr':
                conv = value * 1093.61
            elif time == 's':
                conv = value *  0.30378 
    else:
        raise ValueError("Error!!! Value cannot be Negative")
