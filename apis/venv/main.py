import requests
from tabule import tabulate
url='https://randomuser.me/api/?results=10'
respone = requests.get(url)
print(f'codigo de respone : {respone.status_code}')
#print(f'contenido : {respone.json()}')
if respone.status_code == 200:
    data = respone.json()
    lista_usuarios = []
    for u in data['results']:
            nombre=u['name']['first']+ ' '+u['name']['last']
            pais=u['location']['country']
            correo=u['email']
            telefono=u['phone']
            foto=u['picture']['large']
            lista_usuarios.append([nombre,pais,correo,telefono,foto])
    headers = ['Nombre', 'Pais', 'Correo', 'Telefono', 'Foto']
    print(tabulate(lista_usuarios, headers=headers, tablefmt='grid'))
else:
    print(f'algo salio mal : {respone.status_code}')  