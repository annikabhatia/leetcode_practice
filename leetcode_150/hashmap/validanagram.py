# https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def isAnagram(self, s, t):

        word1 = {}
        word2 = {}

        for char in s:
            if char in word1:
                word1[char] += 1
            else:
                word1[char] = 1

        for char in t:
            if char in word2:
                word2[char] += 1
            else:
                word2[char] = 1

        return word1 == word2
    
# Test cases
solution = Solution()   
print(solution.isAnagram("annikabhatia", "bhatikaannia"))
print(solution.isAnagram("rat", "car"))    