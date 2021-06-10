"""
	107. Binary Tree Level Order Traversal II Medium

	Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

	Input: root = [3,9,20,null,null,15,7]
	utput: [[15,7],[9,20],[3]]
	

	Input: root = [1]
	Output: [[1]]

	Input: root = []
	Output: []

	Runtime 32ms 82.23% of python3 submissions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        
        queue = deque([root])
        result = []
        lvl_nodes = []
        node_vals = []
        
        
        while queue:
            for i in range(len(queue)):
                cur_node = queue.popleft()
                node_vals.append(cur_node.val)
                
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            result.append(node_vals)
            node_vals = []
            lvl_nodes = []
        return result[::-1]