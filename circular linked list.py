class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def is_circular_linked_list(head):
    if not head:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

node1 = ListNode(10)
node2 = ListNode(200)
node3 = ListNode(3000)
node4 = ListNode(40000)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

print(is_circular_linked_list(node1))  
