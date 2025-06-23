# https://leetcode.com/problems/length-of-last-word/

#this code doesnt pass case two, so still need to tweak
def lengthOfLastWord(s: str) -> int:
        length = 0
        trimmed_string = s.rstrip()
        for char in trimmed_string:
            if char == ' ':
                length=0
                continue
            else:
                length+=1
        return length

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))