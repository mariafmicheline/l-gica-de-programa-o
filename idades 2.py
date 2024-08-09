n1 = str(input('Digite seu nome:'))
n2 = str(input('Informe outro nome:'))
d1 = int(input('Digite sua idade {}: '.format(n1)))
d2 = int(input('Agora, digite sua idade {}:'.format(n2)))
if d1>d2:
    print('{} é o(a) mais velho'.format(n1))
elif d1==d2:
    print('As idades de {} e {} são iguais'.format(n1,n2))
else:
    print('{} é o(a) mais velho'.format(n2))