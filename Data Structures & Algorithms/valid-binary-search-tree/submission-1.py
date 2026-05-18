# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSmaller(root, val):
    if root == None: 
        return True
    return root.val < val and isSmaller(root.left, val) and isSmaller(root.right, val)

def isBigger(root, val):
    if root == None: 
        return True
    return root.val > val and isBigger(root.left, val) and isBigger(root.right, val)


def solve(root):
    if root.left == None and root.right == None:
        return True
    
    if root.left == None:
        return root.val < root.right.val and solve(root.right) and isBigger(root.right, root.val)
    
    if root.right == None:
        return root.val > root.left.val and solve(root.left) and isSmaller(root.left, root.val)

    return root.val > root.left.val and root.val < root.right.val and solve(root.left) and solve(root.right) and isSmaller(root.left, root.val) and isBigger(root.right, root.val)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return solve(root)