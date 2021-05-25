# Input: a set S of n points in the plane
# Output: The shortest cycle tour that visits each point in set S
def closest_pair(points: set):
  n = len(points)
  for i in range(1, n-1):
    distance = float('inf')
    # foreach pair of endpoints (s, t) from distance vertex chains
    #   if distance(s, t) <= distance then sm = s, tm = t, and distance = distance(s, t)
    # connect (sm, tm) by an edge
  # connect two endpoints by an edge
