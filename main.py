from utils import criar_campeonato



campeonato=criar_campeonato(
    times_json='times', # Apenas o nome do arquivo, sem extensão. O programa já reconhece que será um json
    randozimar_times=False, # Se True, vai randomizar os times que foi escrito no json
    casa_fora=True, # Se True, irá criar as rodadas de casa e fora
    tipo_campeonato=1, # 1= Pontos corridos, 2= Fase de grupos
    # qtd_grupos=2 # Parâmetro opcional, usado somente no formato fase de grupos, para definir a quantidade de grupos.
)