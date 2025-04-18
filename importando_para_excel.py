import pandas as pd

dados_ocorrencias = [
    {"Ocorrência":"SS 1045/24", "Serviço":"Substituição de transformador queimado", "Localidade":"Patos", "Status":"Concluída"},
    {"Ocorrência":"SS 1050/24", "Serviço":"Instalação de poste", "Localidade":"Pombal", "Status":"Andamento"},
    {"Ocorrência":"SS 1046/24", "Serviço":"Substituição de isoladores", "Localidade":"Santa Terezinha", "Status":"Andamento"},
    {"Ocorrência":"SS 1069/24", "Serviço":"Substituição de poste", "Localidade":"Itaporanga", "Status":"Postergada"},
    {"Ocorrência":"SS 1072/24", "Serviço":"Substituição de condutores BT", "Localidade":"Pricesa Isabel", "Status":"Concluída"}
]

pd.DataFrame(dados_ocorrencias).to_excel
