# https://leetcode.com/problems/remove-element/  

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    #in place algorithm
    k = 0
    for number in range(len(nums)):
        if nums[number] == val:
            continue
        else:
            # first k elements of nums contain the elements which are not equal to val
            nums[k] = nums[number]
            k+=1
    return k

nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))