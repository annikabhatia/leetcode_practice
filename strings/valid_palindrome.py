def isPalindrome(s: str) -> bool:
        new_string = ""
        for char in s:
            #non-alphanumeric characters (space, punctuation)
            if char.isalnum():
                new_string += char
        new_string = new_string.lower()       

        #can't just use reversed since it will return reversed iterator, not a string
        #''.join takes list of strings and joins them into one string
        if ''.join(reversed(new_string)) == new_string:
            return True
        else:
            return False