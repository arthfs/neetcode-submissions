from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = defaultdict(list)
        n = len(nums)
        for i in range(n):
            index = ref.get(target - nums[i]) 
            if index != None:
                return sorted( [i, index[0] ])
            ref[nums[i]].append(i)