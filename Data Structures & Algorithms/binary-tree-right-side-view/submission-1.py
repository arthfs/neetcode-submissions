# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        if root == None:
            return []

        ref = [root]
        while ref!= []:
            last = None
            for i in range(len(ref)):
                c = ref.pop(0)
                last = c.val
                if c.left:
                    ref.append(c.left)
                if c.right:
                    ref.append(c.right)
            sol.append(last)

        return sol