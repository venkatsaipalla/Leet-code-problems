class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        l1=list(map(int,list(str(N))))
        l1.sort()
        num=1
        for i in range(31):
            #print(sorted(list(map(int,list(str(num))))))
            if l1==sorted(list(map(int,list(str(num))))):
                return True
            num=num<<1
        return False
