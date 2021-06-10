"""
	104. Maximum Depth of Binary Tree - Easy

	Given the root of a binary tree, return its maximum depth.

	A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

	Input: root = [3,9,20,null,null,15,7]
	Output: 3

	Input: root = [1,null,2]
	Output: 2

	Input: root = []
	Output: 0
	
	Input: root = [0]
	Output: 1

Runtime 28 ms. 83.22% of python submissions
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        return 1 + max(lh, rh)
