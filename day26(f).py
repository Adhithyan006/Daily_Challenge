# Codechef Qn: Protein Diet  

# MY SOLUTION 
import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        if idx >= len(input_data):
            break
        n = int(input_data[idx])
        s = input_data[idx + 1]
        idx += 2
        
        counts = Counter(s)
        if all(count <= 2 for count in counts.values()):
            results.append("YES")
        else:
            results.append("NO")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()