class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap={}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1
                
        result=0
        for i,j in hashmap.items():
            if j==1:
                result+=i
                
            else:
                continue
                
        return result
