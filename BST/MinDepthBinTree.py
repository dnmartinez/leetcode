"""
	111. Minimum Depth of Binary Tree Easy

	Given a binary tree, find its minimum depth.

	The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

	Note: A leaf is a node with no children.

	Input: root = [3,9,20,null,null,15,7]
	Output: 2

	Input: root = [2,null,3,null,4,null,5,null,6]
	Output: 5

	Runtime 464ms 95.69% of python3 submissions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if self.isLeaf(root):
            return 1
        dq = deque()
        dq.append(root)
        level = 1
        
        while dq:
            tot_nodes = len(dq)
            
            for i in range(tot_nodes):
                node = dq.popleft()
                if self.isLeaf(node):
                    return level
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)                    
            level += 1
        return level    
            
        
    def isLeaf(self, node: TreeNode) -> bool:
        return not node.left and not node.right
