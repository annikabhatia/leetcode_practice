# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k+=1
                nums[k] = nums[i]   
        return k+1
    

# Example usage:
solution = Solution()       
nums = [1, 1, 2]
k = solution.removeDuplicates(nums)
print(k)  # Output: 2
print(nums[:k])  # Output: [1, 2]