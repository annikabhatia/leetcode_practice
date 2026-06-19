# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        #if both null, return true
        if p == None and q == None:
            return True

        #if only 1 is null or both values are not equal, immediately false
        #won't return false if the values are equal, therefore it will return True
        if p == None or q == None or p.val != q.val:
            return False
        
        #recursively check over subtrees
        check_left = self.isSameTree(p.left, q.left)
        check_right = self.isSameTree(p.right, q.right)

        #checks if left and right subtrees are identical recursively
        return check_left and check_right