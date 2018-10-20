# Cauculadora de Tempo que o Sistema Está Ocupado.
'''
* Programa: Cauculadora de Clientes no Sistema.
* Autor: Rômulo de Carvalho.
* email: romulo514@hotmail.com
* Descrição: Caucula o percentual em que o Sistema,
está ocupado ajudando em análise, monitoramento,
e desempenho de sistemas.
'''

# Declarando Variáveis
lamb = float(input('Digite a taxa de entrada: ')) # Média de requsições.
mi = float(input('Digite a taxa de atendimento: ')) # Média de atendimento.
tempoSistemaOcupado = lamb/mi
print('A taxa média de tempo de clientes no sistemas é {:.3f}' .format(tempoSistemaOcupado))
