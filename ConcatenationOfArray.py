class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        ans=[0]*n
        
        for i in range(n):
            ans[i]=nums[i]
            
        for i in range(n):
            ans.append(nums[i])
        
        
        
        
        return ans
      
      
      
      
      
      
      
      class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        
        ans=nums
        ans.extend(nums)
        
        
        return ans
