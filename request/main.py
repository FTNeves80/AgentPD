import requests

url = "https://api.github.com/users/FTNeves80/repos"
response = requests.get(url)
print(f"Status Code: {response.status_code}\n\n")
#print(f"Response text: {response.text}\n\n")
print(f"Response json: {response.json()[0]}\n\n")

# Print first 100 characters of the response content


if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print(f"Nome: {repo['name']} \nURL: {repo['html_url']}\n")
else:
    print(f"Erro ao acessar a API: {response.status_code}")
