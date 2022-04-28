            #Dicionarios - Examples.
teste_meses = {
    "Jan":"Janeiro",
    "Fev":"Fevereiro",
    "Mar":"Março",
    "Abr":"Abril",
    "Jun":"Junho",
    "Jul":"Julho",
    "Ago":"Agosto",
    "Set":"Setembro",
    "Out":"Outubro",
    "Nov":"Novembro",
    "Dez":"Dezembro"
}
print(teste_meses['Jan'])

#-------------------------------------------#

            #Tratando erros - Examples.
try:
    answer = 10/0
    number = int(input('Digite um numero: '))
    print('number')
except ZeroDivisionError as err:
    print(err)
except ValueError:
   print('Entrada invalida.')