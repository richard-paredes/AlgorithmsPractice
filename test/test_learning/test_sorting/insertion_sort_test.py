from unittest import TestCase
from sorting_tests import SortingTests
from learning.sorting.insertion_sort import insertion_sort

class TestInsertionSort(SortingTests, TestCase):

  def create_sorting_algorithm(self):
    return insertion_sort