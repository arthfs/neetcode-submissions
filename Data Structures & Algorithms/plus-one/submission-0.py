class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for i in range(n-1, -1, -1):
            result = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            digits[i] = result
        
        if carry > 0 :
            digits.insert(0, carry)
        return digits