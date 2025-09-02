import random

from pts_corridos import (
    gerar_confrontos_possiveis,
    filtrar_confrontos_unicos,
    criar_todas_rodadas
)



# def time_em_lista(times_list,randomizar_times=True):
#     if randomizar_times:
#         times_list=random.sample(times_list, len(times_list))
#     return times_list


def validar_criacao_fase_grupo(times_list, qtd_grupos=2):
    total_times=len(times_list)
    times_prox_fase=2 # quantidade de times por grupo que passam pra proxima fase
    times_sobram=total_times/qtd_grupos-times_prox_fase # quantidade de times por grupo que não passam pra proxima fase
    if total_times<6:
        print('quantidade de times insuficiente')
        return False
    if total_times%2!=0:
        print('tamanho do grupo invalido')
        return False
    if (qtd_grupos & (qtd_grupos - 1))!=0: # Verifica se é potencia de 2 *Só funciona especificamente pra 2
        print('quantidade de grupos invalida')
        return False
    if times_sobram==0:
        print('times insuficientes para a quantidade de grupos, todos do grupo passariam')
        return False
    if times_sobram%1!=0:
        print('times insuficientes para a quantidade de grupos')
        return False
    return True


def dividir_times_em_grupos(times_list,qtd_grupos,randomizar_times=True):
    grupo_valido=validar_criacao_fase_grupo(times_list, qtd_grupos)
    if grupo_valido == False:
        return False
    grupos={}
    times_por_grupo=len(times_list)/qtd_grupos
    letra_grupo_inicial=65 # A letra 'A' é o 65 na tabela ASCII
    grupo_atual=[]
    for i in range(len(times_list)):
        grupo_atual.append(times_list[i])
        if len(grupo_atual)==times_por_grupo:
            grupos[chr(letra_grupo_inicial)]=grupo_atual
            letra_grupo_inicial+=1
            grupo_atual=[]
    return grupos


def organizar_rodadas_fase_grupo(todas_rodadas_fase_grupos):
    rodadas_final={}
    for letra_grupo in todas_rodadas_fase_grupos:
        for nome_rodada in todas_rodadas_fase_grupos[letra_grupo]:
            if rodadas_final.get(nome_rodada) == None:
                rodadas_final[nome_rodada]={}
            for confronto in todas_rodadas_fase_grupos[letra_grupo][nome_rodada]:
                if rodadas_final[nome_rodada].get(letra_grupo):
                    rodadas_final[nome_rodada][letra_grupo].append(confronto)
                else:
                    rodadas_final[nome_rodada][letra_grupo]=[confronto]
    return rodadas_final


def formatar_rodadas_fase_grupos(rodadas_organizadas_fase_grupos):
    string=""
    for rodada, jogos in rodadas_organizadas_fase_grupos.items(): # Esse trecho é apenas para a saida formatada no arquivo rodadas.txt
        string_atual=f"{rodada}:\n"
        for grupo, confrontos in jogos.items():
            for time1, time2 in confrontos:
                string_atual+=f"  - {time1} vs {time2} (Grupo {grupo})\n"
        string_atual+='\n'
        string+=string_atual
    return string



if __name__ == '__main__':
    from utils import ler_json_times, times_em_lista

    times_dict=ler_json_times('times')
    times=times_em_lista(times_dict)
    grupos=dividir_times_em_grupos(times, qtd_grupos=2)

    confrontos_unicos_grupos={}
    for grupo in grupos:
        confrontos_possiveis=gerar_confrontos_possiveis(grupos[grupo])
        confrontos_unicos=filtrar_confrontos_unicos(confrontos_possiveis)
        confrontos_unicos_grupos[grupo]=confrontos_unicos
    

    print(grupos)
    print(confrontos_unicos_grupos)