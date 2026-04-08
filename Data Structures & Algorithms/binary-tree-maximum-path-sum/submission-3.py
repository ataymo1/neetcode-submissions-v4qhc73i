# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(self.branchPath(root))
    
    def branchPath(self, node) -> tuple(best_branch, best_path):
        if not node:
            return 0, 0

        if not node.left and not node.right:
            return node.val, node.val
        
        elif not node.left:
            right_branch, path = self.branchPath(node.right)
            return max(node.val, right_branch + node.val), max(right_branch, right_branch + node.val, node.val)
       
        elif not node.right:
            left_branch, path = self.branchPath(node.left)
            check = tuple((left_branch + node.val, max(left_branch, left_branch + node.val)))
            return max(node.val, left_branch + node.val), max(left_branch, left_branch + node.val, node.val)
       
        else:
            left_branch, path1 = self.branchPath(node.left)
            right_branch, path2 = self.branchPath(node.right)

            best_branch = max(left_branch + node.val, right_branch + node.val, node.val)
            best_path = max(path1, path2, left_branch + right_branch + node.val, node.val)

            return best_branch, best_path


        