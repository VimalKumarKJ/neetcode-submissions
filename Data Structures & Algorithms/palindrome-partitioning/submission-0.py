class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_valid(sub_str):
            l = 0
            r = len(sub_str) - 1

            while(l<r):
                if sub_str[l] != sub_str[r]:
                    return False
                
                l+=1
                r-=1
            return True
        
        def backtrack(start):
            if start == len(s):
                res.append(path.copy())
                return
            
            for end in range(start, len(s)):
                sub_str = s[start:end+1]

                if is_valid(sub_str):
                    path.append(sub_str)
                    backtrack(end+1)
                    path.pop()
        backtrack(0)
        return res