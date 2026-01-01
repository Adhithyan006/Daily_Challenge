# Codechef Qn name: Entertainments
# Chef is trying to entertain N children. He has 2 options:

# Buy a single television for all the children to watch. This will cost 1000 rupees.
# Buy N toys, one for each child. This will cost 200 rupees for each toy.
# What is the minimum cost Chef needs to pay to entertain all the children?

# Input Format
# The first and only line of input contains a single integer 
# N - the number of children.

# Output Format
# Output the cost to entertain all children.

# Constraints
# 1≤N≤10

# MY SOLUTION
N = int(input().strip())
cost = min(1000, 200 * N)
print(cost)
