# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        k = 0
        for n in range(len(nums)):
            if nums[n] != val:
                nums[k] = nums[n]
                k+=1
        return k
        
# Example usage:
solution = Solution()
nums = [3, 2, 2, 3]
val = 3
k = solution.removeElement(nums, val)
print(k)  # Output: 2