#https://leetcode.com/problems/search-insert-position/

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    for number in nums:
        if number == target:
            return nums.index(number)
        elif number > target:
            return nums.index(number)
    return len(nums)
    

nums = [1,3,5,6]
print(searchInsert(nums, 5))