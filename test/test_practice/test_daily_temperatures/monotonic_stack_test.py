from unittest import TestCase
from daily_temperature_tests import DailyTemperatureTests
from practice.daily_temperatures.monotonic_stack import dailyTemperatures

class TestMonotonicStackSolution(DailytemperatureTests, TestCase):
  
  def create_solution(self):
    return dailyTemperatures