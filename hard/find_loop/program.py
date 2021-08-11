# time = O(n) and space = O(1)
def findLoop(head):
    slow = head.next
    fast = head.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow