class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i, j = 0,2
        counter = 0
        while j < len(s):
            if len(set(s[i:j+1])) == 3:
                counter +=1
            i+=1
            j+=1  
        return counter