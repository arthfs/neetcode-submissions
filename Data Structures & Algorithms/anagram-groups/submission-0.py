from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = []
        ref = defaultdict(list)
        sol = []
        for s in strs:
            ref[''.join(sorted(s))].append(s)
      
        return list(ref.values())