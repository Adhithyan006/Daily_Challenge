# Codechef Qn: Coloured Ballons 
# MY SOLUTION 
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum((i+1) * a[i] for i in range(n))
    print(total)