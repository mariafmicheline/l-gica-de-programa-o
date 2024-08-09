a = int(input('Digite um número:'))
b = int(input('Digite outro número:'))
if a > b:
    print('Número maior é o {} e o menor é o {}'.format(a,b))
elif a == b:
    print('Os números são iguais')
else:
    print('Número maior é o {} e o menor é o {}'.format(b,a))