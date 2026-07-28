class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l,r = 0, 0 

        i = 0
        sol = 0
        ref = dict()
        while i < n:
            
            if ref.get(s[i], False) == False:
                ref[s[i]] = True

            else:
                while s[l] != s[i]:
                    ref[s[l]] = False
                    l+=1
                
                l+=1
            sol = max([sol, i-l+1])
            
            i+=1
        return sol