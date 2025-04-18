# Aula 04 - Comentários e instrução print

# Comentários
# não são executados no programa

a = 84 # variável de exemplo para comentário

# docstring

"""
    Este é um comentário
    que ocupa várias linhas
    conhecido como docstring
"""
    
'''
    O docstring também pode ser feito
    com aspas simples
        
'''

print()
print("Se você pretende meclar 'simbolos' diferentes, faça isso")
print('Ou isso "para alterar" entre aspas simples e duplas')
print()

# Instrução print
print(a)
print("Teste de saída")
print('Teste de saída \nem várias linhas')
print('Curso', 'de', 'Python')
print('Curso', 'de', 'Python', sep='|') # o sep serve para separar as partes utilizando um caractere
print('Curso', 'de', 'Python', end='.') # o end finaliza a string com um determinado caractere
print()
print('Curso \t de \t Python') # separação por tabulador

# arquivo

arquivo = open('Aula 04 - saida.txt', 'a+')

print('Curso', 'de', 'Python', file=arquivo)
print('Sempre', 'aprendendo', 'algo novo', file=arquivo)
arquivo.close()

print()
