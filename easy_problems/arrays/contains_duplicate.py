
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
        #empty hash set to store elements
        seen = set()
        for num in nums:
            #if the element is already in the hash set
            if num in seen:
                return True
            #otherwise, add the element to the hash set
            seen.add(num)
        return False

nums = [1, 2, 3, 4]
print(containsDuplicate(nums))