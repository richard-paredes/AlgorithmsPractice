from typing import List

# This algorithm involves two steps:
## Find the median. Can be done in O(n) by using nth_element (numpy has an implementation in python)
##  Nth_element is similar to partial_sort, in that it partially orders a range of elements: it arranges the range [first, last) such that the element pointed to by the iterator nth is the same as the element that would be in that position if the entire range [first, last) had been sorted. Additionally, none of the elements in the range [nth, last) is less than any of the elements in the range [first, nth).
## Then interleave the elements so that they adhere to wigglesort.
##   This can be done in O(n) using the three-way partition algorithm.
# References:
##  nth_element: https://en.wikipedia.org/wiki/Selection_algorithm
##  three-way-partition: https://en.wikipedia.org/wiki/Dutch_national_flag_problem#Pseudocode
def wiggleSort(nums: List[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  # didn't want to implement the nth_element, so just get the median by sorting. Increases time complexity to O(nlogn)
  nums.sort()
  n = len(nums)
  if n < 2:
    return nums
  
  mid = nums[(n + 1) // 2]
  
  i = (n - 1) // 2 * 2
  j = i
  k = 1
  
  for c in range(len(nums)):
    if nums[j] < mid:
      nums[i], nums[j] = nums[j], nums[i]
      i -= 2
      j -= 2
    elif nums[j] > mid:
      nums[j], nums[k] = nums[k], nums[j]
      k += 2
    else:
      j -= 2
    if j < 0: 
        j = n // 2 * 2 - 1
