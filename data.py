from datetime import date
from dateutil.relativedelta import relativedelta

#função para calcular
def calcular_data_anterior(meses):
  hoje = date.today()

  # Cria um objeto 'delta' para representar a quantidade de meses
  delta = relativedelta(months=meses)

  # Calcula a data anterior subtrai o delta da data de hoje
  data_anterior = hoje - delta

  # Formata a data Americana para exibição 
  data_formatada = data_anterior.strftime('%Y de %B de %d')
  return data_formatada

# Solicita o número de meses ao usuário
while True:
  try:
    meses_str = input("Digite o número de meses (apenas números): ")
    meses = int(meses_str)
    if meses < 0:
      print("O número de meses deve ser positivo.")
      continue   # Repete o loop se o número for negativo
    break  # Sai do loop se o número for válido
  
   # Exceção para valores inválidos
  except ValueError:
    print("Valor inválido. Digite apenas números inteiros.")

# Calcula e exibe a data anterior
data_anterior = calcular_data_anterior(meses)   #Chama a função
print(f"O perido de {meses} meses atrás é: {data_anterior}")