class Solution:
    def isPalindrome(self, s: str) -> bool:
        tempStr = s.lower()
        cleanedStr = ''.join(char for char in tempStr if char.isalnum())
        newStr = cleanedStr[::-1]

        if(newStr == cleanedStr):
            return True
        return False
        