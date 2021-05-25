from unittest import TestCase
from rotatete_linked_list_tests import RotateLinkedListTests
from practice.rotate_linked_list.brute_force import rotateRight

class TestBruteForceSolution(RotateLinkedListTests, TestCase):
  
  def create_solution(self):
    return rotateRight