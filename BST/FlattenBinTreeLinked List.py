"""
	270. Closest Binary Search Tree Value Easy

	Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

	Input: root = [4,2,5,1,3], target = 3.714286
	Output: 4

	Input: root = [1], target = 4.428571
	Output: 1


	Runtime 48ms 75.94% of python3 submissions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorderTraversal(node: TreeNode):
            if not node:
                return []
            return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)
        return 
        	min(inorderTraversal(root), key = lambda node: abs(target - node))
    
