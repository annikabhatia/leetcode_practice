# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150 

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        ransomNote = list(ransomNote)

        # make ransomeNote a list, then if ransomNote and magazine have a matching letter, subtract that letter from ransomeNote
        # return not magazine, so if it is empty then its true and if not false

        for char in magazine:
            if char in ransomNote:
                ransomNote.remove(char)

        return not ransomNote