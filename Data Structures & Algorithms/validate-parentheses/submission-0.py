class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')':'(',
            '}':"{",
            ']':'['
        }
        stack =[]
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                while not stack or stack[-1] != map[ch]:
                    return False
                stack.pop()
        return len(stack)==0