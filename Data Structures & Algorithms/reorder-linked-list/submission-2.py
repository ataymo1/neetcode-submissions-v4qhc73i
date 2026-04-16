# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        temp = slow.next
        slow.next = None
        slow = temp

        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        cur = head
        
        while cur and prev:
            tempSlow = prev.next
            tempCur = cur.next
            
            cur.next = prev
            prev.next = tempCur

            cur = tempCur
            prev = tempSlow






