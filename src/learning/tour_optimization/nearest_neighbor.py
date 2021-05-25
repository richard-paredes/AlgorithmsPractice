from utilities.calculate_distance import distance

# Input: a set S of n points in the plane
# Output: The shortest cycle tour that visits each point in set S
def nearest_neighbor(points: set):
  if len(points) < 1:
    return
  
  unvisited = points
  current_point = points.pop()
  visited = {current_point}
  
  i = 0
  while len(unvisited) > 0:
    i += 1

    next_point = None
    for point in visited:

      if next_point == None or distance(current_point, point) < distance(current_point, next_point):
        next_point = point
    
    unvisited.remove(next_point)
    visited.add(next_point)
    current_point = next_point

  return visited

# Disadvantages to this algorithm:
'''
It is an incorrect algorithm for the problem at hand.
This is a greedy algorithm, so it looks to get the next unvisited point with the smallest distance.
This means that if the points are designed such that they all lie on a straight line and the next smallest point cycles between backwards and forwards in direction, the output is not the optimal distance
Example of this is in The Algorithm Design Manual, pg. 6
'''