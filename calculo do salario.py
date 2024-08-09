s = float(input('Informe seu salário:'))
t = float(input('Agora,informe suas horas trabalhadas no mês:'))
h = float(t*6.42)
i = float(0.03)
f = h*i
totaly = s - i 
print('O salário que você irá receber equivale a: {}'.format(totaly))
