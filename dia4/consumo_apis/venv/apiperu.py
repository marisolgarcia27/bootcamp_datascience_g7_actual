import requests

TOKEN = 'f3250cee2540cd28175f0ea0d226279be5e06f61e8583f15e544d70d14f52b6d'
API_URL = 'https://apiperu.dev/api/ruc'

ruc = input('INGRESE NRO DE RUC : ')

data_request = {
    "ruc":ruc
}

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(API_URL,
                         json=data_request,
                         headers=headers)

if response.status_code == 200:
    data = response.json()['data']
    print(f"RUC : {ruc}")
    print(f"Razón social : {data['nombre_o_razon_social']}")
    print(f'Dirección : {data["direccion"]}')
    print(f'Distrito : {data["distrito"]}')
    print(f'Provincia : {data["provincia"]}')
    print(f'Departamento : {data["departamento"]}')
    print(f'ubigeo : {data["ubigeo_sunat"]}')
    