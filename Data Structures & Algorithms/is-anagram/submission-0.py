from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n!= m :
            return False

        ref1, ref2 = Counter(s), Counter(t)
        items = ref1.items()
        for i in ref1.items():
            if i[1] != ref2[i[0]]:
                return False
        return True
        