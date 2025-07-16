nome=input("Digite um nome:")

url = "https://api.agify.io?nome"
 
# Faz a requisição e guarda a resposta
resposta = requests.get(url)
 
 
# Converte a resposta para um dicionário
dados = resposta.json()
# Mostra o nome
print(f"Nome: {dados['name']}")
 
# Mostra a idade prevista
print(f"Idade estimada: {dados['age']}")