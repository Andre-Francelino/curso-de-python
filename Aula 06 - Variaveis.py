# Aula 06: Variáveis
# Tipos de dados em Python
# int   | Inteiro
# float | Real / Ponto Flutuante
# bool  | Booleano / Verdadeiro (True) ou Falso (False)
# complex   | Tipo complexo
# str   | String / Texto / Alfanuméricos


# Variáveis de texto
texto = 'Curso de Python - Profº Trovato'
print(texto)
print('Tipo:', type(texto))
print()

varNumero = '150'
print(varNumero)
print('Tipo:', type(varNumero))
print()


# Variáveis para tipos numéricos
varA = 99
varB = 2.75814
varC = False
varD = 2+9j
varE = 'Python'
varF = True
varG = -3

print(varA, varB, varC, varD, varE, varF, varG)
print(type(varA), type(varB), type(varC), type(varD), type(varE), type(varF), type(varG))
print()
print(varA, '=> seu tipo é:', type(varA))
print(varB, '=> seu tipo é:', type(varB))
print(varC, '=> seu tipo é:', type(varC))
print(varD, '=> seu tipo é:', type(varD))
print(varE, '=> seu tipo é:', type(varE))
print(varF, '=> seu tipo é:', type(varF))
print(varG, '=> seu tipo é:', type(varG))
print()


# Conversões de tipos 
varH = float(varA)
print("Float de varH:", type(varH))
print('Então o valor convertido ficou:', varH)
print()

varI = int(varB)
print('Int de varI:', type(varI))
print('Então o valor convertido ficou:', varI)
print()


# Variáveis booleanas
varJ = True
varK = False
varL = not(True)
varM = not(False)

print(varJ, varK, varL, varM)
print()
