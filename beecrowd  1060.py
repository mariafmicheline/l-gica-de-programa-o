count = 0
neg = 0
imp = 0
par = 0
for n in range(5):
    n = int(input())
    if n%2==0:
        par = par+1
    elif n%2 != 0:
        imp = imp+1
    if n>0:
        count = count+1
    if n<0:
        neg = neg+1
print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(imp))
print('{} valor(es) positivo(s)'.format(count))
print('{} valor(es) negativo(s)'.format(neg))
    

    