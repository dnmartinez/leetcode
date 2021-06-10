"""
	965. Univalued Binary Tree

    A binary tree is univalued if every node in the tree has the same value.
    Return true if and only if the given tree is univalued.

    Input: [1,1,1,1,1,null,1]
    Output: true

    Input: [2,2,2,5,2]
    Output: false

	Runtime 32ms 61.69% of python3 submissions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # Idea: Maybe use a list or a dictionary and check that lenght == 1
        # or keep a variable with the root value. If I see a number that is different thatn 
        # the root value, then return false
       
        
        if not root:
            return True
        
        if root.left and (root.val != root.left.val):
            return False
        
        if root.right and (root.val != root.right.val):
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)