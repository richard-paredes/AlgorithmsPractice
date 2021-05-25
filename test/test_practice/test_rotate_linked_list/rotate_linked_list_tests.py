from utilities.list_node import ListNode

class RotateLinkedListTests:
  
  def setUp(self):
    self.rotate_linked_list = self.create_solution()
  
  def to_linked_list(self, arr):
    if len(arr) < 1:
      return None
    
    head = ListNode()
    head.val = arr[0]
    head.next = None
    
    tail = head
    for i in range(1, len(arr)):
      tail.next = ListNode()
      tail = tail.next
      tail.val = arr[i]
      
      
    return head

  def to_list(self, head):
    arr = []
    while head is not None:
      arr.append(head.val)
    
    return arr

  def test_returns_correct_output(self):
    linked_list = self.to_linked_list([1,2,3,4,5])

    output = self.rotate_linked_list(linked_list)

    self.assertEquals([4,5,1,2,3], self.to_list(output))