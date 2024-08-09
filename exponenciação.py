a = float(input())
b = int(input())
result = 1
count = 1
for i in range(b):
    count += b
    result *= a
print('{}^{} = {} = {}'.format(a,b,count,result))