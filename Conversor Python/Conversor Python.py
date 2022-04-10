            #Apresentação e tomada de decisão.

print('1-) Bem-vindo, eu sou um conversor de bases numéricas!')
github = str(input('2-) Antes de começarmos, por favor digite o seu nome de usuário no GitHub: '))
nome = str(input('3-) Digite o seu nome: '))
sobrenome = str(input('4-) Entendi, agora digite o seu sobrenome: '))
apst = input(f'5-) Muito prazer, {nome} {sobrenome}. Vamos começar!')
decpoint = str(input(f'6-) {nome}, preciso saber qual vai ser o tipo da sua conversão. Essas são as opções disponíveis:'
f'\n  A- Decimal para binario \n  B- Decimal para Hexadecimal \n  C- Decimal para Octal.'
f'\n7-) Selecione a alternativa desejada: '))

            #Decisões e finalização.

if decpoint =='a' or  decpoint =='A':
    binary = int(input(f'8-) {nome}, digite o número que você deseja converter para Binario: '))
    binary = bin(binary)
    print(f'A sua resposta para essa conversão é: {binary [2::]}')
elif decpoint =='b' or decpoint=='B':
    hexa = int(input(f'8-) {nome}, digite o número que você deseja converter para Hexadecimal: '))
    hexa = hex(hexa).upper()
    print(f'A sua resposta para essa conversão é: {hexa [2::]}')
elif decpoint =='c' or decpoint=='C':
    octal = int(input(f'8-) {nome}, digite o número que você deseja converter para Octal: '))
    octal = oct(octal)
    print(f'A sua resposta para essa conversão é: {octal [2::]}')
print(f'9-) Terminamos!Volte sempre que precisar, {nome}. :D')