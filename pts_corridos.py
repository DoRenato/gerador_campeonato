def times_em_lista(times_sorteados):
    times=[]
    for time in times_sorteados:
        times.append(times_sorteados[time])
    return times


def gerar_confrontos_possiveis(times_em_lista):
    confrontos={}
    for time in times_em_lista:
        partida_atual=[]
        for time2 in times_em_lista:    
            if time != time2:
                partida_atual.append(time2)
        confrontos[time]=partida_atual
    return confrontos


def filtrar_confrontos_unicos(confrontos_possiveis): # Vai criar todos os confrontos sem repetir os jogos. Assim o modelo de jogo de ida e volta fica para uma função idependente
    jogos_unicos=[]
    for mandante in confrontos_possiveis:
        for visitante in confrontos_possiveis[mandante]:
            confronto_atual=[mandante, visitante]
            confronto_atual_reverse=[visitante, mandante]
            if len(jogos_unicos)>0:
                if confronto_atual_reverse in jogos_unicos:
                    continue
                else:
                    confronto_atual=[mandante, visitante]
            else:
                confronto_atual=[mandante, visitante]
            jogos_unicos.append(confronto_atual)
    return jogos_unicos


def validar_times_rodada(confronto_atual, lista_rodada_atual):
    if len(lista_rodada_atual)>0:
        for time in confronto_atual:
            for confronto in lista_rodada_atual:
                if time in confronto:
                    return False
                else:
                    continue
    return True


def montar_rodada(confrontos_unicos, lista_confrontos_marcados):
    rodada_atual=[]
    for confronto in confrontos_unicos:
        if confronto in lista_confrontos_marcados:
            continue
        confronto_disponivel=validar_times_rodada(confronto, rodada_atual)
        if confronto_disponivel:
            rodada_atual.append(confronto)
            lista_confrontos_marcados.append(confronto)
        else:
            continue
    return rodada_atual


def criar_todas_rodadas(lista_de_times, confrontos_unicos):
    num_total_rodadas= len(lista_de_times)-1 if len(lista_de_times)%2==0 else len(lista_de_times)
    contador_rodada=1
    todas_rodadas={}
    lista_confrontos_marcados=[]
    while contador_rodada<=num_total_rodadas:
        string=f"Rodada {contador_rodada}"
        rodada_atual=montar_rodada(confrontos_unicos, lista_confrontos_marcados)
        for confronto_criado in rodada_atual:
            lista_confrontos_marcados.append(confronto_criado)
        todas_rodadas[string]=rodada_atual
        contador_rodada+=1
    return todas_rodadas