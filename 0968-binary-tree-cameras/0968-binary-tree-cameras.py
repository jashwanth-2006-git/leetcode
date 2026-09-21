# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        ans = [0]

        def cam(n):
            if not n: 
                return 2

            l = cam(n.left) 
            r = cam(n.right)
            
            if 0 in (l, r):
                ans[0] += 1
                return 1

            if 1 in (l, r):
                return 2 
            else:
                return 0

        if cam(root) == 0: 
            ans[0] += 1
        return ans[0]
        