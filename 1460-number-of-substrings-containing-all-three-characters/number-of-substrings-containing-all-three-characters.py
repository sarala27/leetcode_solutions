class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq=[0]*3
        left=0
        ans=0
        n=len(s)
        for right in range(n):
            freq[ord(s[right])-ord('a')]+=1
            while freq[0] > 0 and freq[1]>0 and freq[2]>0:
                ans+=n-right
                freq[ord(s[left])-ord('a')]-=1
                left+=1
        return ans
        