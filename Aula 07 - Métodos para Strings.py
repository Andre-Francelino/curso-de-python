# Método é um procedimento que pode manipular atributos de objetos
# para qual o método foi chamado

print()
print(type('Rock and Roll'))
print(('esse texto é um exEmplo para Testar o método capitalize'.capitalize()))
print()

# Concatenação de textos (Strings)
textoA = "Heavy"
textoB = "Metal"
textoC = "is"
textoD = "the"
textoE = "Law"
resultadoConcatenacao = textoA + ' ' + textoB + ' ' + textoC + ' ' + textoD + ' ' + textoE

print(resultadoConcatenacao)
print(resultadoConcatenacao.upper())
print(resultadoConcatenacao.lower())
print()

varA, varB = 99, 257
print('Resultado', varA + varB)
print('Resultado ' + str(varA + varB))
print()

# Métodos para os textos
varTexto = 'Curso Introdução a linguagem Python'

# Preenchimento usando caracteres
print(varTexto.ljust(50, '.'))
print(varTexto.ljust(50) + '|')

print(varTexto.rjust(50, '-'))
print(varTexto.rjust(50))

print(varTexto.center(50, '='))
print(varTexto.center(50))

print()

# Repetição de caracteres
print('X' * 50)
print()

# Alteração da caixa das palavras A/a
varTexto = 'curso introdução a linguagem python'
print('Resultado usando o método title(): ', varTexto.title())
print('andré francelino'.title())

print('André'.swapcase())

print()

# Função LEN (tamanho da string)
print(len(varTexto))

print(len('...And Justice For All...'))

print()

# Extração de texto
print(varTexto[0])
print(varTexto[0:5])
print(len(varTexto[0:5]))
print(varTexto[6])
print(varTexto[6:])
print(len(varTexto[6:]))
print(varTexto[:9])

# Eliminar espaços desnecessários
varTexto = '                Curso introdução a linguagem Python   '
print('Como está a string antes da limpeza:', varTexto)
print('Tamanho da string antes da limpeza:', len(varTexto))
print('Limpando a string:', varTexto.strip())
print('Tamanho da string após a limpeza:', len(varTexto.strip()))

print()

# Concatenar caracteres a sua string
linguagem = 'Python'
print('-'.join(linguagem))

jogo = 'Medal of Honor'
print('_'.join(jogo))

print()





