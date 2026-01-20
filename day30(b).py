# Codeforces Qn: 32B. Borze
# Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to decode the Borze code, i.e. to find out the ternary number given its representation in Borze alphabet.

# Input
# The first line contains a number in Borze code. The length of the string is between 1 and 200 characters. It's guaranteed that the given string is a valid Borze code of some ternary number (this number can have leading zeroes).

# Output
# Output the decoded ternary number. It can have leading zeroes.

# Examples
# InputCopy
# .-.--
# OutputCopy
# 012
# InputCopy
# --.
# OutputCopy
# 20
# InputCopy
# -..-.--
# OutputCopy
# 1012

# MY SOLUTION
s = input().strip()
i = 0
res = []
while i < len(s):
    if s[i] == '.':
        res.append('0')
        i += 1
    else:
        if s[i+1] == '.':
            res.append('1')
            i += 2
        else:
            res.append('2')
            i += 2
print("".join(res)) 