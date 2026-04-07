# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if self.isLeafNode(root, target):
            return None
        return root

    def isLeafNode(self, root, target):
        if not root:
            return False
        
        if not root.right and not root.left and target == root.val:
            return True
        
        if self.isLeafNode(root.right, target):
            root.right = None

        if self.isLeafNode(root.left, target):
            root.left = None

        print(f"stayed: {root.val}")
        if not root.right and not root.left and target == root.val:
            print(f"here: {root.val}")
            return True
        else:
            print(f"here again: {root.val}")
            return False

        

