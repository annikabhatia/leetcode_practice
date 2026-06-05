# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        left = 0
        right = 0
        last = len(nums) - 1

        while right < last:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, i + nums[i])
            left = right+1
            right = farthest
            result += 1
        return result

# Example usage:
solution = Solution()
nums = [2, 3, 1, 1, 4]
result = solution.jump(nums)
print(result)  # Output: 2 (jump 1 step from index 0 to 1, then 3 steps to the last index)