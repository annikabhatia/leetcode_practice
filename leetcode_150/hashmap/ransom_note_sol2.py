# has better runtime

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        final = {}

        # dictionary.get() --> retrieve a value by key for a dictionary
        
        for char in magazine:
            #if a char already exists in dictionary, increment the count
            #if NOT, start from 0 and add 1
            final[char] = final.get(char, 0) + 1   
        for char in ransomNote:
            #if an element in ransomNote is not in magazine, then immediately return False
            if final.get(char, 0) == 0:
                return False
            #decrement the available count for that char in magazine
            final[char] -= 1
        #if all conditions are satisfied, then return True
        return True