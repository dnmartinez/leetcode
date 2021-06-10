"""
	Given the root of a binary tree, return the inorder traversal of its nodes' values.
	Input: root = [1,null,2,3]
	Output: [1,3,2]


	Input: root = []
	Output: []

	Input: root = [1]
	Output: [1]

	Input: root = [1,null,2]
	Output: [1,2]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def recursiveInorder(node, lst):
            if node:
                lst = recursiveInorder(node.left, lst)
                lst.append(node.val)
                lst = recursiveInorder(node.right, lst)
            return lst
        return recursiveInorder(root, [])
            