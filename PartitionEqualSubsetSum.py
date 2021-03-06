def subsetSum(arr,sum,N):
    dp=[[False for i in range(sum + 1)]for i in range(N + 1)]
    for i in range(N+1):
        dp[i][0]=True
            
    for j in range(1,sum+1):
        dp[0][j]=False
                    
                    
    for i in range(1,N+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
                    
            else:
                dp[i][j]=dp[i-1][j]
            
    return dp[N][sum]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ =sum(nums)
        n=len(nums)
        
        if sum_ & 1:
            return False
        
        else:
            x=subsetSum(nums,sum_//2,n)
            return x
