        #Lógica de programação.

# 01-) Abrir os seis arquivos em Excel.
# 02-) Para cada um dos arquivos:
# 03-) Analisar se algum valor na coluna VENDAS do arquivo é maior que 55.000.
# 04-) Se o valor da coluna VENDAS for maior do que 55.000, então o programa deve me enviar um SMS com o nome, o mês e as VENDAS do VENDEDOR.
# 05-) Se o valor da coluna VENDAS não for maior do que 55.000, então o programa não deve fazer nada.

#Bibliotecas utilizadas no projeto.
import pandas as pd
from twilio.rest import Client

#Desenvolvimento do projeto.
account_sid = "AC73ffa6a23ed2046a6cd7975fffcd33ef"
auth_token  = "ed27527bdf84ba9a260a9ea37b7fd18b"
client = Client(account_sid, auth_token)
lista_analisados = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_analisados:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} algum vendedor bateu a meta. O nome do vendedor é {vendedor} e o valor das vendas dele é de {vendas} reais.')
        message = client.messages.create(
            to="+5515988184850",
            from_="+19034818087",
            body="Esse é um SMS enviado para teste que será colocado no README.md do projeto chamado Python-AnaliseDadosSMS. Olá, GitHub :D")
        print(message.sid)