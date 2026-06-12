# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def strStr(self, haystack, needle):

        if not needle:
            return 0
        
        size = len(needle)
        
        for char in range(0, len(haystack)):
            if haystack[char: char+size] == needle:
                return char
        return -1
    

# Test cases
solution = Solution()   
print(solution.strStr("hello!annika", "anni"))  
print(solution.strStr("practice_leetcode", "leetc"))    
