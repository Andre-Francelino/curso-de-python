#BEECROWD 1036 - Fórmula de Bhaskara
#https://www.beecrowd.com.br/judge/pt/problems/view/1036
#Chamando biblioteca MATH
import math

#Entradas - 3 valores de ponto flutuante
a, b, c = map(float, input().split())

#Condicionais
if a != 0:
    delta = b ** 2 - 4 * a * c

    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print('R1 = %.5f' % x1) #Saída da raiz X'
        print('R2 = %.5f' % x2) #Saída da raiz X''
    else:
        print('Impossivel calcular') #Saída
else:
    print('Impossivel calcular') #Saída
