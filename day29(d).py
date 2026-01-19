# Codechef Qn: Adjacent Sum Parity 

# MY SOLUTION 
T = int(input())
for _ in range(T):
    N = int(input())
    B = list(map(int, input().split()))
    ok = False
    for start in [0, 1]:
        A = [0] * N
        A[0] = start
        valid = True
        for i in range(N-1):
            A[i+1] = (B[i] - A[i]) % 2
        if (A[-1] + A[0]) % 2 == B[-1]:
            ok = True
            break
    print("YES" if ok else "NO")