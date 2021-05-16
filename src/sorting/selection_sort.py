def selection_sort(array):
  arr = array[:]
  for i in range(len(arr)):
    index_of_minimum = i

    for j in range(i + 1, len(arr)):
      if arr[j] < arr[index_of_minimum]:
        index_of_minimum = j
    
    arr[i], arr[index_of_minimum] = arr[index_of_minimum], arr[i]

  return arr