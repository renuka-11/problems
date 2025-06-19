# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
shoes=list(map(int, input().split()))
stock = Counter(shoes)
N=int(input())
total=0
for _ in range(N):
    size, price = map(int, input().split())
    if stock[size] > 0:
        total += price
        stock[size] -= 1

print(total)
