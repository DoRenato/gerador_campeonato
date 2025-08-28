import json
from pts_corridos import *


# Lê o arquivo com os times na pasta dados
with open('dados/times.json') as file:
    times_sorteados = json.loads(file.read())

# Transforma o arquivo em lista     
lista_de_times=times_em_lista(times_sorteados)

# Cria uma mega lista com todos os confrontos possiveis, mesmo repetidos
possiveis_confrontos=gerar_confrontos_possiveis(lista_de_times)

# Cria uma nova lista filtrando todos os confrontos unicos e removendo os repetidos
confrontos_unicos=filtrar_confrontos_unicos(possiveis_confrontos)

# Cria todas as rodadas do campeonato, se 'casa_fora' estiver como True irá criar os jogos de ida e volta. 
rodadas=criar_todas_rodadas(lista_de_times, confrontos_unicos, casa_fora=False)

# Esse trecho é apenas para criar uma saída formatada no arquivo rodadas.txt
string=""
for rodada, jogos in rodadas.items():
    string_atual=f"{rodada}:\n"
    for time1, time2 in jogos:
        string_atual+=f"  - {time1} vs {time2}\n"
    string_atual+='\n'
    string+=string_atual
with open('dados/rodadas.txt', 'w', encoding='utf8') as file:
    file.write(string)