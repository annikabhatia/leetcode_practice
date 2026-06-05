# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0
        last = len(nums) - 1 #this is our goal, we want to reach here

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= last: #if at any point farthest has reached or passed the last index, no need to keep looping, return True early
                return True
        return True
            
# Example usage:
solution = Solution()
nums = [2, 3, 1, 1, 4]
result = solution.canJump(nums)
print(result)  # Output: True (jump 1 step from index 0 to 1, then 3 steps to the last index)
