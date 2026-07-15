import os 
os.system("cls")

planes = { 
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'], 
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'], 
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'], 
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'], 
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],     'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'], ... } 

inscripciones = { 
    'F001': [14990, 30], 
    'F002': [22990, 10], 
    'F003': [39990, 0], 
    'F004': [35990, 6], 
    'F005': [159990, 2],'F006': [18990, 15], 
    ... 
}

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    try:
        opcion=int(input("Ingrese una opcion entre 1 y 6: "))
        if opcion>=1 and opcion<=6:
            return opcion
        else:
            print("Debes ingresar un valor entre 1 y 6.")
    except ValueError:
        print("Debes ingresar un valor valido.")


def cupos_tipo(tipo, planes, incripciones):
    cupos=0
    for codigo, plan in planes.items():
        if plan [0].strip().lower()==tipo.strip().lower():
            cupos+= incripciones[plan][1]
            print(f"El total de cupos disponibles es: {cupos}")

def busqueda_preio(p_min, p_max, inscripciones):
    lista=[]
    for codigo, plan in planes.items():
        if plan [0]>=p_min and plan[0]<=p_max and plan[1] !=0:
            tipo=inscripciones[codigo][0]
            lista.append(f"{tipo}--{plan}")
            lista.sort()
            return lista
        
def buscar_codigo(codigo, inscripciones):
    if codigo in inscripciones:
        return True
    else:
        return False
    
def agregar_plan():
    

def actualizar_precio(codigo, planes, inscripciones):
    if buscar_codigo==False:
        return False
    else:
        inscripciones[codigo][0]=precio
        return True




while True:
    menu()
    opcion=leer_opcion
    if opcion ==1:
        print("")
    elif opcion ==2:
        print("")
    elif opcion ==3:
        print("")
    elif opcion ==4:
        print("")
    elif opcion ==5:
        print("")
    elif opcion ==6:
        print("Saliendo del Programa")
        break