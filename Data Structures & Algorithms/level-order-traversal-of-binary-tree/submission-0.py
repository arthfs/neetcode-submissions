# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
            
        ref = [root]
        sol = []
        while ref!= []:
            temp = []
            for i in range(len(ref)):
                c = ref.pop(0)
                temp.append(c.val)
                if c.left!= None:
                    ref.append(c.left)
                
                if c.right!= None:
                    ref.append(c.right)
            sol.append(temp.copy())
        return sol