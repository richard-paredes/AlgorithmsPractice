class SortingTests:
  
  def setUp(self):
    self.sort = self.create_sorting_algorithm()

  def test_sort_random_unsorted_array_returns_asc_sorted_array(self):
    unsorted_arr = [5, 2, 4, 6, 1, 3]
    sorted_arr = self.sort(unsorted_arr)
    
    self.assertSequenceEqual(sorted(unsorted_arr), sorted_arr)
  
  def test_sort_asc_sorted_array_returns_asc_sorted_array(self):
    asc_sorted_arr = [1, 2, 3, 4, 5, 6]
    sorted_arr = self.sort(asc_sorted_arr)

    self.assertSequenceEqual(asc_sorted_arr, sorted_arr)
  
  def test_sort_desc_sorted_array_returns_asc_sorted_array(self):
    desc_sorted_arr = [6, 5, 4, 3, 2, 1]
    sorted_arr = self.sort(desc_sorted_arr)

    self.assertSequenceEqual(sorted(desc_sorted_arr), sorted_arr)
