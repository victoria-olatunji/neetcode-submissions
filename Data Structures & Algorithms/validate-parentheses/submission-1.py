class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cto = { ')' : '(', ']': '[', '}':'{'}
        for p in s:
            if p in cto:
                if stack and stack[-1] == cto[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False
        