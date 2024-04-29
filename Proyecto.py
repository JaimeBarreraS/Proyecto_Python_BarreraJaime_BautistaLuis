import json

DATA_FILE="Campers.json" #Ruta del archivo

#cargar los archivos desde el json
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data=json.load(file)
    except FileNotFoundError:
        data=[]
    return data

#guardar los archivos
def save_data(data):
    with open(DATA_FILE, 'w' ) as file:
        json.dump(data,file, indent=4)

    
#menu 
while True:
    print("--------Campers-------")
    print("")
    print("1. Crear campers")
    print("2. Leer Campers")
    print("3. Actualizar Campers")
    print("4. Eliminar Campers")
    print("5. Salir")
    print("")
    
    opcion = int(input("Eliga un numero del 1 al 5: "))
    print("")

    if opcion == 1: #crear camper
        camper = {
            "id" : int(input("Ingrese el numero de ID del camper: ")),  
            "nombre" : input("Ingrese el nombre del camper: "),
            "apellido" : input("Ingrese el apellido del camper: "),
            "direccion" : input("Ingrese la dirección del camper: "),
            "acudiente" : input("Ingrese nombre del acudiente del camper: "),
            "telefono" : int(input("Ingrese el numero de telefono del camper: (celular o fijo): ")),
            "estado" : input("Ingrese el estado del camper: (ingreso, inscrito, aprobado, cursando, graduado, expulsado, retirado): "),
            "riesgo" : input("ingrese el riesgo del camper: (alto, medio, bajo): "), #supongo que eso se refiere a riesgo
        }
        data = load_data()
        data.append(camper)
        save_data(data)
        print("")
        print("Camper creado!!")
        print("")
        
    elif opcion == 2: #leer campers 
        data = load_data()
        for camper in data:
            print(f"ID: {camper['id']}")
            print(f"Nombre: {camper['nombre']}")
            print(f"Apellido: {camper['apellido']}")
            print(f"Direccion: {camper['direccion']}")
            print(f"Acudiente: {camper['acudiente']}")
            print(f"Telefono: {camper['telefono']}")
            print(f"Estado: {camper['estado']}")
            print(f"Riesgo: {camper['riesgo']}")
            print("----------------------------------")
    
    elif opcion == 3: #actualizar campers
        for camper in data:
            print(f"{camper['id']}")

        camper_id = int(input("Ingrese el ID del camper para actualizar: "))
        data = load_data()
        for camper in data:
            print("")
            if camper['id'] == camper_id: #compara si el id ingresado con el id guardado
                 print("")
                 camper ['nombre'] = input("Ingrese el nombre del camper: ")
                 camper ['apellido'] = input("Ingrese el apellido del camper: ")
                 camper ['direccion'] = input("Ingrese la dirección del camper: ")
                 camper ['acudiente'] = input("Ingrese nombre del acudiente del camper: ")
                 camper ['telefono'] = int(input("Ingrese el numero de telefono del camper: (celular o fijo): "))
                 camper ['estado'] = input("Ingrese el estado del camper: (ingreso, inscrito, aprobado, cursando, graduado, expulsado, retirado): ")
                 camper ['riesgo'] = input("ingrese el riesgo del camper: (alto, medio, bajo): ")
                 save_data(data)
                 print("")
                 print("Camper actualizado!!")
                 break
    
    elif opcion == 4: #eliminar camper
        for camper in data:
            print(f"{camper['id']}")

        camper_id=int(input("Ingrese el ID del camper para eliminar: "))
        data = load_data()
        for i, camper in enumerate(data):
            print("")
            if camper['id'] == camper_id: 
                del data[i]
                save_data(data)
                print("")
                print("Camper eliminado!!")

    elif opcion == 5:
        break 

    #hecho por jaime barrera cc 1093925253 
    


#fechas de subidas (NO BORRAR)
#1 28-04-2024       10:00 pm    (por Jaime Barrera)

#COSAS POR ARREGLAR 
#1 Como quitar las comas al final de leer. SOLUCIONADO
