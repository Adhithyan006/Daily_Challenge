# Codechef Qn name: Signal 
# MY SOLUTION 
T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    S = input().strip()
    seen_silence = False
    count = 0
    for ch in S:
        if ch == '0':
            seen_silence = True
        elif ch == '1' and seen_silence:
            count += 1
    print(count)