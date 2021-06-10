"""
	102. Binary Tree Level Order Traversal - Medium

	Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

	Input: root = [3,9,20,null,null,15,7]
	Output: [[3],[9,20],[15,7]]

	Input: root = [1]
	Output: [[1]]

	Input: root = []
	Output: []

	Runtime 28 ms - 95.02% of python 3 submissions
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        nodes = [root]
        node_vals = []
        next_lvl = []
        while nodes:
            for node in nodes:
                node_vals.append(node.val)
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            nodes = next_lvl
            result.append(node_vals)
            node_vals = []
            next_lvl = []
        return result


