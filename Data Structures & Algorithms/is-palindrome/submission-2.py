import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ref = string.ascii_letters+ string.digits
        n = len(s)
        i , j = 0, n-1
        while i < j:
            
            while i < j and s[i] not in ref:
                i+= 1

            while j > i and s[j] not in ref:
                j-= 1

            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1

   
        return True
          