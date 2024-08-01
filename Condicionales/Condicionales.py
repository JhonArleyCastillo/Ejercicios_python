#Condicionales simples
'''temperature = 40

if temperature > 35:
    print('Aviso por alta temperatura')'''
    
'''temperature = 20

if temperature > 35:
    print('Aviso por alta temperatura')
else:
    print('Parámetros normales')'''

#Condicionales anidados    
'''temperature = 28

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperature < 30:
        print('Nivel naranja')
    else:
        print('Nivel rojo')'''
        
'''temperature = 28

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
elif temperature < 30:
    print('Nivel naranja')
else:
    print('Nivel rojo')'''
    
    
'''temperature = 35

if temperature < 30:
    fire_risk = 'LOW'
else:
    fire_risk = 'HIGH'

print (fire_risk)'''

#match-case
'''point = (2, 5)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')

point = (3, 1, 7)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')'''

# Lista de diccionarios
auths = [
    {'username': 'sdelquin', 'password': '1234'},
    {'email': 'sdelquin@gmail.com', 'token': '4321'},
    {'email': 'test@test.com', 'password': 'ABCD'},
    {'username': 'sdelquin', 'password': 1234}
]

for auth in auths:
    print(auth)
    match auth:
        case {'username': str(username), 'password': str(password)}:
            print('Authenticating with username and password')
            print(f'{username}: {password}')
        case {'email': str(email), 'token': str(token)}:
            print('Authenticating with email and token')
            print(f'{email}: {token}')
        case _:
            print('Authenticating method not valid!')
    print('-_--')