class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        for char in s:
            if stack and char in mapping and stack[-1] != mapping[char]:
                return False
            elif stack and char in mapping and stack[-1] == mapping[char]:
                stack.pop()
                continue
            stack.append(char)
        # print(stack)
        return not stack
            
            
        