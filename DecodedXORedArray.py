class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output=[]
        output.append(first)
        for i in range(len(encoded)):
            x=output[i]^encoded[i]
            output.append(x)
            
            
        return output 
