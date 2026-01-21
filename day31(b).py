# Codechef Qn: Encoding Message

# MY SOLUTION 
T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input().strip())
    for i in range(0, N - 1, 2):
        S[i], S[i+1] = S[i+1], S[i]
    for i in range(N):
        S[i] = chr(ord('a') + (25 - (ord(S[i]) - ord('a'))))
    print("".join(S))