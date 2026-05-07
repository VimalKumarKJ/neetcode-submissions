class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + "!" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while (i < len(s)):
            j = i
            while(s[j] != "!"):
                j += 1
            getLength = int(s[i:j])
            i = j + 1
            j = i + getLength
            decoded.append(s[i:j])
            i = j
        return decoded
            