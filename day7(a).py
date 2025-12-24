# Leetcode Qn no: 101
# Qn name: Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

#MY SOLUTION:
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and mirror(t1.left, t2.right) and mirror(t1.right, t2.left)
        return mirror(root, root)