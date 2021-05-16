def insertion_sort(array):
  arr = array[:]

  for j in range(1, len(arr)):
    i = j
    while (i > 0 and arr[i] < arr[i-1]):
      arr[i], arr[i-1] = arr[i-1], arr[i]
      i -= 1
    
  return arr