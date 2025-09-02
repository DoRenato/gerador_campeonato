import json
import random

from pts_corridos import (
    gerar_confrontos_possiveis,
    filtrar_confrontos_unicos,
    dividir_turnos,
    criar_todas_rodadas,
    formatar_rodadas_pts_corridos
)
from fase_grupos import(
    dividir_times_em_grupos,
    organizar_rodadas_fase_grupo,
    formatar_rodadas_fase_grupos
)



def ler_json_times(times_json):
    with open(f'dados/{times_json}.json') as file:
        times_sorteados = json.loads(file.read())
    return times_sorteados 


def times_em_lista(times_sorteados, randomizar=True):
    times=[]
    for time in times_sorteados:
        times.append(time)
    if randomizar:
        random.shuffle(times)
    return times


def exportar_rodadas(rodadas_formatadas, tipo_campeonato):
    if tipo_campeonato==1:
        nome_arquivo='rodadas_pts_corridos'
    if tipo_campeonato==2:
        nome_arquivo='rodadas_fase_grupos'
    with open(f'dados/{nome_arquivo}.txt', 'w', encoding='utf8') as file:
        file.write(rodadas_formatadas)


def criar_campeonato(times_json, randozimar_times=True, casa_fora=False, tipo_campeonato=1, qtd_grupos=2): # tipo_campeonato= 1=pts_corridos, 2=fase_grupos
    times_sorteados=ler_json_times(times_json)  
    lista_de_times=times_em_lista(times_sorteados, randozimar_times)
    if tipo_campeonato==1:
        possiveis_confrontos=gerar_confrontos_possiveis(lista_de_times) # Cria uma mega lista com todos os confrontos possiveis, inclusive repetidos
        confrontos_unicos=filtrar_confrontos_unicos(possiveis_confrontos) # Cria uma nova lista filtrando todos os confrontos unicos e removendo os repetidos
        todas_rodadas=criar_todas_rodadas(lista_de_times, confrontos_unicos) # Cria todas as rodadas do campeonato, funciona tanto pra quantidade impares ou pares do total de times
        if casa_fora:
            todas_rodadas=dividir_turnos(todas_rodadas)
        rodadas_formatadas=formatar_rodadas_pts_corridos(todas_rodadas)
        exportar_rodadas(rodadas_formatadas, tipo_campeonato)
        return todas_rodadas
    if tipo_campeonato==2:
        grupos=dividir_times_em_grupos(lista_de_times, qtd_grupos)
        if not grupos:
            return False
        rodadas_fase_grupos={}
        for grupo in grupos:
            possiveis_confrontos=gerar_confrontos_possiveis(grupos[grupo]) # Cria uma mega lista com todos os confrontos possiveis, inclusive repetidos
            confrontos_unicos=filtrar_confrontos_unicos(possiveis_confrontos) # Cria uma nova lista filtrando todos os confrontos unicos e removendo os repetidos
            todas_rodadas=criar_todas_rodadas(grupos[grupo], confrontos_unicos)
            if casa_fora:
                todas_rodadas=dividir_turnos(todas_rodadas)
            rodadas_fase_grupos[grupo]=todas_rodadas
        rodadas_organizadas_fase_grupo=organizar_rodadas_fase_grupo(rodadas_fase_grupos)
        rodadas_fase_grupos_formatada=formatar_rodadas_fase_grupos(rodadas_organizadas_fase_grupo)
        exportar_rodadas(rodadas_fase_grupos_formatada, tipo_campeonato)
        return rodadas_fase_grupos_formatada