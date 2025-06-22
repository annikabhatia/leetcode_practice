# https://leetcode.com/problems/remove-element/  

from typing import List

def removeElement(nums: List[int], val: int) -> int:
        expectedNums = []
        for number in nums:
            if number == val:
                continue
            else:
                expectedNums.append(number)
        return len(expectedNums)

nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))