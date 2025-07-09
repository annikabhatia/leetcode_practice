
from typing import List 
def moveZeroes(nums: List[int]) -> None:
        
        if len(nums) <= 1:
            return nums
        
        position = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[position]
                nums[position] = temp
                position+=1
        
        return nums

nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))