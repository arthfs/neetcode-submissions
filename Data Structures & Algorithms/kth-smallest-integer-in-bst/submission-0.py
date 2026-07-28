# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def count(root, cur):
    if root == None:
        return cur

    return 1+ count(root.left, cur) + count(root.right, cur)


def solve( root, cur):
    global found
    global sol
    
    if found:
        return 

    if root == None:
        return

    l = count(root.left, 0)
    if l+1  == cur:
        found = True
        sol =  root.val
        return

    elif l+1> cur:
        solve(root.left, cur )
    
    else :
        solve(root.right, cur - (l+1) )
    

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global found
        found = False

        global sol
        sol = -1

     
        solve(root, k)
        return sol