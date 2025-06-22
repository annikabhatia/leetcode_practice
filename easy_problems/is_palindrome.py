# https://leetcode.com/problems/palindrome-number/description/

def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        #starting at the end of the string, going backwards (step = -1)
        return x_string == x_string[::-1]