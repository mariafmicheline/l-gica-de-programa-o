print('Digite três valores a seguir por linha:')
x = input().split()
y = input().split()
a,b,c = x
a = int(a)
b = int(b)
c = int(c)
if  a==0 and b==0 and c==0:
    saida = 'Nenhum'
if  a==0 and b==0 and c==1:
    saida = 'Direita'
elif a==0 and b==1 and c==0:
    saida = 'Centro'
if a==0 and b==1 and c==1:
    saida = 'Centro-direita'
elif a==1 and b==0 and c==0:
    saida = 'Esquerda'
if a==1 and b==0 and c==1:
    saida = 'Esquerda-direita'
elif a==1 and b==1 and c==0:
    saida = 'Centro-esquerda'

def criartabela():
    print('Entrada 1\tEntrada 2\tEntrada 3\t\tSaída')
    print('---------------------------------------------------------------------')
    print('%i\t\t%i\t\t%i\t\t\t%s' % (a,b,c,saida))
    print('---------------------------------------------------------------------')
    print('%i\t\t%i\t\t%i\t\t\t%s' % (a,b,c,saida))
    print('---------------------------------------------------------------------')
    print('%i\t\t%i\t\t%i\t\t\t%s' % (a,b,c,saida))
    print('---------------------------------------------------------------------')
    print('%i\t\t%i\t\t%i\t\t\t%s' % (a,b,c,saida))
    print('---------------------------------------------------------------------')
    print('%i\t\t%i\t\t%i\t\t\t%s' % (a,b,c,saida))
    print('---------------------------------------------------------------------')
    print('%i\t\t%i\t\t%i\t\t\t%s' % (a,b,c,saida))
    print('---------------------------------------------------------------------')
    print('%i\t\t%i\t\t%i\t\t\t%s' % (a,b,c,saida))
    print('---------------------------------------------------------------------')
    
criartabela()