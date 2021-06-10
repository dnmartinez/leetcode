"""
	1469. Find All The Lonely Nodes - Easy
	In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.

	Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.

	Input: root = [1,2,3,null,4]
	Output: [4]
	Explanation: Light blue node is the only lonely node.
	Node 1 is the root and is not lonely.
	Nodes 2 and 3 have the same parent and are not lonely.

	Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
	Output: [6,2]
	Explanation: Light blue nodes are lonely nodes.
	Please remember that order doesn't matter, [2,6] is also an acceptable answer.

	Runtime 56 ms. 50.76% of python submissions
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        def recursiveLeaf(root, lst):
            if not root:
                return
            if root.left and not root.right:
                next_node = root.left
                lst.append(next_node.val)
            if root.right and not root.left:
                next_node = root.right
                lst.append(next_node.val)
            if root.left:
                recursiveLeaf(root.left, lst)
            if root.right:
                recursiveLeaf(root.right, lst)
            return lst
        return recursiveLeaf(root, [])