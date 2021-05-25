from typing import List

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    result = []

    for i in range(len(temperatures)):
      days = 0
      for j in range(i+1, len(temperatures)):
        days += 1
        if temperatures[j] > temperatures[i]:
          result.append(days)
        
      if i == len(temperatures) - 1:
        result.append(0)
    
    return result
  