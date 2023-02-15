class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        carry = 0
        i = len(num) - 1
        while i >= 0 or k > 0:
            digit = k % 10 if k > 0 else 0
            k //= 10
            if i >= 0:
                digit += num[i]
                i -= 1
            digit += carry
            carry = digit // 10
            digit %= 10
            result.append(digit)
        if carry > 0:
            result.append(carry)
        return result[::-1]

        