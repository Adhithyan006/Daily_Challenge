# Leetcode Qn no: 145
# Qn name: Binary Tree Postorder traversal
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [3,2,1]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,6,7,5,2,9,8,3,1]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 
#  MY SOLUTION
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode):
        result = []
        self._dfs(root, result)
        return result
    
    def _dfs(self, node, result):
        if not node:
            return
        self._dfs(node.left, result)   # Traverse left subtree
        self._dfs(node.right, result)  # Traverse right subtree
        result.append(node.val)        # Visit node