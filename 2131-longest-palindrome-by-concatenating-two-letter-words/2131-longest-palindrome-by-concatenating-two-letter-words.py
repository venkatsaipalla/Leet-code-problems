class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res=dict(Counter(words))
        keys=list(res.keys())
        values=list(res.values())
        print(keys,values)
        print(res)
        count=0
        flag=True
        for i in keys:
            if i[0]==i[1]:
                if res[i]%2!=0:
                    if flag:
                        count=count+res[i]
                        flag=False
                    else:
                        count=count+(res[i]-1)
                else:
                    count=count+res[i]
            else:
                if i[::-1] in keys:
                    count=count+ min(res[i],res[i[::-1]])
        return count*2    