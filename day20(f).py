# Codechef Qn: Chef and Close Friends 

# MY SOLUTION:
import sys

input_data = sys.stdin.read().split()
t = int(input_data[0])
res = []
idx = 1
for _ in range(t):
    x, y, z = map(int, input_data[idx:idx+3])
    idx += 3
    left_friend = x - y
    right_friend = x + y
    left_limit = x - z
    right_limit = x + z
    left = max(left_friend, left_limit)
    right = min(right_friend, right_limit)
    if left > right:
        res.append("0")
    else:
        count = right - left + 1
        if left <= x <= right:
            count -= 1
        res.append(str(count))
print("\n".join(res))