            #IF Statement - Examples.
homem = True
alto = True

if homem and alto:
    print("você é um homem alto")
elif homem and not (alto):
    print('você é um homem baixo')
elif not (homem) and alto:
    print('voce é uma mulher alta')
else:
    print('voce não é mulher e nem alta')

#-------------------------------------------#

            #Calculadora. 
num1 = float(input('digite o primeiro numero: '))
op = input('digite o operador: ')
num3 = float(input('digite o terceiro numero: '))

if op == '+':
    print(num1+num3)
elif op == '-':
    print(num1 - num3)
elif op == '*':
    print(num1 * num3)
elif op == '/':
    print(num1 / num3)
else:
    print('operador invalido.')