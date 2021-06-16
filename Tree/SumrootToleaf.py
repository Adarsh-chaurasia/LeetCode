# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def solve(root,path):
    if not root:
        return 0

    path=path*10+root.val
        
    if not root.left and not root.right:
        return path
    
    return     solve(root.left,path)+solve(root.right,path)

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return solve(root,0)
        
        
