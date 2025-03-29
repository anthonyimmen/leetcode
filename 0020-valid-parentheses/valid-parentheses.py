class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack, push opening, pop closing
        stack = []
        openers = {"(": ")", "{": "}", "[": "]"}
        closers = {")": "(", "}": "{", "]": "["}

        for i in range(len(s)):
            if s[i] in openers:
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            elif closers[s[i]] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
            