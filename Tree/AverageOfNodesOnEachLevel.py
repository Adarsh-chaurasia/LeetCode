from collections import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        average=[]
        if not root :
            return 0
        
        queue=deque([])
        queue.append(root)
        
        while queue:
            level=len(queue)
            sum_=0
            for i in range(level):
                current=queue.popleft()
                sum_+=current.val
                
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                    
            avg=sum_/level
            
            average.append(avg)
            
        return average
