n = int(input())
count = 0
s = 1
med = 0
menor = 0
maior = 0
while n != 0:
    n = int(input())
    count = count + 1
    s += n
    med = s/count
    if count == 0:
       maior = n
       menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Foram fornecidos {} números'.format(count))
print('A soma dos números fornecidos é {}'.format(s))
print('A média aritmética entre os números é {}'.format(med))
print('O menor valor fornecido é {}'.format(menor))
print('O maior valor fornecido é {}'.format(maior))
    