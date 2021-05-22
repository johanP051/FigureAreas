import os

print('@johanPosada')

E = 'No indique unidades, debe ser entero o decimal'

def triangulo():
    while True:
        try:
            b, h = float(input('Inserte valor para b: ')), float(input('Inserte valor para b: '))
        except ValueError:
            print(E)
            continue
        else:
            break
    print(f"\nEl area del Triángulo es: {(b*h)/2}")

def cuadrado():
    while True:
        try:
            l = float(input('Inserte valor para l: '))
        except ValueError:
            print(E)
            continue
        else:
            break
            
    print(f"\nEl area del Cuadrado es: {l**2}")
    
def rectangulo():
    while True:
        try:
            l, l2 = float(input('Inserte valor para l: ')), float(input('Inserte valor para l2: '))
        except ValueError:
            print(E)
        else:
            break
    print(f"\nEl area del Rectángulo es: {l * l2}")
    
def circulo():
    while True:
        try:
            r = float(input('Inserte valor para el radio: '))
        except ValueError:
            print(E)
            continue
        else:
            break
    print(f"\nEl area del Circulo es: {3.1416 * (r**2)}")
    
figuras = ['triangulo', 'cuadrado', 'rectangulo', 'circulo' ]
print(figuras)

while True:
    try:
        figura = input('Inserte la figura que desea: ')
        figura = figura.lower()
    except ValueError:
        continue
    if figura not in figuras:
        print('Las figuras son:', figuras)
        continue
    else:
        break
        
if figura == 'triangulo':
    triangulo()
elif figura == 'cuadrado':
    cuadrado()
elif figura == 'rectangulo':
    rectangulo()
else:
    circulo()

while True:
    try:
        exec_ = input('¿Quiere continuar? S/n ~ ')
    except ValueError:
        print('Deben ser carácteres')
        continue
    if exec_ == '':
        print('Inserte algo')
        continue
    else:
        break

if exec_ == 'S' or exec_ == 's':
    os.system('python3 ' + __file__)
else:
    print('Bye!')