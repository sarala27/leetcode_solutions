class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix=[0]
        sprefix=[0]
        size=[0]
        sm=0
        num=0
        st=0
        for i in range(len(s)):
            if s[i]!="0":
                st+=1
                sm+=int(s[i])
                sm=sm%(10**9+7)
                num*=(10)
                num+=int(s[i])
            prefix.append(sm)
            size.append(st)
            num%=(10**9+7)
            sprefix.append(num)
        ans=[]
        for i,j in queries:
            sm=prefix[j+1]-prefix[i]
            tmp=size[j+1]-size[i]
            tm=sprefix[j+1]-(sprefix[i]*pow(10,tmp,(10**9+7)))
            ans.append(tm*sm%(10**9+7))
        return (ans)
        