from unittest import TestCase
from sorting_tests import SortingTests
from learning.sorting.heap_sort import heap_sort

class TestHeapSort(SortingTests, TestCase):

  def create_sorting_algorithm(self):
    return heap_sort