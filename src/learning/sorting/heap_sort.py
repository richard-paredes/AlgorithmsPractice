class PriorityQueue:
  
  def __init__(self, size):
    self.queue = [-1 for i in range(size + 1)]
    self.MAX_SIZE = size
    self.num_elements = 0
  
  def initialize(self):
    self.num_elements = 0
  
  def parent(self, n):
    if n == 1:
      return -1
    
    return n // 2
  
  def child(self, n):
    return 2*n
  
  def insert(self, item):
    if self.num_elements >= self.MAX_SIZE:
      print('Priority queue is full')
    else:
      self.num_elements += 1
      self.queue[self.num_elements] = item
      self.bubble_up(self.num_elements)
  
  def bubble_up(self, idx):
    if self.parent(idx) == -1:
      return
    
    if self.queue[self.parent(idx)] > self.queue[idx]:
      self.swap(self.parent(idx), idx)
      self.bubble_up(self.parent(idx))
  
  def swap(self, a, b):
    self.queue[a], self.queue[b] = self.queue[b], self.queue[a]
  
  def make_heap(self, array):
    self.initialize()

    for i in range(len(array)):
      self.insert(array[i])
  
  def optimized_make_heap(self, array):
    self.initialize()
    self.num_elements = len(array)
    
    for i in range(len(array)):
      self.queue[i + 1] = array[i]
    
    for i in range(self.num_elements//2, 0, -1):
      self.bubble_down(i)
    
  
  def extract_minimum(self):
    minimum = -1
    
    if self.num_elements <= 0:
      print('Priority queue is empty')
    else:
      minimum = self.queue[1]

      self.queue[1] = self.queue[self.num_elements]
      self.num_elements = self.num_elements - 1
      self.bubble_down(1)
    
    return minimum
  
  def bubble_down(self, idx):
    child = self.child(idx)
    min_idx = idx

    for i in range(2):
      if child + i <= self.num_elements:
        if self.queue[min_idx] > self.queue[child + i]:
          min_idx = child + i
    
    if min_idx != idx:
      self.swap(idx, min_idx)
      self.bubble_down(min_idx)

def heap_sort(array):
  arr = array[:]
  priority_queue = PriorityQueue(len(array))
#   priority_queue.make_heap(arr)
  priority_queue.optimized_make_heap(arr)
  
  for i in range(len(arr)):
    arr[i] = priority_queue.extract_minimum()
  
  return arr