import requests

try:
    # Faz uma requisição para a API de usuários aleatórios
    response = requests.get('https://randomuser.me/api/')
    response.raise_for_status()  # Verifica se houve erro na resposta
    
    # Converte a resposta para JSON
    data = response.json()
    
    # Extrai os dados do usuário
    user = data['results'][0]
    name = f"{user['name']['first']} {user['name']['last']}"
    email = user['email']
    country = user['location']['country']
    
    # Exibe os dados
    print(f"Nome: {name}")
    print(f"E-mail: {email}")
    print(f"País: {country}")
    
except requests.exceptions.RequestException as e:
    # Em caso de erro na conexão
    print("Erro na conexão: Falha ao acessar a API.")
