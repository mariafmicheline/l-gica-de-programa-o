a = float(input())
b = float(input())
c = float(input())
import math
angulo = ((b**2)+(c**2)-(a**2))/(2*b*c)
math.cos(math.radians(angulo)) 
graus = (angulo*180)/math.pi 
print('O valor do ângulo em graus é:{:.2f}'.format(graus))
