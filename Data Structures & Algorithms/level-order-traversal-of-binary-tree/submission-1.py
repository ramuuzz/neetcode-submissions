# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        ans=deque([root])
        level=[]
        
        while ans:
           
            curr=[]
            
            for _ in range(len(ans)):
                
                a=ans.popleft()
                curr.append(a.val)
                if a.left:
                    ans.append(a.left)

                if a.right:
                    ans.append(a.right)
            
            level.append(curr)
        return level


        
        