import json

DATA_FILE="campus_lands.json" #Ruta del archivo

#cargar los archivos desde el json
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data=json.load(file)
    except FileNotFoundError:
        data={
            "campers": [],
            "trainers": [],
            "coordinador": [],
            "rutas": [],
            "areas": [
                {"nombre":"Area 1", "ruta":None, "campers":[]},
                {"nombre":"Area 2", "ruta":None, "campers":[]},
                {"nombre":"Area 2", "ruta":None, "campers":[]}
            ],
            "matriculas": [],
            
            
            }
    return data

#guardar los archivos
def save_data(data):
    with open(DATA_FILE, 'w' ) as file:
        json.dump(data,file, indent=4)

    
#menu principal
while True:
    print("----Gestion Academica CampusLands----")
    print("")
    print("1. Registrar Camper")
    print("2. Registrar Trainer")
    print("3. Registar Coordinar")
    print("4. Crear ruta de entrenamiento")
    print("5. Registar notas de campers (coordinador)")
    print("6. Asignar campers y traines a rutas")
    print("7. Generar reportes")
    print("8. Gestionar matriculas")
    print("9. Salir")
    print("")

    opcion = int(input("Eliga un numero del 1 al 9: "))
    print("")

    if opcion == 1: #crear camper
        camper = {
            "# de Identificacion" : int(input("Ingrese el numero de CC o TI del camper: ")),  
            "nombres" : input("Ingrese el nombre del camper: "),
            "apellidos" : input("Ingrese el apellido del camper: "),
            "direccion" : input("Ingrese la dirección del camper: "),
            "acudiente" : input("Ingrese nombre del acudiente del camper: "),
            "Fijo" : int(input("Ingrese el numero de fijo del camper: ")),
            "Telefono" : int(input("Ingrese el numero de telefono del camper:")),
            "estado" : input("Ingrese el estado del camper: (ingreso): "),
            "riesgo" : input("ingrese el riesgo del camper: (bajo): "), 
        }
        data = load_data()
        data["campers"].append(camper)
        save_data(data)
        print("")
        print("Camper creado!!")
        print("")

    elif opcion == 2: #registrar un nuevo trainer
        trainer={
           "# de Identificacion" : int(input("Ingrese el numero de CC del Trainer: ")),
           "nombres" : input("Ingrese el nombre del Trainer: "),
           "apellidos" : input("Ingrese el apellido del Trainer: "),
           "rutas_asignadas":[]
        }
        data = load_data()
        data["trainers"].append(trainer)
        save_data(data)
        print("")
        print("Trainer creado!!")
        print("")
    
    elif opcion == 3: #registrar un nuevo coordinador
        coordinador={
           "# de Identificacion" : int(input("Ingrese el numero de CC del Coordinador: ")),
           "nombres" : input("Ingrese el nombre del Coordinador: "),
           "apellidos" : input("Ingrese el apellido del Coordinador: "),
        }
        data = load_data()
        data["coordinador"].append(coordinador)
        save_data(data)
        print("")
        print("Coordinador creado!!")
        print("")
    
    elif opcion == 4: #crear nueva ruta de entrenamiento
        ruta_nombre=input("Ingrese el nombre de la ruta (NodeJS, Java, NetCore): ")
        if ruta_nombre.lower() in ["nodejs","java","netcore"]:
            ruta={
                "nombre": ruta_nombre.lower(),
                "modulos":[]
            }
            modulos = ["Fundamentos de programacion","Programacioon Web","Programacioon formal","Bases de datos","Backend"]
            print("""- Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)
- Programación Web (HTML, CSS y Bootstrap).
- Programación formal (Java, JavaScript, C#).
- Bases de datos (Mysql, MongoDb y Postgresql).
- Backend (NetCore, Spring Boot, NodeJS y Express).
""")
            for modulo in modulos:
                print(f"Configurando modulo: {modulo}")
                detalle_modulo={
                    "nombre": modulo,
                    "contenido": input(f"Ingrese el contenido del modulo '{modulo}':")
                }
                ruta["modulos"].append(detalle_modulo)
            data = load_data()
            data["rutas"].append(ruta)
            save_data(data)
            print("")
            print("Ruta de entrenamiento creada!")
            print("")
        else:
            print("Ruta de entrenamiento no valida. Las opciones validas son: NodeJS, Java, NetCore.")

    elif opcion == 5: #registrar la nota de los campers
        data = load_data()
        campers=data["campers"]
        coordinador=data["coordinador"]

        if not coordinador:
            print("No hay coordinador registrado")
        else:
            print(f"Binvenido, coordinador {coordinador['nombres']} {coordinador['apellidos']}")
            #print("Binvenido, coordinador" coordinador["# de Identificacion"], coordinador["nombres"], coordinador["apellidos"] )
            for camper in campers:
                if camper['estado'] == "ingreso":
                    nota_teorica=float(input(f"Ingrese la nota teorica del camper{camper['nombres']} {camper['apellidos']}: "))
                    nota_practica=float(input(f"Ingrese la nota practica del camper{camper['nombres']} {camper['apellidos']}: "))
                    promedio = (nota_teorica * 0.3) + (nota_practica * 0.6)
                    if promedio >= 60:
                        camper["estado"] = "Aprobado"
                    else: 
                        camper["estado"] = "Inscrito"
                    camper["nota_final"] = promedio
            save_data(data)
            print("")
            print("Notas registradas !!")
            print("")
            break

    

    

        
    
            
#hecho por jaime barrera cc 1093925253 
    


#fechas de subidas (NO BORRAR)
#1 28-04-2024       10:00 pm    (por Jaime Barrera)
#2 30-04-2024       12:45 pm    (por Jaime Barrera)

#COSAS POR ARREGLAR #1 Como quitar las comas al final de leer. SOLUCIONADO