a1 = input('Digite o nome do primeiro aluno:')
a2 = input('Digite o segundo aluno:')
a3 = input('Digite o terceiro aluno:')

def criartabela():
    
    print('Matrícula\t\tNome do aluno\t\tNotas')
    print('------------------------------------------------------------------')
    print('%i:\t\t\t%s\t\t\t%f' % (1,a1,9.5))
    print('%i:\t\t\t%s\t\t\t%f' % (2,a2,5.8))
    print('%i:\t\t\t%s\t\t\t%f' % (3,a3,10))
    print('------------------------------------------------------------------')


criartabela()