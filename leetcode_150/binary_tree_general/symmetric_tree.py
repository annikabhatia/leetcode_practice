# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        
        return self.isMirror(root.left, root.right)

    # we need a helper function since we are comparing 2 nodes at a time, and the regular function only has 1 parameter (which wont allow us to check if the tree is symmetric)
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
                
        return (left.val == right.val 
                    and self.isMirror(left.left, right.right)  
                    and self.isMirror(left.right, right.left))

            
            
