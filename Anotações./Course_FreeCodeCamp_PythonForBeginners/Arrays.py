            #Listas - Examples.
friends = ["Kevin", "Karen", "Jim", "Andrew", "Tom", "Tobey"]
print(friends[1:])

#-------------------------------------------#

            #Inserindo o bill no lugar da Kelly, dessa forma, empurrando todos para frente. - Examples.
amigos = ["Kevin", "Karen", "Jim", "Andrew", "Tom", "Tobey"]
amigos.insert(1,'Bill')
print(amigos)

#-------------------------------------------#

            #Removendo algum item da lista - Examples.
amigos = ["Kevin", "Jim", "Andrew", "Tom", "Tobey"]
amigos.remove('Jim')
print(amigos)

#-------------------------------------------#

            #Localizando o item na lista - Examples.
amigos = ["Kevin", "Jim", "Andrew", "Tom", "Tobey"]
print(amigos.index("Tobey"))

#-------------------------------------------#

            #Contando o número de vezes de um item na lista - Examples.
amigos = ["Kevin", "Jim", "Andrew", "Tom", "Tobey", "Tobey"]
print(amigos.count("Tobey"))

#-------------------------------------------#

            #Deixando a lista em ordem alfabética - Examples.
amigos = ["Kevin", "Jim", "Andrew", "Tom", "Tobey"]
amigos.sort()
print(amigos)