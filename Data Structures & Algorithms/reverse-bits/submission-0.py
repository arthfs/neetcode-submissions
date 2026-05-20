class Solution:
    def reverseBits(self, n: int) -> int:
        sol = 0
        s = bin(n)[2:]
        cur_length = len(s)
        for i in range(32- cur_length):
            s = '0' + s
 
        length = len(s)
        for i in range(length - 1, -1, -1):
            sol+= int(s[i]) * (2 ** i)
        return sol