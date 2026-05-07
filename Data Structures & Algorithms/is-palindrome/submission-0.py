class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_spaces = ''.join([char for char in s if char.isalnum()]).lower()
        return no_spaces == no_spaces[::-1]
        