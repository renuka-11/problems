# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
line = input().split()
s=line[0]
k=int(line[1])
sorted_s=sorted(s)
perm = permutations(sorted_s, k)


for p in perm:
    print(''.join(p))


