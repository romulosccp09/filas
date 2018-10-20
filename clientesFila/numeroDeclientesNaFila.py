# Cauculadora de Clientes na Filas.
'''
* Programa: Cauculadora de Clientes na Fila
* Autor: Rômulo de Carvalho.
* email: romulo514@hotmail.com
* Descrição: Caucula número de clienes na fila, ajudando em análise,
 monitoramento, e desempenho de sistemas.
'''

# Declarando Variáveis
lamb = float(input('Digite a taxa de entrada: ')) # Média de requsições.
mi = float(input('Digite a taxa de atendimento: ')) # Média de atendimento.
clientesNaFila = (pow(lamb,2))/(mi*(mi-lamb))
print("número de clientes na fila é: {:.3f}" .format(clientesNaFila))
