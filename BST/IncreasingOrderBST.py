"""
	897. Increasing Order Search Tree Easy

    Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

    Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
    Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

    Input: root = [5,1,7]
    Output: [1,null,5,null,7]



	Runtime 36ms 21.93% of python3 submissions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lst = self.sortedListNodeVals(root, list())
        if len(lst) == 1:
            new_root = TreeNode(lst[0])
            return new_root
        pointer = TreeNode()
        new_root=TreeNode(lst[0])
        pointer.right = new_root
        new_tree = self.insertNodes(lst[1:], new_root)

        return pointer.right
    
    def sortedListNodeVals(self,root: TreeNode, lst):
        if not root:
            return
        
        lst.append(root.val)
        
        if root.left:
            lst = self.sortedListNodeVals(root.left, lst)
        if root.right:
            lst = self.sortedListNodeVals(root.right, lst)
        
        if lst:
            lst.sort()
            
        return lst
    
    def insertNodes(self, node_lst, cur_node):
        for data in node_lst:
            self._insertNode(data, cur_node)
                
            
    def _insertNode(self, node_val, node):
        if node_val > node.val:
            if node.right:
                self._insertNode(node_val, node.right)
            else:
                new_node = TreeNode(node_val)
                node.right = new_node
        