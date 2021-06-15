from collections import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        bfs=[]
        if not root:
            return 
        queue=deque([])
        queue.append(root)
        
        while queue:
            level=len(queue)
            curr=[]
            
            for i in range(level):
                current=queue.popleft()
                curr.append(current.val)
                
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                    
                
            bfs.append(curr)
            
            
            
            
            
            
        return bfs[-1][0]
