import json
from pts_corridos import *



def ler_json_times(times_json):
    with open(f'dados/{times_json}.json') as file:
        times_sorteados = json.loads(file.read())
    return times_sorteados 


def criar_campeonato(times_json, randozimar_times=True, casa_fora=False, tipo_campeonato=1):
    times_sorteados=ler_json_times(times_json)  
    lista_de_times=times_em_lista(times_sorteados, randozimar_times)
    possiveis_confrontos=gerar_confrontos_possiveis(lista_de_times) # Cria uma mega lista com todos os confrontos possiveis, inclusive repetidos
    confrontos_unicos=filtrar_confrontos_unicos(possiveis_confrontos) # Cria uma nova lista filtrando todos os confrontos unicos e removendo os repetidos
    todas_rodadas=criar_todas_rodadas(lista_de_times, confrontos_unicos) # Cria todas as rodadas do campeonato, funciona tanto pra quantidade impares ou pares do total de times
    if casa_fora:
        todas_rodadas=dividir_turnos(todas_rodadas)
    string=""
    for rodada, jogos in todas_rodadas.items(): # Esse trecho é apenas para a saida formatada no arquivo rodadas.txt
        string_atual=f"{rodada}:\n"
        for time1, time2 in jogos:
            string_atual+=f"  - {time1} vs {time2}\n"
        string_atual+='\n'
        string+=string_atual
    with open('dados/rodadas.txt', 'w', encoding='utf8') as file:
        file.write(string)
    return todas_rodadas