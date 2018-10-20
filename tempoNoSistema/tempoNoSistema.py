# Cauculadora de Tempo de Clientes no Sistema.
'''
* Programa: Cauculadora de Clientes no Sistema.
* Autor: Rômulo de Carvalho.
* email: romulo514@hotmail.com
* Descrição: Caucula a taxa do tempo de clienes no Sistema, ajudando em análise,
 monitoramento, e desempenho de sistemas.
'''

# Declarando Variáveis
lamb = float(input('Digite a taxa de entrada: ')) # Média de requsições.
mi = float(input('Digite a taxa de atendimento: ')) # Média de atendimento.
tempoSistema = 1/(mi-lamb)
print('A taxa média de tempo de clientes no sistemas é {:.3f}' .format(tempoSistema))
