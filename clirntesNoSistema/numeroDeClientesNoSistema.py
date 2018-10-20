# Cauculadora de Clientes no Sistema.
'''
* Programa: Cauculadora de Clientes no Sistema.
* Autor: Rômulo de Carvalho.
* email: romulo514@hotmail.com
* Descrição: Caucula número de clienes no Sistema, ajudando em análise,
 monitoramento, e desempenho de sistemas.
'''

# Declarando Variáveis
lamb = float(input('Digite a taxa de entrada: ')) # Média de requsições.
mi = float(input('Digite a taxa de atendimento: ')) # Média de atendimento.
clientesNoSistema = lamb/(mi-lamb)
print('O número de Clientes no sistema é: {:.3}' .format(clientesNoSistema))
