# https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def isValid(self, s):

        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["} #should make the closing brackets the keys since this is the deciding factor as to if the string is valid or not!
        for char in s:
            if char in closeToOpen: #checks if its a closing bracket
                if not stack or stack[-1] != closeToOpen[char]:
                    return False
                stack.pop()
            else: #if it as an opening bracket, add it to the stack
                stack.append(char)
        
        return not stack #if the stack is empty, then we know we found valid parentheses!