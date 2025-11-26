class Solution:
    def isPalindrome(self, x: int) -> bool:
        revNum = 0
        copy = x

        while(x>0):
            extractedNum = x % 10
            x = int(x/10)
            revNum = (revNum * 10) + extractedNum            
        
        if revNum == copy:
            return True
        else: 
            return False