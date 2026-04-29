class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0]* (n)
        dp[0] = nums[0]
        if dp[0] > n-1:
            dp[0] = n-1
            
        last = dp[0] if dp[0] >0 else 0
        for i in range(1, n):
            if last >= i:
                dp[i] = max( [dp[last], i + nums[i] ])
                if dp[i] > n-1:
                    dp[i] = n-1

            last = max([dp[i], last])
   
        return dp[-1] >= n-1