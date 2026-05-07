class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = {}
        l1 = 0
        for char in s1:
            f1[char] = f1.get(char, 0) + 1
        l1 = len(f1)
        for i in range(len(s2)):
            f2, l2 = {}, 0
            for j in range(i, len(s2)):
                f2[s2[j]] = f2.get(s2[j], 0) + 1
                if f1.get(s2[j], 0) < f2.get(s2[j]):
                    break
                if f1.get(s2[j]) == f2.get(s2[j]):
                    l2 += 1
                if l1 == l2:
                    return True
        return False
            

