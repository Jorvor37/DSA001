"""
Q: Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
I solve this problem use simple if else and linked list
1. create ListNode with head and current
2. use while loop to loop until all value in list is passed
3. use simple if else to compare value and then assign the order
4. return head of list
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        current = head

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        return head.next
