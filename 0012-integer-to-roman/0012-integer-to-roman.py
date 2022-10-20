class Solution:
    def intToRoman(self, num: int) -> str:
        keys=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        val=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        print(keys,val)
        result=""
        def near(n):
            i=12
            while n<val[i]:
                i=i-1
                if i<0:
                    return 0
            return i
        while num>0:
            k=near(num)
            result=result+keys[k]
            num=num-val[k]
        return result
            