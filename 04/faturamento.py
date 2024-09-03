valores = {
    'SP':67836.43,
    'RJ':36678.66,
    'MG':29229.88,
    'ES':27165.48,
    'OUTROS':19849.53 
}

total = 0
for valor in valores.values():
    total += valor

print(f'Valor total: R${total}')
print('Percentual de representação')

for estado, valor in valores.items():
    percentual = (valor * 100.0)/ total
    print(f'{estado} - {percentual:.2f}%')
