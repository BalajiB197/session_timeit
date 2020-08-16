import os
import session5
from session5 import *


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"
    
def test_print():
    session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons= 5)

def test_squared_power_list():
    session5.time_it(squared_power_list, 2, start=0, end=5, repetitons=1000)

def test_polygon_area():
    session5.time_it(polygon_area, 15, sides = 5, repetitons=10)

def test_temp_converter():
    session5.time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100) 

def test_speed_converter():
    session5.time_it(speed_converter,100, dist='m', time='s', repetitons=20) 

def test_speed_converter_2():
    session5.time_it(speed_converter, 100, dist='km', time='m', repetitons=200) 