class Solution:
    def isSymmetric(self, root):
        def tree(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False

            return (a.val == b.val and
                    tree(a.left, b.right) and
                    tree(a.right, b.left))

        return tree(root.left, root.right)