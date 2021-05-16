from unittest import TestCase
from pattern_matching.substring_pattern_match import substring_pattern_match

class TestSubstringPatternMatch(TestCase):
  
  def setUp(self):
    self.match = substring_pattern_match

  def test_match_empty_string_in_nonempty_string_returns_0(self):
    self.assertEquals(0, self.match('aba', ''))
  
  def test_match_nonempty_string_in_empty_string_returns_negative_1(self):
    self.assertEquals(-1, self.match('', 'a'))
  
  def test_match_a_in_a_returns_0(self):
    self.assertEquals(0, self.match('a', 'a'))

  def test_match_abba_in_abaababbaba_returns_5(self):
    self.assertEquals(5, self.match('abaababbaba', 'abba'))
  
  def test_match_aba_in_ddd_returns_negative_1(self):
    self.assertEquals(-1, self.match('aba', 'ddd'))