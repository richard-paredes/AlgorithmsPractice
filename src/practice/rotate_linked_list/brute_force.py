from utilities.list_node import ListNode

def rotateRight(head: ListNode, k: int) -> ListNode:
  num_nodes = count_num_nodes(head)
  
  if num_nodes < 1 or (k % num_nodes) == 0:
    return head
  
  node_to_rotate = num_nodes - (k % num_nodes)
  
  count = 0
  previous = None
  current = head
  while count < node_to_rotate:
    previous = current
    current = current.next
    count += 1
  
  previous.next = None
  new_head = current
  while current.next is not None:
    current = current.next
  
  current.next = head
  return new_head
    
    
    
  
def count_num_nodes(head: ListNode):
  count = 0
  curr = head
  while curr is not None:
    curr = curr.next
    count += 1
    
  return count