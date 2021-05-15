def insertion_sort(arr):
  arr = arr[:] # make a copy
  for j in range(1, len(arr)):
    key = arr[j]
    # Insert A[j] into the sorted sequence A[1, ..., j-1]
    i = j - 1
    while (i > -1 and arr[i] > key):
      # Push every larger element over to the right
      arr[i + 1] = arr[i]
      i = i - 1
      # Once there are no more larger elements, replace the remaining duplicated element with the key
      arr[i + 1] = key
    
  return arr