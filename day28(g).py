# Codechef Qn: Easy Pronunciation 

# MY SOLUTION 
T = int(input())
vowels = set("aeiou")
for _ in range(T):
    N = int(input())
    S = input().strip()
    consecutive = 0
    hard = False
    for ch in S:
        if ch not in vowels:
            consecutive += 1
            if consecutive >= 4:
                hard = True
                break
        else:
            consecutive = 0
    print("NO" if hard else "YES")