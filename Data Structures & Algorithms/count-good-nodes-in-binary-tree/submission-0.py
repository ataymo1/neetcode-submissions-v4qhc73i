# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 1
        if root.left:
            total += self.dfs(root.left, root.val)
        if root.right:
            total += self.dfs(root.right, root.val)
        
        return total
    def dfs(self, node, high):
        added = 0
        if node.val >= high:
            high = node.val
            added += 1

        if node.left:
            added += self.dfs(node.left, high)
        
        if node.right:
            added += self.dfs(node.right, high)
        
        return added



        