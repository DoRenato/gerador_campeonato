# Gerador de Campeonatos

Este programa foi desenvolvido para criar campeonatos de futebol eletrônico (eFootball, FIFA, etc.), onde você pode organizar torneios com múltiplos jogadores e times.

## Como Funciona

O programa suporta dois tipos de campeonato:
- **Pontos Corridos**: Todos jogam contra todos
- **Fase de Grupos**: Times são divididos em grupos, depois eliminatórias

## Como Usar

### 1. Preparar o Arquivo de Times

Crie um arquivo JSON na pasta `dados/` com a seguinte estrutura:

```json
{
    "Inter de Milan": "Fulano",
    "Atl. Madrid": "Cicrano", 
    "Chelsea": "Beltrano",
    "Barcelona": "Fulaninho",
    "AC Milan": "Cicraninho",
    "Man. City": "Beltraninho",
    "Liverpool": "Deltrando",
    "PSG": "Deltrandinho"
}
```

**Formato**: `"Nome do Time": "Nome do Jogador"`

### 2. Configurar o Campeonato

Edite o arquivo `main.py` e ajuste os parâmetros conforme sua preferência:

```python
campeonato = criar_campeonato(
    times_json='times',           # Nome do arquivo JSON (sem extensão)
    randomizar_times=False,       # True = randomiza ordem dos times
    casa_fora=True,              # True = jogo de ida e volta
    tipo_campeonato=1,           # 1 = Pontos Corridos, 2 = Fase de Grupos
    qtd_grupos=2                 # Quantidade de grupos (apenas para Fase de Grupos)
)
```

### 3. Executar

```bash
python main.py
```

## Parâmetros Explicados

- **`times_json`**: Nome do arquivo JSON (sem a extensão `.json`)
- **`randomizar_times`**: Se `True`, embaralha a ordem dos times
- **`casa_fora`**: Se `True`, cada time joga em casa e fora contra cada adversário
- **`tipo_campeonato`**: 
  - `1` = Pontos Corridos (todos contra todos)
  - `2` = Fase de Grupos
- **`qtd_grupos`**: Quantidade de grupos (usado apenas no tipo 2), se não passado ele será setado automaticamente para o valor 2

## Exemplos de Saída

O programa gera arquivos de texto com as rodadas organizadas:
- `dados/rodadas_pts_corridos.txt` - Para pontos corridos
- `dados/rodadas_fase_grupos.txt` - Para fase de grupos

## Validações da Fase de Grupos

Para usar a fase de grupos, certifique-se de que:
- Mínimo de 6 times
- Número par de times
- Quantidade de grupos deve ser potência de 2 (2, 4, 8, etc.)
- Proporção adequada entre times e grupos

## Estrutura do Projeto

```
gerador_campeonato/
├── dados/                    # Arquivos de entrada e saída
│   ├── exemplos/            # Exemplos de arquivos
│   └── times.json          # Seu arquivo de times
├── main.py                 # Arquivo principal
├── pts_corridos.py         # Lógica dos pontos corridos
├── fase_grupos.py          # Lógica da fase de grupos
├── utils.py                # Funções utilitárias
└── tests/                  # Testes automatizados
```