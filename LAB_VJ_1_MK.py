import requests
# 2. Zadatak
"""
response = requests.get('http://192.168.83.5/login')
print(response.text)
print(response.status_code)

for k, v in response.headers.items():
    print(f'{k}: {v}') 
"""

# 3. Zadatak
"""
ispravni_podaci = {
    'username': 'PURS',
    'password': '1234'
}

response = requests.post('http://192.168.83.5/login', json=ispravni_podaci)

print(response.text)
print(response.status_code)

neispravni_podaci = {
    'username': 'PURS',
    'password': 1234
}

response = requests.post('http://192.168.83.5/login', json=neispravni_podaci)

print(response.text)
print(response.status_code)
"""

# 4. Zadatak
"""
response = requests.get('http://192.168.83.5/temperatura')

if response.headers.get('Content-type') == 'application/json':
    print(response.json().get('temperatura'))
"""
# 5. Zadatak
"""
nova_temperatura = {
    'temperatura' : '21'
}

response = requests.post('http://192.168.83.5/temperatura', json=nova_temperatura)

print(response.text)
print(response.status_code)
"""

# 6. Zadatak
"""
payload = {
    'id': 45
}

response = requests.delete('http://192.168.83.5/temperatura', params=payload)
print(response.text)
print(response.status_code)
"""

# 7. Zadatak
"""
response = requests.get('https://api.ipify.org/?format=json')
print(response.json())
print(response.text)
print(response.json().get('ip'))
"""