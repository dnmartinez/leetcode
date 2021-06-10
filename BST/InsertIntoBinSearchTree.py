"""
	701. Insert into a Binary Search Tree Medium

	You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

	Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

	Input: root = [4,2,7,1,3], val = 5
	Output: [4,2,7,1,3,5]

	Input: root = [40,20,60,10,30,50,70], val = 25
	Output: [40,20,60,10,30,50,70,null,null,25]

	Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
	Output: [4,2,7,1,3,5]


	Runtime 136ms 61.81% of python3 submissions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        else:
            self._insert(root, val)
        return root
    
    def _insert(self, cur_node, val):
        if val < cur_node.val:
            if cur_node.left:
                self._insert(cur_node.left, val)
            else:
                cur_node.left = TreeNode(val)
                print(cur_node)
        elif val > cur_node.val:
            if cur_node.right:
                self._insert(cur_node.right, val)
            else:
                cur_node.right = TreeNode(val)
                