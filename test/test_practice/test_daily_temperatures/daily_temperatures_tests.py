class DailyTemperatureTests:
  
  def setUp(self):
    self.daily_temperatures = self.create_solution()
  
  def test_returns_correct_output(self):
    temperatures = [73,74,75,71,69,72,76,73]

    self.assertSequenceEquals([1,1,4,2,1,1,0,0], self.daily_temperatures)
  
