n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
opção = 0
while opção!= 3:
    print(''' Menu de opções:   
        [1] somar os dois números
        [2] raiz quadrada de um número
        [3] sair''')
    opção =int(input('Digite a opção desejada:'))
    if opção == 1:
        s = n1+n2
        print('A soma dos números é igual a : {} '.format(s))
    elif opção == 2:
        import math
        r1 = math.sqrt(n1)
        r2 = math.sqrt(n2)
        print('As raizes dos números são iguais a:{:.2f} e {:.2f}'.format(r1,r2))
else:
    print('Fim do programa')