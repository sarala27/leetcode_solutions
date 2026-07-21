from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d=Counter(nums)
        result=[]
        for num,freq in d.items():
            if(freq>n//3):
                result.append(num)
        return result

        