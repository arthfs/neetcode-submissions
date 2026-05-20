class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = int( (i+j)/2)
            if nums[m] == target:
                return m

            if nums[m] > target:
                j = m - 1

            if nums[m] < target:
                i = m + 1
        return -1