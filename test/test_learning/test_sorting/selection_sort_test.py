from unittest import TestCase
from sorting_tests import SortingTests
from learning.sorting.selection_sort import selection_sort

class TestSelectionSort(SortingTests, TestCase):

  def create_sorting_algorithm(self):
    return selection_sort