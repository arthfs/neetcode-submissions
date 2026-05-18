from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ref = defaultdict(int)
        for i in nums:
            if ref[i]!= 0:
                return True
            ref[i]+= 1
        return False