# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if k < 2 or nums[i] != nums[k - 2]:
                nums[k] = nums[i]   
                k+=1
        return k
    
# Example usage:
solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = solution.removeDuplicates(nums)     
print(k)  # Output: 5
print(nums[:k])  # Output: [1, 1, 2, 2, 3]