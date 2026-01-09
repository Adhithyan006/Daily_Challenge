# Codeforces Qn: 427A. Police Recruits 
# The police department of your city has just started its journey. Initially, they don’t have any manpower. So, they started hiring new recruits in groups.

# Meanwhile, crimes keeps occurring within the city. One member of the police force can investigate only one crime during his/her lifetime.

# If there is no police officer free (isn't busy with crime) during the occurrence of a crime, it will go untreated.

# Given the chronological order of crime occurrences and recruit hirings, find the number of crimes which will go untreated.

# Input
# The first line of input will contain an integer n (1 ≤ n ≤ 105), the number of events. The next line will contain n space-separated integers.

# If the integer is -1 then it means a crime has occurred. Otherwise, the integer will be positive, the number of officers recruited together at that time. No more than 10 officers will be recruited at a time.

# Output
# Print a single integer, the number of crimes which will go untreated.

# Examples
# InputCopy
# 3
# -1 -1 1
# OutputCopy
# 2
# InputCopy
# 8
# 1 -1 1 -1 -1 1 1 1
# OutputCopy
# 1
# InputCopy
# 11
# -1 -1 2 -1 -1 -1 -1 -1 -1 -1 -1
# OutputCopy
# 8
# Note
# Lets consider the second example:

# Firstly one person is hired.
# Then crime appears, the last hired person will investigate this crime.
# One more person is hired.
# One more crime appears, the last hired person will investigate this crime.
# Crime appears. There is no free policeman at the time, so this crime will go untreated.
# One more person is hired.
# One more person is hired.
# One more person is hired.
# The answer is one, as one crime (on step 5) will go untreated.

# MY SOLUTION 
n = int(input())
events = list(map(int, input().split()))

officers = 0
untreated = 0

for e in events:
    if e == -1:
        if officers > 0:
            officers -= 1
        else:
            untreated += 1
    else:
        officers += e

print(untreated)