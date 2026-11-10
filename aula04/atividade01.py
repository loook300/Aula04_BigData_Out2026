compra = float (input ('informe o Valor da compra : '))

if compra >= 250 :
    valor_desc = compra * 0.16
    
    print(f'Valor do desconto e de R$:{valor_desc}')
    total = compra - valor_desc
    print(f'valor da compra {total}')

else:
    print(f'valor sem desconto : {compra}')

