from unittest import TestCase
from pattern_matching.substring_pattern_match import substring_pattern_match

class TestSubstringPatternMatch(TestCase):
  
  def setUp(self):
    self.match = substring_pattern_match

  def test_match_abba_in_abaababbaba_returns_5(self):
    self.assertEquals(5, self.match('abbaababbaba', 'abba'))