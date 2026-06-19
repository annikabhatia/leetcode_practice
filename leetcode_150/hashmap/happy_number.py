class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()

        while n != 1:
            if n in seen:
                return False #cycle detected, means you are in  a loop and will never reach 1
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n)) #convert, square, sum in one line
        
        return True