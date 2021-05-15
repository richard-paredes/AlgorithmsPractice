from unittest import TestCase
from sorting_tests import SortingTests
from sorting.insertion_sort import insertion_sort

class InsertionSortTests(SortingTests, TestCase):

  def create_sorting_algorithm(self):
    return insertion_sort