#https://leetcode.com/problems/majority-element/description/?envType=problem-list-v2&envId=array

#this is another way, using the Moore Voting Algorithm

from typing import List

def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_element = 0
        tracker = 0
        for i in range(n):
            if tracker == 0:
                majority_element = nums[i]
            if nums[i] == majority_element:
                tracker+=1
            else:
                tracker-=1
        return majority_element