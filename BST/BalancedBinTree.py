"""
	110. Balanced Binary Tree Easy

	Given a binary tree, determine if it is height-balanced.

	For this problem, a height-balanced binary tree is defined as:
	a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

	Input: root = [3,9,20,null,null,15,7]
	utput: [[15,7],[9,20],[3]]
	

	Input: root = [1]
	Output: [[1]]

	Input: root = []
	Output: []

	Runtime 56ms 48.59% of python3 submissions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self._isBalanced(root)
    
    def _isBalanced(self, cur_node):
        if not cur_node:
            return True
        return abs(self.branchHeight(cur_node.left) - self.branchHeight(cur_node.right)) <= 1 and self._isBalanced(cur_node.left) and self._isBalanced(cur_node.right)
    
    def branchHeight(self, cur_node):
        if not cur_node:
            return -1
        l_height = self.branchHeight(cur_node.left)
        r_height = self.branchHeight(cur_node.right)
        return 1 + max(l_height, r_height)
        