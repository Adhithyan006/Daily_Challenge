# Leetcode Qn: 3454. Seperate Squares II 
# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and
# the side length of a square parallel to the x-axis.
# Find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals 
# the total area covered by squares below the line.
# Answers within 10-5 of the actual answer will be accepted.
# Note: Squares may overlap. Overlapping areas should be counted only once in this version.

# Example 1:
# Input: squares = [[0,0,1],[2,2,1]]
# Output: 1.00000
# Explanation:
# Any horizontal line between y = 1 and y = 2 results in an equal split, with 1 square unit above and 1 square unit below.
# The minimum y-value is 1.

# Example 2:
# Input: squares = [[0,0,2],[1,1,1]]
# Output: 1.00000
# Explanation:
# Since the blue square overlaps with the red square, it will not be counted again. 
# Thus, the line y = 1 splits the squares into two equal parts.

# Constraints:
# 1 <= squares.length <= 5 * 104
# squares[i] = [xi, yi, li]
# squares[i].length == 3
# 0 <= xi, yi <= 109
# 1 <= li <= 109
# The total area of all the squares will not exceed 1015.

# MY SOLUTION 
class Solution:
    def separateSquares(self, squares):
        from bisect import bisect_left
        events = {}
        ys = set()
        for x, y, l in squares:
            ys.add(y); ys.add(y+l)
            events.setdefault(y, []).append((1, x, x+l))
            events.setdefault(y+l, []).append((-1, x, x+l))
        ys = sorted(ys)
        active = []
        area_prefix = [0.0]
        widths = []
        for i in range(len(ys)-1):
            y = ys[i]
            for typ, x1, x2 in events.get(y, []):
                if typ == 1:
                    active.append((x1, x2))
                else:
                    active.remove((x1, x2))
            merged = []
            for a, b in sorted(active):
                if not merged or a > merged[-1][1]:
                    merged.append([a, b])
                else:
                    merged[-1][1] = max(merged[-1][1], b)
            width = sum(b - a for a, b in merged)
            heights = ys[i+1] - ys[i]
            area_prefix.append(area_prefix[-1] + width * heights)
            widths.append(width)
        total = area_prefix[-1]
        target = total / 2.0
        i = bisect_left(area_prefix, target)
        if i < len(area_prefix) and abs(area_prefix[i] - target) <= 1e-12:
            return float(ys[i])
        lo_idx = i - 1
        base = area_prefix[lo_idx]
        width = widths[lo_idx]
        return ys[lo_idx] + (target - base) / width if width > 0 else float(ys[lo_idx])