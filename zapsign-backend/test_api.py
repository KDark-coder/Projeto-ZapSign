import requests

# URL do endpoint
url = "http://localhost:8000/api/analyze/"

# Seu token de autenticação
headers = {
    "Authorization": "Token 50a3c5a4722ab8ba4ab6e1d47f6265de16acfa1a"
}

# Teste com um PDF válido
data = {
    "pdf_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
}

response = requests.post(url, headers=headers, json=data)
print("Status code:", response.status_code)
print("Resposta:", response.json())