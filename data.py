d = int(input('Que dia é hoje?'))
m = int(input('Qual mês estamos? '))
a = int(input('Qual ano estamos?'))
if m == 1:
    m = 'janeiro'
elif m == 2:
    m = 'fevereiro'
if m == 3:
    m = 'março'
if m == 4:
    m = "abril"
elif m == 5:
    m = 'maio'
if m == 6:
    m = 'junho'
elif m == 7:
    m = 'julho'
if m == 8:
    m = 'agosto'
elif m == 9:
   m = 'setembro' 
if m == 10:
    m = 'outubro'
elif m == 11:
    m = 'novembro'
if m == 12:
    m = 'dezembro'
print('{} de {} de {}'.format(d,m,a))

