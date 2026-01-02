# Hackerrank Qn name: Tuples 
# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers.
# Then compute and print the result of .

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Input Format
# The first line contains an integer, , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple .
# Output Format
# Print the result of .

# Sample Input 0
# 2
# 1 2
# Sample Output 0
# 3713081631934410656

# MY SOLUTION
def tuple_hash(t):
    x = 0x345678
    mult = 1000003
    z = len(t)
    for item in t:
        y = int(item)
        x = (x ^ y) * mult
        z -= 1
        mult += 82520 + z + z
    x += 97531
    x &= (1 << 64) - 1
    if x >= (1 << 63):
        x -= (1 << 64)
    if x == -1:
        x = -2
    return x

if __name__ == '__main__':
    n = int(input().strip())
    nums = tuple(map(int, input().split()))
    print(tuple_hash(nums))