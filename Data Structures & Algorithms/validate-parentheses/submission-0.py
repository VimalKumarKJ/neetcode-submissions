class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for i in s:
            if i in hashmap:
                top = stack.pop() if stack else '!'
                if top != hashmap[i]:
                    return False
            else:
                stack.append(i)
        return not stack