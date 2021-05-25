from unittest import TestCase
from daily_temperature_tests import DailyTemperatureTests
from practice.daily_temperatures.brute_force import dailyTemperatures

class TestBruteForceSolution(DailytemperatureTests, TestCase):
  
  def create_solution(self):
    return dailyTemperatures