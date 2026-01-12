# Leetcode Qn: 840. Magic-Squares In Grid
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers 
# from 1 to 9 such that each row, column, and both diagonals all have the same sum.
# Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

# Example 1:
# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# Explanation: 
# The following subgrid is a 3 x 3 magic square:
# while this one is not:
# In total, there is only one magic square inside the given grid.

# Example 2:
# Input: grid = [[8]]
# Output: 0
 
# Constraints:
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15

# MY SOLUTION
class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def isMagic(r, c):
            nums = [grid[r+i][c+j] for i in range(3) for j in range(3)]
            if sorted(nums) != list(range(1, 10)):
                return False
            s = sum(grid[r][c:c+3])
            if sum(grid[r+1][c:c+3]) != s: return False
            if sum(grid[r+2][c:c+3]) != s: return False
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != s: return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != s: return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != s: return False
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s: return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s: return False
            return True

        for r in range(rows-2):
            for c in range(cols-2):
                if isMagic(r, c):
                    count += 1
        return count