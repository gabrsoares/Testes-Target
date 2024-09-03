import json

valores = dict()

with open ('dados.json', 'r') as file:
    valores = json.load(file)

maior_dia = max(valores, key=lambda x: x['valor'])
menor_dia = min(valores, key=lambda x: x['valor'] if x['valor'] > 0 else float('+inf')) # caso o valor seja 0, retorna infinito para que ele não seja escolhido como o menor valor.

soma_valores = sum(item['valor'] for item in valores)

soma_dias = 0
for itens in valores:
    if itens['valor'] != 0:
        soma_dias += 1
media = soma_valores / soma_dias

soma_dias_maiores = 0
for itens in valores:
    if itens['valor'] > media:
        soma_dias_maiores += 1

print(f'O menor valor de faturamento foi de R${menor_dia['valor']:.2f} que ocorreu no dia {menor_dia['dia']}.')
print(f'O maior valor de faturamento foi de R${maior_dia['valor']:.2f} que ocorreu no dia {maior_dia['dia']}.')
print(f'O valor de faturamento diário foi maior do que a média mensal em {soma_dias_maiores} dias.')
