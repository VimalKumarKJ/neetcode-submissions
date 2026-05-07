class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        result = 0
        left = 0

        for right in range(len(s)):
            while s[right] in subString:
                subString.remove(s[left])
                left+=1
            subString.add(s[right])
            result = max(result, right-left+1)
        return result