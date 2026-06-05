# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #this is more optimized **reversal** -- time complexity: O(n) , space complexity: O(1)

        n = len(nums)
        k = k % n #so if k is larger than n, it wraps it around! ex) rotating [1, 2, 3] by 5 is the same as rotating by 2

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, n-1) #reverse the entire array
        reverse(0, k-1) #reverse just the first k elements
        reverse(k, n-1) #reverse the remaining elements

# Example usage:
solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution.rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]