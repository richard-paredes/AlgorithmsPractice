class WiggleSortTests:
  def setUp(self):
    self.wiggle_sort = self.create_solution()
  
  def test_returns_correct_output(self):
    arr = [1,5,1,1,6,4]

    self.wiggle_sort(arr)

    self.assertSequenceEquals([1,5,1,6,1,4], arr)