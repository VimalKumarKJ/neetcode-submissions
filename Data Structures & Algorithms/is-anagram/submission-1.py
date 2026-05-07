class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkS = {}
        checkT = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            checkS[char] = checkS.get(char, 0) + 1
        
        for char in t:
            checkT[char] = checkT.get(char, 0) + 1

        return checkS == checkT
        