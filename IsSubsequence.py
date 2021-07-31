def lcs(a,b):
    n=len(a)
    m=len(b)
    dp=[[0 for i in range(m+1)]for j in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (a[i-1]==b[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
                
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                
                
    return dp[n][m]


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m,n=len(s),len(t)
        
        result=lcs(s,t)
        
        if result==m:
            return True
        
        else:
            return False