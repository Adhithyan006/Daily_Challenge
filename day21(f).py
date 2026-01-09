# Codechef Qn: Bull or Bear 

# MY SOLUTION 
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if y > x:
        print("PROFIT")
    elif y < x:
        print("LOSS")
    else:
        print("NEUTRAL")