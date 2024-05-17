mi_diccionario = {}
pendiente = []
import os

def fnt_agregar(apellidos, nombres, contacto ,edad ,extracto ,sexo, direcciones):
    if sexo.lower() == 'm':
        if 15 <= int(edad) <= 24 and 1 <= int(extracto) <= 2:
            mi_diccionario[apellidos] = {'nombre': nombres, 'contacto': contacto, 'edad': edad, 'extracto': extracto, 'sexo': sexo, 'direcciones': direcciones}
            enter = input(f'\nLa persona {nombres} ha sido registrada con éxito <ENTER>')
        else:
            pendiente.append(contacto)
    elif sexo.lower() == 'f':
        if 20 <= int(edad) <= 35 and 1 <= int(extracto) <= 4:
            mi_diccionario[apellidos] = {'nombre': nombres, 'contacto': contacto, 'edad': edad, 'extracto': extracto, 'sexo': sexo, 'direcciones': direcciones}
            enter = input(f'\nLa persona {nombres} ha sido registrada con éxito <ENTER>')
        else:
            pendiente.append(contacto)
    else:
        pendiente.append(contacto)
        enter = input('\nNo cumple con los criterios de registro <ENTER>')
        
def fnt_selector():
    opcion = input('\n1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    return opcion
        
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    opcion = fnt_selector()
    if opcion == '1':
        apellidos = input('Apellidos: ')
        nombre = input('Nombre: ')
        contacto = input('Contacto: ')
        edad = input('Edad: ')
        extracto = input('Extracto: ')
        sexo = input("Sexo [M/F]: ")
        direccion = input('Dirección: ')
        fnt_agregar(apellidos, nombre, contacto, edad, extracto, sexo, direccion)
    elif opcion == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nCantidad de registros:', len(mi_diccionario), '\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        if pendiente:
            print('\nContactos pendientes de registro:')
            for contacto in pendiente:
                print(contacto)
        input('\nPresione ENTER para continuar...')
    elif opcion == '3':
        break