def isValid(s: str) -> bool:
        
        #format for dict --> key:val
        dictionary = {')':'(', '}':'{', ']':'['}
        stack = []

        for i in s:
            if i in dictionary.values():
                #add OPENING brackets to the stack
                stack.append(i)
            elif i in dictionary:
                #if the stack is empty, this means there's no matching opening bracket.
                #or, we pop the top of the stack and check if it matches the expected opening bracket
                if not stack or stack.pop() != dictionary[i]:
                    return False
        #returns true if all of the open/closed brackets matched up
        return len(stack) == 0