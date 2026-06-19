# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2: #not None
            if list1.val < list2.val: 
                tail.next = list1 
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1: #if list1 still has more values and we went through all of list2
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next #skips the dummy variable to give us the actual list starting from the first value

# https://leetcode.com/problems/merge-two-sorted-lists/ 