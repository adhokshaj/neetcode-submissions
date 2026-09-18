class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {'(':')', '{':'}', '[':']'}

        n = len(s)
        for i in range(n-1,-1,-1):
            c = s[i]
            if c not in map:
                stack.append(c)
            else:
                if stack and stack[-1] != map[c]:
                    return False
                elif stack and stack[-1]==map[c]:
                    stack.pop()
                else:
                    return False
            # print(stack)
        return not stack


        