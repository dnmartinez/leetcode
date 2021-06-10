"""
	112. Path Sum Easy

	Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

	A leaf is a node with no children.

	Note: A leaf is a node with no children.

	Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
	Output: true

	Input: root = [1,2,3], targetSum = 5
	Output: false

	Input: root = [1,2], targetSum = 0
	Output: false

	Runtime 40ms 81.47% of python3 submissions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        if (not root.left and not root.right) and sum == root.val:
            return True
        
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        
    
    def isLeaf(self, root: TreeNode) -> bool:
        return not root.left and not root.right
