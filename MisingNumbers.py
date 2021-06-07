min_heap=[]
n=len(nums)
for k in range(n):
    heappush(min_heap,-nums[k])

           
i=n
while min_heap:
  x=heappop(min_heap)
 if i==-x:
  i-=1
  continue
 else:
  return i
return 0
        
  """this takes O(NlogN) times to create a heap""""
  
  
  
  def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+1)//2)-sum(nums)
      
  """this takes a O(N) times to sumup array"""
