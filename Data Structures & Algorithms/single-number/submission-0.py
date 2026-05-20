from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for i in counter.items():
            if i[1] == 1:
                return i[0]