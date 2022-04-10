preço_base_areia = 34.00
preço_base_pedrita = 42.50
preço_base_brita = 28.00
preço_base_saibro = 27.00

produto = str(input('Digite o tipo de produto: '))
comp = str(input('Digite o tipo da composição: '))
quantidade = float(input('Digite a quantidade vendida: '))

if produto =='A' and comp =='F':
    preço_final = preço_base_areia
    valor_venda = preço_base_areia * quantidade
elif produto == 'A' and comp == 'M':
    areia_media = preço_base_areia * 1.15
    preço_final = areia_media
    valor_venda = areia_media * quantidade
elif produto =='A' and comp =='G':
    areia_grossa = preço_base_areia * 1.25
    preço_final = areia_grossa
    valor_venda = areia_grossa * quantidade
if produto =='P' and comp =='F':
    preço_final = preço_base_pedrita
    valor_venda = preço_base_pedrita * quantidade
elif produto == 'P' and comp == 'M':
    pedrita_media = preço_base_pedrita * 1.15
    preço_final = pedrita_media
    valor_venda = pedrita_media * quantidade
elif produto == 'P' and comp == 'G':
    pedrita_grossa = preço_base_pedrita * 1.25
    preço_final = pedrita_grossa
    valor_venda = pedrita_grossa * quantidade
if produto == 'B' and comp =='F':
    preço_final = preço_base_brita
    valor_venda = preço_base_brita * quantidade
elif produto == 'B' and comp == 'M':
    brita_media = preço_base_brita * 1.15
    preço_final = brita_media
    valor_venda = brita_media * quantidade
elif produto == 'B' and comp == 'G':
    brita_grossa = preço_base_brita * 1.25
    preço_final = brita_grossa
    valor_venda = brita_grossa * quantidade
if produto == 'S' and comp =='F':
    preço_final = preço_base_saibro
    valor_venda = preço_base_saibro * quantidade
elif produto == 'S' and comp == 'M':
    saibro_media = preço_base_saibro * 1.15
    preço_final = saibro_media
    valor_venda = saibro_media * quantidade
elif produto == 'S' and comp == 'G':
    saibro_grosso = preço_base_saibro * 1.25
    preço_final = saibro_grosso
    valor_venda = saibro_grosso * quantidade

if valor_venda < 750.00:
    valor_venda = valor_venda + 45.00

print(f'O preço final do produto é de R$%.2f' % (preço_final))
print(f'O valor da venda é de R$%.2f' % (valor_venda))