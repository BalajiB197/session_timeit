import os
import session5
from session5 import *
import pytest


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"
    
def test_print():
    session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons= 5)

def test_squared_power_positive():
    session5.time_it(squared_power_list, 2, start=0, end=5, repetitons=1000)

def test_timeit():
    with pytest.raises(ValueError):
        session5.time_it(None)

def test_squared_power_negative():
    with pytest.raises(ValueError):
        session5.time_it(squared_power_list, -3, start=0, end=5, repetitons=1000)

def test_polygon_area_2():
    with pytest.raises(ValueError):
        session5.time_it(polygon_area, 15, sides = 2, repetitons=10)

def test_polygon_area_3():
    session5.time_it(polygon_area, 15, sides = 3, repetitons=10)

def test_polygon_area_4():
    session5.time_it(polygon_area, 15, sides = 4, repetitons=10)

def test_polygon_area_5():
    session5.time_it(polygon_area, 15, sides = 5, repetitons=10)

def test_polygon_area_6():
    session5.time_it(polygon_area, 15, sides = 6, repetitons=10)

def test_polygon_area_7():
    with pytest.raises(ValueError):
        session5.time_it(polygon_area, 15, sides = 7, repetitons=10)

def test_temp_converter_f():
    session5.time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100)

def test_temp_converter_c():
    session5.time_it(temp_converter, 35, temp_given_in = 'c', repetitons=100) 

def test_speed_converter_m_s():
    session5.time_it(speed_converter,100, dist='m', time='s', repetitons=200)

def test_speed_converter_m_m():
    session5.time_it(speed_converter,50, dist='m', time='m', repetitons=30)

def test_speed_converter_m_m1():
    session5.time_it(speed_converter,100, dist='m', time='m', repetitons=30)

def test_speed_converter_m_ms():
    session5.time_it(speed_converter,50, dist='m', time='ms', repetitons=25)

def test_speed_converter_feet_hr():
    session5.time_it(speed_converter, 35, dist='ft', time='hr', repetitons=10)

def test_speed_converter_feet_s():
    session5.time_it(speed_converter, 70, dist='ft', time='s', repetitons=10)

def test_speed_converter_yard_hr():
    session5.time_it(speed_converter, 30, dist='yrd', time='hr', repetitons=10)

def test_speed_converter_m_day():
    session5.time_it(speed_converter,80, dist='m', time='day', repetitons=101)

def test_speed_converter_m():
    session5.time_it(speed_converter, 100, dist='km', time='m', repetitons=200)

def test_speed_converter_s():
    session5.time_it(speed_converter, 110, dist='km', time='s', repetitons=150)

def test_speed_converter_ms():
    session5.time_it(speed_converter, 90, dist='km', time='ms', repetitons=120)

def test_speed_converter_day():
    session5.time_it(speed_converter, 150, dist='km', time='day', repetitons=101)

def test_speed_converter_yard_s():
    session5.time_it(speed_converter, 15, dist='yrd', time='s', repetitons=101)

def test_speed_converter_negative():
    with pytest.raises(ValueError):
        session5.time_it(speed_converter, -150, dist='km', time='day', repetitons=101) 