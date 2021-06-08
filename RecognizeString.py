"""
author:AdarshChaurasia

"""


class Solution:
    
    def reorganizeString(self, s: str) -> str:
        d={}
        for char in s:
            if char in d:
                d[char]+=1
            else:
                d[char]=1
            
        max_heap=[]
        
        for char,fr in d.items():
            heappush(max_heap,(-fr,char))
            
            
        res=[]
        while len(max_heap)>1:
            f1,char=heappop(max_heap)
            f2,char1=heappop(max_heap)
            res.append(char)
            res.append(char1)
            f1+=1
            f2+=1
            if f1:
                heappush(max_heap,(f1,char))
            if f2:
                heappush(max_heap,(f2,char1))
                
        if len(max_heap)==1:
            f,c=heappop(max_heap)
            if -f==1:
                res.append(c)
                    
            else:
                return ""
        
                     
        return "".join(res)
            
