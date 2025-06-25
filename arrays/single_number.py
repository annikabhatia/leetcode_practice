#https://leetcode.com/problems/single-number/description/?envType=problem-list-v2&envId=array

from typing import List

def singleNumber(self, nums: List[int]) -> int:
        
        tracker = 0
        for i in range(len(nums)):
            #xor property
            tracker ^= nums[i]
        return tracker