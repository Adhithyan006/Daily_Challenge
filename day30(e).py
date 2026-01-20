Codechef Qn: Break the Stick

# MY SOLUTION
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    if n%2==0 or x%2==1:
        print("YES")
    else:
        print("NO")
