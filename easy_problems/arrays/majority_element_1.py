#https://leetcode.com/problems/majority-element/description/?envType=problem-list-v2&envId=array

#this is one way using a sort method

from typing import List

def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n // 2]