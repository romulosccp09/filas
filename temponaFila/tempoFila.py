# Cauculadora tempo de Clientes na Filas.
'''
* Programa: Cauculadora de Tempo Clientes na Fila.
* Autor: Rômulo de Carvalho.
* email: romulo514@hotmail.com
* Descrição: Caucula a taxa média, do tempo de clienes na Fila,
 ajudando em análise, monitoramento, e desempenho de sistemas.

'''

# Declarando Variáveis
lamb = float(input('Digite a taxa de entrada: ')) # Média de requsições.
mi = float(input('Digite a taxa de atendimento: ')) # Média de atendimento
tempoFila = lamb/(mi*(mi-lamb))
print('O tempo de espera na fila é: {:.3f}' .format(tempoFila))
