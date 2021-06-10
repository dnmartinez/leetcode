"""
	1008. Construct Binary Search Tree from Preorder Traversal Medium

	Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

	It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

	A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

	A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

	Input: preorder = [8,5,1,7,10,12]
	Output: [8,5,10,1,7,null,12]

	Input: preorder = [1,3]
	Output: [1,null,3]


	Runtime 24ms 99.62% of python3 submissions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return preorder
        
        # Get frist num of the list and create a TreeNode. The very first number will be the root of the tree
        root = TreeNode(preorder[0])
        # Create a stack and add the root to it. We will have a stack of TreeNodes and pointers that will have
        # a reference to their left and right children
        stack = [root]
        
        for i in range(1, len(preorder)):
            # Add elements to the left of the tree
            if preorder[i] < stack[-1].val:
                # Create a new TreeNode. Set the left of the last element of the stack to the new node.
                # Append the new TreeNode to the stack. So the stack will not only have the previous element with 
                # its left pointing to the new node, but also the new node will be added to the stack 
                # with lt and rt = None
                stack[-1].left = TreeNode(preorder[i])
                stack.append(stack[-1].left)
            # Add elements to the right of the tree
            else:
                while stack and preorder[i] > stack[-1].val:
                    # Keep popping TreeNodes to get the correct node to which we will set its right to the current node
                    last_node = stack.pop()
                last_node.right = TreeNode(preorder[i])
                stack.append(last_node.right)
                
        return root
        