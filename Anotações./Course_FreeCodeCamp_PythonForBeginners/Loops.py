            #While Loops - Examples.
x = 10
while x <= 100:
    print(x)
    x +=1
print('finish')

#-------------------------------------------#

            #Jogo de adivinhação.
palavra_secreta = 'Corinthians'
palpite = ''
contagem_palpite = 0
limite_palpite = 3
fora_palpite = False

while palpite != palavra_secreta and not (fora_palpite):
    if contagem_palpite < limite_palpite:
        palpite = input('Digite seu palpite: ')
        contagem_palpite += 1
    else:
        fora_palpite = True

if fora_palpite:
    print('Desculpa, você perdeu!')
else:
    print('Parabéns, você venceu!')

#-------------------------------------------#

            #For Loops - Examples.
friends = ['Jim', 'Karen', 'Kevin']
for friend in friends:
    print(friend)

#-------------------------------------------#