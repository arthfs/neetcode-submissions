# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root, path):
    global sol
    if root == None:
        return

    if path!= []:
        if root.val >= max(path):
            sol+=1

    path.append(root.val)
    dfs(root.left, path)
    dfs(root.right, path)
        
    path.pop()

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global sol
        sol = 1
        dfs(root, [])
        return sol