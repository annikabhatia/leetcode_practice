# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        #Floyd's Cycle Detection
        #space complexity: O(1), time complexity: O(n)

        slow = head
        fast = head

        while fast and fast.next:
            #move slow 1 step
            slow = slow.next
            #move fast 2 steps
            fast = fast.next.next

            #if a cycle exists, the fast pointer will eventually meet the slow pointer
            if slow == fast:
                return True

        return False
        
        