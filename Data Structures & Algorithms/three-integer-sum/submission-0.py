from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ref = defaultdict(list)
        n = len(nums)
        for i in range(n):
            ref[nums[i]].append(i)
        
        sol = set()
        for i in range(n):
            for j in range(i+1, n):
                target = - (nums[i] + nums[j])
                for index in ref[target]:
                    if i != index and j != index:
                        sol.add( tuple(sorted(( nums[i], nums[j], nums[index]))))
                        
        sol = [ list(s) for s in sol]
        return sol