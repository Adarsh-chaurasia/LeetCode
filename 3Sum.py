class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        output=set()
        for i in range(0,len(nums)-1):
            start=i+1
            end=len(nums)-1
            x=nums[i]
            while start<end:
                if x+nums[start]+nums[end]==0:
                    output.add((nums[i],nums[start],nums[end]))
                    start+=1
                    end-=1
                    
                elif x+nums[start]+nums[end]<0:
                    start+=1
                    
                else:
                    end-=1
                    
                    
                
        return list(output)
