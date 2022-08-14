# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

string, length = input().split()
output = ["".join(i) for i in permutations(string, int(length))]
output.sort()
print("\n".join(output))
