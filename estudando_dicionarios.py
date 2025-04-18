from pprint import pprint

especificacoes_contrabaixo = {
    "marca" : "Fender",
    "modelo" : "Precision Bass",
    "serie" : "American DLX Player Series",
    "qtd_cordas" : 4,
    "cor_pintura" : "Ciano",
    "escudo" : "Sanduiche 3ply",
    "cor_escudo":"branco",
    "madeira_corpo" : "Alder",
    "madeira_braco" : "Maple - modern C shape",
    "medeira_escala" : "Maple",
    "largura_escala" : "864mm",
    "qtd_trates" : 20,
    "tipo_trates" : "Medium Jumbo",
    "material_nut" : "Osso",
    "largura_nut" : "41.3mm",
    "tarraxas" : "Standart",
    "ponte" : "Standart Vintage",
    "captador" : "Alnico 5 Split Single-Coil PB",
    "controles" : "MV/MT",
    "peso" : "3.8kg",
    "preco": 8499.88
}

arquivo = open('especificacoes.txt', 'a+')

print(especificacoes_contrabaixo, file=arquivo)
pprint(especificacoes_contrabaixo)
