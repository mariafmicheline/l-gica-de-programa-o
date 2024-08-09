a,b = map(float,input().split())
if a==1:
    total = b*4
    print('Total: R$ {:.2f}'.format(total))
elif a==2:
    total = b*4.5
    print('Total: R$ {:.2f}'.format(total))
elif a==3:
    total = b*5.00
    print('Total: R$ {:.2f}'.format(total))
elif a==4:
    total = b*2.00
    print('Total: R$ {:.2f}'.format(total))
elif a==5:
    total = b*1.5
    print('Total: R$ {:.2f}'.format(total))