# Docstring

def minhaFuncao(parametro1, parametro2, parametro3, parametro4):
    """
        Descrição: função de três parâmetros de exemplo
        Utilização: aprendizado de um novo recurso
        Parâmetros:
            parâmetro1: qualquer tipo de dados
            parâmetro2: qualquer tipo de dados
            parâmetro3: qualquer tipo de dados
            parâmetro4: qualquer tipo de dados
    """
    print(type(parametro1), type(parametro2), type(parametro3), type(parametro4))
    print("===== Vamos saber os tipos de dados nos parâmetros! =====")
    print(f"O valor do parâmetro 1 é {parametro1}, e seu tipo é {type(parametro1)}")
    print(f"O valor do parâmetro 2 é {parametro2}, e seu tipo é {type(parametro2)}")
    print(f"O valor do parâmetro 3 é {parametro3}, e seu tipo é {type(parametro3)}")
    print(f"O valor do parâmetro 4 é {parametro4}, e seu tipo é {type(parametro4)}")

minhaFuncao('André', 32, [1, 3, 5], 3.14)
