# https://leetcode.com/problems/length-of-last-word/

#this code doesnt pass case two, so still need to tweak
def lengthOfLastWord(s: str) -> int:
        length = 0
        for char in s:
            if char == ' ':
                length = 0
            else:
                length+=1
        return length

s = "Hello World"
print(lengthOfLastWord(s))