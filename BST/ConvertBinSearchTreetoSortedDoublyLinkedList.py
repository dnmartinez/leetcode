"""
	426. Convert Binary Search Tree to Sorted Doubly Linked List Medium

	Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

	You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

	We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

	Input: root = [4,2,5,1,3]
	Output: [1,2,3,4,5]
	Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

	Input: root = [2,1,3]
	Output: [1,2,3]

	Input: root = []
	Output: []
	Explanation: Input is an empty tree. Output is also an empty Linked List.

	Input: root = [1]
	Output: [1]


	Runtime 36ms 62.81% of python3 submissions
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        lst = self.nodeVals(root, [])
        lst.sort()
        node = self.makeList(lst) # node is the beginning or "head" of the list

        return node
    
    """
        Traverses a list of ints and returns a circular, doubly linked list 
    """
    def makeList(self, lst):
        new_node = Node(lst[0]) # get first val from list and turn it into a node
        head = tail = new_node # head and tail to keep track of beginning and end of list
        
        for i in lst[1:]:
            new_node = Node(i)
            tail.right, new_node.left = new_node, tail
            tail = new_node
        tail.right, head.left = head, tail # Make CLL by pointing head and tail to each other 

        return head
           
    """
        Traverses the tree and returns a list of ints
    """
    def nodeVals(self, root, lst):
        if root:
            lst.append(root.val)
        # Needs following two if statements. Without them the program crashes because
        # it will not know what to do if the left or right of a node is None.
        # So if the left/right exists then keep going down the tree
        if root.left:
            lst = self.nodeVals(root.left, lst)
        if root.right:
            lst = self.nodeVals(root.right, lst)
        
        return lst
