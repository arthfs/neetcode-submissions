class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if nums.count(0) == 1:
            ref = [0] * n
            leftPart = 1 
            rightPart = 1
            targetIndex = nums.index(0)
            for i in range(targetIndex):
                leftPart*= nums[i]

            for i in range(targetIndex+1, n):
                rightPart*= nums[i]

            ref[targetIndex] = leftPart * rightPart
            return ref

        ref = [nums.pop(0)]
        for i in nums:
            ref.append(i * ref[-1] )
        
        sol = [0] * n
        for i in range(n):
            if i == 0 and ref[0]!= 0:
                sol[i] = ref[-1] // ref[0]
            elif i == n-1:
                sol [i] = ref[i-1]
            else:
                if ref[i] != 0:
                    sol[i] = ref[i-1] * (ref[-1] // ref[i])
        return sol 