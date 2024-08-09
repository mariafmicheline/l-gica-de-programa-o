#a) utilizando o para
import math
n = int(input())
for i in range(n):
    f = math.factorial(n)
print(f)

#b) utlizando o enquanto
num = int(input())
result = 1
count = 1
while count <= num:
    result *= count
    count += 1
print(result)