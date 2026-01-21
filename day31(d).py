# Codeforces Qn: 1512A - Spy Detected!
# You are given an array aconsisting of n (n≥3) positive integers. It is known that in this array, all the numbers except one are the same
# (for example, in the array [4,11,4,4] all numbers except one are equal to 4).
# Print the index of the element that does not equal others. The numbers in the array are numbered from one.

# Input
# The first line contains a single integer t (1≤t≤100). Then t test cases follow.
# The first line of each test case contains a single integer n (3≤n≤100) — the length of the array a.
# The second line of each test case contains n integers a1,a2,…,an (1≤ai≤100).
# It is guaranteed that all the numbers except one in the a array are the same.

# Output
# For each test case, output a single integer — the index of the element that is not equal to others.

# Example
# InputCopy
# 4
# 4
# 11 13 11 11
# 5
# 1 4 4 4 4
# 10
# 3 3 3 3 10 3 3 3 3 3
# 3
# 20 20 10
# OutputCopy
# 2
# 1
# 5
# 3

# MY SOLUTION 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != a[1] and a[0] != a[2]:
        print(1)
    else:
        for i in range(1, n):
            if a[i] != a[0]:
                print(i+1)
                break