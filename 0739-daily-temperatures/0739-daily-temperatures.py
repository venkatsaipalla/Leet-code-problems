class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1): 
            while len(stk)>0 and temperatures[stk[-1]]<=temperatures[i]:
                stk.pop()
            if len(stk)>0 and temperatures[stk[-1]]>temperatures[i]:
                res[i]=stk[-1]-i
            stk.append(i) 
            for k in stk:
                print(temperatures[k],end=" ")
            print("new")    
        return res