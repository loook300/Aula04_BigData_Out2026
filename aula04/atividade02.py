salario = float (input ('informe seu salario : '))

venda = float (input("informe da venda : "))

if venda >= 1000 :
    venda = 150
    print (f'Parabens seu bonus e de: R$ {venda}')
    salario = salario +150 
    print (f'Seu salario é : R$ {salario}')

elif venda >= 500 :
    venda =  75
    print (f'Parabens seu bonus e de: R$ {venda}')
    salario = salario + 75
    print (f'Seu salario é : R$ {salario}')

else: 
    venda < 500 
    print ('Você nao Obteve Bonus !')