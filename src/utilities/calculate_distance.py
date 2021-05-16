from math import sqrt

def distance(first_point, second_point):
  return sqrt((second_point.x - first_point.x)**2 + (second_point.y - first_point.y)**2)