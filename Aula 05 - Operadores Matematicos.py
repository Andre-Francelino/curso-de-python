# Aula 05: Operadores Matemáticos

valorA = 99
valorB = 5

print()

print('Variáveis: A:', valorA, 'B:', valorB)
print('Somar:', valorA + valorB)
print('Subtrair:', valorA - valorB)
print('Multiplicar:', valorA * valorB)
print('Elevar a uma potência:', valorA ** valorB)
print('Dividir:', valorA / valorB)
print('Dividir truncando (sem casas decimais):', valorA // valorB)
print('MOD ou calcular o resto da divisão:', valorA % valorB)

print()

# Prioridades das Operações
# Potencia e Radiciação são efetuadas primeiro
# Depois, Multiplicação e Divisão, e por ultimo a soma e subtração
print(-2 * 4 + 3 ** 2)

# Se houverem parênteses, as operações dentro deles são efetuadas como prioridade
print(-2 * (4 + 3) ** 2)

A = 5
B = 2
C = 3
D = 4

print('Média:', (A + B + C + D)/4)

print('Prioridade:', A * B + C)
print('Prioridade:', A * (B + C))

print('Multiplicando String:', 'x' * 30)

# Operadores incrementais
print()
valorX = 10
print('valorX:', valorX)

valorX += 10 # valorX = valorX + 10
print('valorX incrementado:', valorX)

valorX *= 2 # valorX = valorX * 2
print('valorX incrementado por multiplicação:', valorX)
