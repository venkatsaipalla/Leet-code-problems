class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0              # contains the reversed number
        for i in range(32):
            num = num << 1   # (1) shift left to have space for a new bit  
            bit = n % 2      # (2) get the rightmost bit of the input
            num += bit       # (3) add this bit to the output number 
			                 #     and it will be shifted leftwards later
            n = n >> 1       # (4) drop the rightmost bit of the input
        return num