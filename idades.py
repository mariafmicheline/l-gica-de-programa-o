a = int(input('Digite uma idade:'))
b = int(input('Digite outra idade:'))
if a>b:
    print('A idade {} é a mais nova'.format(b))
elif a==b:
    print('As idades são iguais')
else:
    print('A idade {} é a mais nova'.format(a))