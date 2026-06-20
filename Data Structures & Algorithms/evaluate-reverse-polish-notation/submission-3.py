class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens)==1:
            return int(tokens[0])

        def doOperation(num1, num2, token):
            if token=='+':
                return num1+num2
            elif token=='-':
                return num1-num2
            elif token=='*':
                return num1*num2
            elif token=='/':
                return int(num1/num2)


        symbols = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            # print(stack)
            if token in symbols and len(stack)>=2:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                result = doOperation(num1, num2, token)
                stack.append(result)
            else:
                stack.append(token)
        
        print(stack)
        return stack[-1]
        


        