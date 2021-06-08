class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(arr)
        rank=1
        d={}
        for i in s:
            if i not in d:
                d[i]=rank
                rank+=1
        j=0
        for i in arr:
            arr[j]=d[i]
            j+=1
        return arr
