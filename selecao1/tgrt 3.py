import json

with open('faturamento_diario.json', 'r') as arquivo:
    faturamento_diario = json.load(arquivo)

menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

dias_com_faturamento = [faturamento for faturamento in faturamento_diario if faturamento > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

dias_acima_da_media = len([faturamento for faturamento in faturamento_diario if faturamento > media_mensal])

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")