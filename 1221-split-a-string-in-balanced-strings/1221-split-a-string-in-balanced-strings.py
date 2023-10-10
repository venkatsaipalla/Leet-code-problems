class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # n=len(s)
        # r_count=0
        # l_count=0
        # count=0
        # for i in s:
        #     if(r_count==l_count):
        #         count+=1
        #         l_count=0
        #         r_count=0
        #     if i=="R":
        #         r_count+=1
        #     else:
        #         l_count+=1
        # return count 
        count = 0
        balance = 0
        for i in range(len(s)):
            if s[i] == 'R':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count
                