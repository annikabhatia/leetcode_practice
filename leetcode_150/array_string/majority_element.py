# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #iterate through the array and make a count, return highest count

        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1 #get is what looks up num in the dictionary; will return the current count or 0 if its not there. then adds 1 and saves it back
            if counts[num] > len(nums) // 2: #the majority threshold
                return num
# Example usage:
solution = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
result = solution.majorityElement(nums)
print(result)  # Output: 2  
