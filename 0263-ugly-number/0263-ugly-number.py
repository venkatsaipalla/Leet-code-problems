class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        l=[]
        def find(n):
            while n%2==0:
                if 2 not in l:
                    l.append(2)
                n=n/2
                
            
            for i in range(3,int(math.sqrt(n))+1,2):
                while n%i==0:
                    n=n/i
                    l.append(i)
            if n > 2:
                l.append(int(n))       
        find(n)
        l=list(set(l))
        print("l=",l)
        if len(l)>3:
            return False
        for i in l:
            if i not in [2,3,5]:
                return False
        return True    