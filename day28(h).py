# Codechef Qn: ATM Machine 

# MY SOLUTION
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = []
    for x in A:
        if K >= x:
            result.append('1')
            K -= x
        else:
            result.append('0')
    print("".join(result))