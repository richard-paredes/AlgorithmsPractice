from typing import List

# Monotonic stack
## Helps us identify smallest values when stack is in ascending
## Helps us identify largest values when stack is descending (*)
# Reference: https://www.youtube.com/watch?v=m4hvxzLoN_I
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
  stack = []
  result = [0 for i in range(len(temperatures))]

  for i in range(len(temperatures)):
    while len(stack) > 0 and stack[-1][0] < temperatures[i]:
      (temp, idx) = stack.pop()
      result[idx] = i - idx
    
    stack.append((temperatures[i], i))

  return result