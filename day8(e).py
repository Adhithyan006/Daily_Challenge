# # Codeforces Qn no: 486A
# # Qn name: A.Calculating Function

# For a positive integer n let's define a function f:
# f(n) =  - 1 + 2 - 3 + .. + ( - 1)nn
# Your task is to calculate f(n) for a given integer n.

# Input
# The single line contains the positive integer n (1 ≤ n ≤ 1015).

# Output
# Print f(n) in a single line.

# Examples
# InputCopy
# 4
# OutputCopy
# 2
# InputCopy
# 5
# OutputCopy
# -3
# Note
# f(4) =  - 1 + 2 - 3 + 4 = 2

# f(5) =  - 1 + 2 - 3 + 4 - 5 =  - 3



#MY SOLUTION
n = int(input())
print(n//2 if n % 2 == 0 else -(n//2 + 1))
    