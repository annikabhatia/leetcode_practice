# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #each element has i 0's added to it, with i representing the index in the linked list

        current_l1 = l1
        counter_l1 = 0
        number_l1 = 0

        current_l2 = l2
        counter_l2 = 0
        number_l2 = 0
        
        while current_l1 is not None:
            number_l1 += (current_l1.val * (10**counter_l1))
            current_l1 = current_l1.next 
            counter_l1+=1

        while current_l2 is not None:
            number_l2 += (current_l2.val * (10**counter_l2))
            current_l2 = current_l2.next 
            counter_l2+=1

        total = number_l1 + number_l2

        #now, for converting the answer into the reversed linked list
        dummy = ListNode(0)
        tail = dummy

        if total == 0:
            return ListNode(0)

        while total > 0:
            digit = total % 10
            tail.next = ListNode(digit)
            tail = tail.next
            total //= 10

        return dummy.next
        
        