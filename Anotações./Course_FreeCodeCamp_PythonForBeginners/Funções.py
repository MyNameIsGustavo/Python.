            #Funções - Examples.
def ola_mundo (nome, idade):
    print(f"Hello, {nome}. Você tem {idade}")
ola_mundo("mike", "18 anos")
ola_mundo("Steve", "23 anos")
ola_mundo("Tony", "31 anos")
ola_mundo("Elon", "20 anos")

#-------------------------------------------#

            #Return.
def cube (num):
    return num*num*num
print(cube(5))

#-------------------------------------------#

            #IF com funções - Examples.
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print((max_num(300,500,10)))

#-------------------------------------------#

            #Função expoente.
def raise_to_power (base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3, 4))