print('@johanPosada\n')
print('No indique unidades')

class Figuras:
    def triangulo(self):
        b = int(input('Inserte base: '))
        h = int(input('Inserte altura: '))
        print(f"\nEl area del triangulo es: {(b*h)/2}")
        
    def circulo(self):
        r = int(input('Inserte el radio: '))
        pi = 3.1416
        print(f"\nEl area del círculo es: {pi*(r**2)}")

    def cuadrado(self):
        l = int(input("Inserte el valor del lado: "))
        print(f"El area del cuadrado es: {l**2}")

    def rectangulo(self):
        l1 = int(input("Inserte el valor para el lado 1"))
        l2 = int(input("Inserte el valor para el lado 2"))
        print(f"El area del rectángulo es: {l1 * l2}")
        
figuras_lista = ['triangulo', 'circulo', 'cuadrado', 'rectangulo']
print(f"Las figuras disponibles son: {figuras_lista}\n")

while True:
    try:
        figura = input('Inserte la figura ~ ')
    except Exception as e:
        print(e)
    if figura not in figuras_lista:
        print('Debe estar en las figuras disponibles')
        continue
    else:
        break

#El valor de la variable figura se toma para llamar al método de la clase Figuras()
exec(f"callClass = Figuras().{figura}")
callClass()
