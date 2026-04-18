# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from functools import cache
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur_node = head
        next_node = head.next

        while next_node:

            new_node = ListNode(self.gcd(cur_node.val, next_node.val), next_node)
            cur_node.next = new_node
            
            cur_node = next_node
            next_node = next_node.next

        return head


    def gcd(self, num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1


        