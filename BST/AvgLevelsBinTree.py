"""
	637. Average of Levels in Binary Tree Easy

	Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10^-5 of the actual answer will be accepted.

	Input: root = [3,9,20,null,15,7]
	Output: [3.00000,14.50000,11.00000]
	Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
	Hence return [3, 14.5, 11].

	Input: root = [3,9,20,15,7]
	Output: [3.00000,14.50000,11.00000]


	Runtime 48ms 77.02% of python3 submissions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        avgs = []
        queue = deque([root])
        count = 0
        sum = 0
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                sum += node.val
                count += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avgs.append(sum / count)
            sum = 0
            count = 0
        return avgs
            