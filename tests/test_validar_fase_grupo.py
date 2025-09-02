import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fase_grupos import validar_criacao_fase_grupo


def test_cenario_valido():
    """Testa um cenário válido: 8 times com 2 grupos"""
    qtd_times=8
    qtd_grupos=2
    times = [f'Time{i+1}' for i in range(qtd_times)]
    resultado = validar_criacao_fase_grupo(times, qtd_grupos)
    assert resultado == True


def test_cenario_invalido():
    """Testa um cenário inválido: 8 times com 4 grupos"""
    qtd_times=8
    qtd_grupos=4
    times = [f'Time{i+1}' for i in range(qtd_times)]
    resultado = validar_criacao_fase_grupo(times, qtd_grupos)
    assert resultado == False


def test_qtd_minima_de_times():
    """Testa um cenário inválido: 4 times"""
    qtd_times=4
    qtd_grupos=2
    times = [f'Time{i+1}' for i in range(qtd_times)]
    resultado = validar_criacao_fase_grupo(times, qtd_grupos)
    assert resultado == False


def test_numero_impar_times():
    """Testa se rejeita número ímpar de times"""
    qtd_times=9
    qtd_grupos=2
    times = [f'Time{i+1}' for i in range(qtd_times)]
    resultado = validar_criacao_fase_grupo(times, qtd_grupos)
    assert resultado == False


def test_grupos_nao_potencia_de_2():
    """Testa se rejeita grupos que não são potência de 2"""
    qtd_times=10
    qtd_grupos=3
    times = [f'Time{i+1}' for i in range(qtd_times)]
    resultado = validar_criacao_fase_grupo(times, qtd_grupos)
    assert resultado == False


def test_grupos_possiveis(): # Se a quantidade de grupos é possivel para a quantidade de times
    """Testa se rejeita quando grupos é desproporcional ao número de times"""
    qtd_times=10
    qtd_grupos=4
    times = [f'Time{i+1}' for i in range(qtd_times)]
    resultado = validar_criacao_fase_grupo(times, qtd_grupos)
    assert resultado == False


def test_grupos_possiveis_2(): # Se a quantidade de grupos é possivel para a quantidade de times
    """Testa se rejeita quando grupos é desproporcional ao número de times"""
    qtd_times=18
    qtd_grupos=4
    times = [f'Time{i+1}' for i in range(qtd_times)]
    resultado = validar_criacao_fase_grupo(times, qtd_grupos)
    assert resultado == False


def test_parametro_padrao():
    """Testa se o parâmetro padrão funciona"""
    qtd_times=8
    qtd_grupos=2
    times = [f'Time{i+1}' for i in range(qtd_times)]
    resultado = validar_criacao_fase_grupo(times, qtd_grupos)  # Sem passar qtd_grupos
    assert resultado == True
