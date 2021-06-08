class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        
        d={}
        for each in sentence:
            if each in d:
                d[each]+=1
            else:
                d[each]=1
        char=list(d.keys())
        if len(char) ==26:
            return True
        else:
            return False
       
