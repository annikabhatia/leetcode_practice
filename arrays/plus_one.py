#https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=array

from typing import List

def plusOne(digits: List[int]) -> List[int]:
        full_integer=0
        final_digits_array = []
        
        #convert array to integer
        for i in range(len(digits)):
            full_integer += (digits[i]) * (10 ** (len(digits) - i - 1))
        #add 1 to end    
        full_integer+=1

        #convert back to list of ints
        final_digits_array = list(map(int, str(full_integer)))
        return final_digits_array