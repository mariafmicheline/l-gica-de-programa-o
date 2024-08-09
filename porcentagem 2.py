s = float(input('João informe seu salário:'))
c1 = float(input('Informe o valor da primeira conta:'))
c2 = float(input('Informe o valor da segunda conta:'))
m1 = (c1*0.02)+c1
m2 = (c2*0.02)+c2
r = s-(m1+m2)
print('O valor restante do seu salário é igual a: {}'.format(r))