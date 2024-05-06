import os # Importa el módulo para interactuar con el sistema operativo 
import json # Importa el módulo json para trabajar con archivos JSON
from colorama import Fore, Style # Importa las clases Fore y Style del módulo colorama para imprimir texto en colores

DATA_FILE="campus_lands.json" # Ruta del archivo JSON donde se almacenarán los datos

def limpiar(): # Función para limpiar la consola
    if os.name == 'nt': # Si el sistema operativo es Windows
        os.system('cls') # Ejecuta el comando 'cls' para limpiar la consola en Windows
    else: # Si el sistema operativo es diferente a Windows (por ejemplo, Linux o macOS)
        os.system('clear') # Ejecuta el comando 'clear' para limpiar la consola

#cargar los archivos desde el json
def cargar(): # Función para cargar los datos desde el archivo JSON
    try: # Intenta abrir el archivo JSON
        with open(DATA_FILE, 'r') as file: # Abre el archivo en modo lectura
            data=json.load(file) # Carga los datos del archivo JSON
    except FileNotFoundError: # Si el archivo no existe
        data={  # Crea un diccionario con los datos iniciales
            "campers": [],
            "trainers": [],
            "coordinador": [],
            "rutas": [],
            "areas": [
                {"nombre":"Area 1", "capacidad_maxima":33, "ruta":None, "campers":[]},  
                {"nombre":"Area 2", "capacidad_maxima":33, "ruta":None, "campers":[]},
                {"nombre":"Area 3", "capacidad_maxima":33, "ruta":None, "campers":[]}
            ],
            "matriculas": [],
        }
    return data # Devuelve los datos cargados o los datos iniciales

# Función para guardar los datos en el archivo JSON
def guardar(data):
    with open(DATA_FILE, 'w' ) as file: # Abre el archivo en modo escritura
        json.dump(data,file, indent=4) # Guarda los datos en el archivo JSON con una indentación de 4 espacios

def decimal(prompt): # Función para solicitar un número decimal al usuario
    while True:
        try:
            value = float(input(prompt))# Solicita un número decimal al usuario
            return value # Devuelve el valor ingresado si es válido
        except ValueError:
            print(Fore.RED + "Entrada inválida. Ingrese un número decimal." + Style.RESET_ALL) # Muestra un mensaje de error si la entrada no es válida

def enteros(prompt): # Función para solicitar un número entero al usuario
    while True:
        try:
            value = int(input(prompt)) # Solicita un número entero al usuario
            return value # Devuelve el valor ingresado si es válido
        except ValueError:
            print(Fore.RED + "Entrada inválida. Ingrese un número entero." + Style.RESET_ALL) # Muestra un mensaje de error si la entrada no es válida

def instrucciones(): # Función para imprimir las instrucciones de uso del programa
    print(Fore.YELLOW + "Instrucciones de uso:" + Style.RESET_ALL)
    print("1. Selecciona una opcion del menú ingresando el número correspondiente.")
    print("2. Sigue las instrucciones en pantalla para completar la acción seleccionada.")
    print("3. Para salir del programa, selecciona la opcion 0.")
    print("")


# Menú principal
while True:
    limpiar() # Limpia la consola
    instrucciones() # Imprimir las instrucciones en la consola
    print(Fore.GREEN + "==== Gestion Academica CampusLands ====" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Registrar Camper" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Registrar Trainer" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Registar Coordinador" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. Crear ruta de entrenamiento" + Style.RESET_ALL)
    print(Fore.YELLOW + "5. Registar notas de campers (coordinador)" + Style.RESET_ALL)
    print(Fore.YELLOW + "6. Asignar campers y traines a rutas" + Style.RESET_ALL)
    print(Fore.YELLOW + "7. Generar reportes" + Style.RESET_ALL)
    print(Fore.YELLOW + "8. Gestionar matriculas" + Style.RESET_ALL)
    print(Fore.YELLOW + "9. Seleccionar horario de trainers" + Style.RESET_ALL)
    print(Fore.RED + "0. Salir" + Style.RESET_ALL)
    print("")

    opcion = enteros(Fore.GREEN + "Eliga una opcion: " + Style.RESET_ALL) # Solicita al usuario que ingrese una opción del menú
    print("-------------------------------")

    if opcion == 0:  # Si la opción es 0, salir del programa
        print(Fore.GREEN + "¡Hasta Luego!" + Style.RESET_ALL)
        break

    elif opcion == 1: # Si la opción es 1, registrar un nuevo camper
        print(Fore.YELLOW + "=== Registrar Camper ===" + Style.RESET_ALL)
        camper = {
            "# de Identificacion" : enteros("Ingrese el numero de CC o TI del camper: "),  
            "nombres" : input("Ingrese el nombre del camper: "),
            "apellidos" : input("Ingrese el apellido del camper: "),
            "direccion" : input("Ingrese la dirección del camper: "),
            "acudiente" : input("Ingrese nombre del acudiente del camper: "),
            "Fijo" : enteros("Ingrese el numero de fijo del camper: "),
            "Telefono" : enteros("Ingrese el numero de telefono del camper: "),
            "estado" : "ingreso",
            "riesgo" : "bajo"
        }
        data = cargar() # Carga los datos existentes
        data["campers"].append(camper) # Agrega el nuevo camper a la lista de campers
        guardar(data) # Guarda los datos actualizados
        print(Fore.GREEN + "Camper creado exitosamente." + Style.RESET_ALL)
        input("Presiona Enter para continuar...")

    elif opcion == 2: # Si la opción es 2, registrar un nuevo trainer
        print(Fore.YELLOW + "=== Registrar Trainer ===" + Style.RESET_ALL)
        trainer={
            "# de Identificacion" : enteros("Ingrese el numero de CC del Trainer: "),
            "nombres" : input("Ingrese el nombre del Trainer: "),
            "apellidos" : input("Ingrese el apellido del Trainer: "),
            "rutas_asignadas":[]
        }
        data = cargar() # Carga los datos existentes
        data["trainers"].append(trainer) # Agrega el nuevo trainer a la lista de trainers
        guardar(data) # Guarda los datos actualizados
        print(Fore.GREEN + "Trainer creado exitosamente." + Style.RESET_ALL)
        input("Presiona Enter para continuar...")
    
    elif opcion == 3: # Si la opción es 3, registrar un nuevo coordinador
        print(Fore.YELLOW + "=== Registrar Coordinador ===" + Style.RESET_ALL)
        coordinador={
            "# de Identificacion" : enteros("Ingrese el numero de CC del Coordinador: "),
            "nombres" : input("Ingrese el nombre del Coordinador: "),
            "apellidos" : input("Ingrese el apellido del Coordinador: "),
        }
        data = cargar() # Carga los datos existentes
        data["coordinador"] = coordinador  # Asigna el diccionario del coordinador a la clave "coordinador"
        guardar(data) # Guarda los datos actualizados
        print(Fore.GREEN + "Coordinador creado exitosamente." + Style.RESET_ALL)
        input("Presiona Enter para continuar...")
    
    elif opcion == 4: # Si la opción es 4, crear una nueva ruta de entrenamiento
        print(Fore.YELLOW + "=== Crear Ruta de Entrenamiento ===" + Style.RESET_ALL)
        ruta_nombre=input("Ingrese el nombre de la ruta (NodeJS, Java, NetCore): ").lower()
        if ruta_nombre in ["nodejs","java","netcore"]: # Verifica si el nombre de la ruta es válido
            ruta={
                "nombre": ruta_nombre,
                "modulos":[]
            }
            modulos = [
                {"nombre": "Fundamentos de Programacion", "contenido": "Introducción a la algoritmia, PSeInt y Python"},
                {"nombre": "Programacion Web", "contenido": "HTML, CSS y Bootstrap"},
                "Programacion formal",
                "Base de datos",
                "Backend",
            ]
            print("""
- Programación formal (Java, JavaScript, C#).
- Bases de datos (Mysql, MongoDb y Postgresql).
- Backend (NetCore, Spring Boot, NodeJS y Express).
""")
            for modulo in modulos: # Itera sobre los módulos
                if isinstance(modulo, dict): # Si el módulo es un diccionario, lo agrega directamente a la ruta
                    ruta["modulos"].append(modulo)
                else: # Si el módulo es un string, solicita el contenido y lo agrega como un diccionario
                    print("---------------------------------------------------------")
                    print(Fore.YELLOW + f"Configurando módulo: {modulo}" + Style.RESET_ALL)
                    detalle_modulo={
                        "nombre": modulo,
                        "contenido":input(f"Ingrese el contenido del módulo '{modulo}': ")
                    }

                    ruta["modulos"].append(detalle_modulo)

            data=cargar() # Carga los datos existentes
            data["rutas"].append(ruta) # Agrega la nueva ruta a la lista de rutas
            guardar(data) # Guarda los datos actualizados
            print(Fore.GREEN + "Ruta de entrenamiento creada exitosamente." + Style.RESET_ALL)
            input("Presiona Enter para continuar...")
        else:
            print(Fore.RED + "Ruta de entrenamiento no valida. Las opciones validas son: NodeJS, Java, NetCore." + Style.RESET_ALL)
            input("Presiona Enter para continuar...")

    elif opcion == 5: # Si la opción es 5, registrar las notas de los campers
        data = cargar() # Carga los datos existentes
        campers=data["campers"]
        coordinador=data["coordinador"]

        if not coordinador: # Verifica si hay un coordinador registrado
            print(Fore.RED + "No hay coordinador registrado." + Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"Binvenido, coordinador {coordinador['nombres']} {coordinador['apellidos']}" + Style.RESET_ALL)
            print("==============================================================================")
            
            for camper in campers: # Itera sobre los campers
                if camper['estado'] == "ingreso": # Verifica si el camper está en estado "ingreso"
                    nota_teorica=decimal(f"Ingrese la nota teorica del camper {camper['nombres']} {camper['apellidos']}: ")
                    print("-------------------------------------------------------------------------------")
                    nota_practica=decimal(f"Ingrese la nota practica del camper {camper['nombres']} {camper['apellidos']}: ")
                    promedio = (nota_teorica * 0.3) + (nota_practica* 0.6)  # Calcula el promedio de las notas
                    if promedio >= 0.6: # Verifica si el promedio es mayor o igual a 0.6
                        camper["estado"] = "aprobado"
                    else: 
                        camper["estado"] = "inscrito"
                    camper["nota_final"] = promedio # Asigna el promedio como la nota final del camper
            guardar(data) # Guarda los datos actualizados
            print(Fore.GREEN + "Notas registradas exitosamente." + Style.RESET_ALL)
            input("Presiona Enter para continuar...")

    elif opcion == 6: # Si la opción es 6, asignar campers y trainers a rutas de entrenamiento
        data=cargar() # Carga los datos existentes
        campers=[c for c in data["campers"] if c["estado"] == "aprobado"] # Filtra los campers aprobados
        rutas=data["rutas"]
        areas=data["areas"]
        trainers=data["trainers"]

        for camper in campers: # Itera sobre los campers aprobados
            print(Fore.GREEN + f"Asignando ruta para el camper {camper['nombres']} {camper['apellidos']}" + Style.RESET_ALL)
            print("")
            for i, ruta in enumerate(rutas): # Muestra las rutas disponibles
                print(Fore.CYAN + f"{i+1}. {ruta['nombre']}" + Style.RESET_ALL)

            print("")
            opcion_ruta=enteros("Seleccione una ruta: ") # Solicita al usuario que seleccione una ruta
            ruta_seleccionada=rutas[opcion_ruta-1] # Obtiene la ruta seleccionada

            area_disponible=None
            for area in areas: # Itera sobre las áreas
                if area["ruta"] is None or (area["ruta"] == ruta_seleccionada["nombre"] and len(area["campers"]) < area["capacidad_maxima"]):
                    area_disponible = area # Encuentra un área disponible para la ruta seleccionada
                    break

            if area_disponible:
                area_disponible["ruta"]=ruta_seleccionada["nombre"]
                camper["ruta_asignada"]=ruta_seleccionada["nombre"]
                area_disponible["campers"].append(camper)  # Agrega el camper al área disponible
                print("---------------------------------------------------------------------------------")
                print(Fore.GREEN + f"El camper {camper['nombres']} {camper['apellidos']} ha sido asignado a la ruta {ruta_seleccionada['nombre']} en el area {area_disponible['nombre']}." + Style.RESET_ALL)

                trainer_disponible=None
                for trainer in trainers: # Itera sobre los trainers
                    if ruta_seleccionada["nombre"] not in trainer["rutas_asignadas"]:
                        trainer_disponible=trainer # Encuentra un trainer disponible para la ruta seleccionada
                        trainer["rutas_asignadas"].append(ruta_seleccionada["nombre"])
                        break

                if trainer_disponible:
                    print(Fore.GREEN + f"El trainer {trainer_disponible['nombres']} {trainer_disponible['apellidos']} ha sido asignado a la ruta {ruta_seleccionada['nombre']}." + Style.RESET_ALL)
                    print("---------------------------------------------------------------------------------")
                else:
                    print(Fore.RED + f"No hay trainers disponibles para asignar a la ruta {ruta_seleccionada['nombre']}." + Style.RESET_ALL)
            else: 
                print(Fore.RED + f"No hay areas disponibles para la ruta {ruta_seleccionada['nombre']}. El camper {camper['nombres']} {camper['apellidos']} no puede ser asignado." + Style.RESET_ALL)

        guardar(data) # Guarda los datos actualizados
        input("Presiona Enter para Continuar...")

    elif opcion == 7: # Si la opción es 7, generar reportes
        data=cargar() # Carga los datos existentes
        campers=data["campers"]
        trainers=data["trainers"]
        rutas=data["rutas"]

        print(Fore.YELLOW + "==== Modulo de Reportes ====" + Style.RESET_ALL)
        print("")
        print(Fore.CYAN + "1. Evaluar campers" + Style.RESET_ALL)
        print(Fore.CYAN + "2. Listar campers inscritos" + Style.RESET_ALL)
        print(Fore.CYAN + "3. listar campers aprobados" + Style.RESET_ALL)
        print(Fore.CYAN + "4. Listar trainers" + Style.RESET_ALL)
        print(Fore.CYAN + "5. Listar campers con bajo rendimiento" + Style.RESET_ALL)
        print(Fore.CYAN + "6. listar camper y trainers por ruta" + Style.RESET_ALL)
        print(Fore.CYAN + "7. mostrar estadisticas de modulos" + Style.RESET_ALL)
        print("")
        
        opcion_reporte=enteros("Eliga una opcion: ") # Solicita al usuario que seleccione una opción de reporte
        print("")

        if opcion_reporte == 1:  # Si la opción es 1, evaluar campers
            for ruta in rutas: # Itera sobre las rutas
                print(Fore.GREEN + f"Ruta: {ruta['nombre'].upper()}" + Style.RESET_ALL)
                for modulo in ruta["modulos"]: # Itera sobre los módulos de la ruta
                    print("")
                    print(Fore.YELLOW + f"Evaluando modulo {modulo['nombre']}" + Style.RESET_ALL)
                    print("====================================================")
                    for camper in campers: # Itera sobre los campers
                        if"ruta_asignada" in camper and camper["ruta_asignada"] == ruta["nombre"]:
                            nota_teorica=decimal(f"Ingrese la nota teorica del camper {camper['nombres']} {camper['apellidos']} para el modulo {modulo['nombre']}: ")
                            print("-------------------------------------------------------------------------------------------")
                            nota_practica=decimal(f"Ingrese la nota practica del camper {camper['nombres']} {camper['apellidos']} para el modulo {modulo['nombre']}: ")
                            print("-------------------------------------------------------------------------------------------")
                            promedio_pruebas=(nota_teorica * 0.3) + (nota_practica * 0.6) # Calcula el promedio de las pruebas
                            if promedio_pruebas >= 0.6:
                                estado_pruebas="aprobado"
                            else:
                                estado_pruebas="reprobado"
                            
                            quizes_trabajos = []
                            num_quizes_trabajos = enteros(f"Ingrese el numero de quices y trabajos del camper {camper['nombres']} {camper['apellidos']} para el modulo {modulo['nombre']}: ")
                            for i in range(num_quizes_trabajos): # Itera para ingresar las notas de los quices y trabajos
                                print("-------------------------------------------------------------------------------------------")
                                nota_quiz_trabajo = decimal(f"Ingrese la nota del quiz/trabajo {i+1}: ")
                                print("")
                                quizes_trabajos.append(nota_quiz_trabajo)
                            promedio_quizes_trabajos = sum(quizes_trabajos) / num_quizes_trabajos # Calcula el promedio de los quices y trabajos

                            nota_final = (promedio_pruebas * 0.9) + (promedio_quizes_trabajos * 0.1) # Calcula la nota final del módulo
                            if nota_final >= 0.6:
                                estado_final="aprobado"
                            else:
                                estado_final="reprobado"

                            camper[modulo['nombre']]={ # Asigna las notas y estados del módulo al camper
                                "nota_teorica": nota_teorica,
                                "nota_practica": nota_practica,
                                "promedio_pruebas": promedio_pruebas,
                                "estado_pruebas": estado_pruebas,
                                "quizes_trabajos": quizes_trabajos,
                                "promedio_quizes_trabajos": promedio_quizes_trabajos,
                                "nota_final": nota_final,
                                "estado_final": estado_final
                            }
            guardar(data) # Guarda los datos actualizados
            print(Fore.GREEN + "Evaluacion de campers completada." + Style.RESET_ALL)
            input("Presione Enter para continuar...")

        elif opcion_reporte == 2: # Si la opción es 2, listar campers inscritos
            campers_inscritos = [c for c in campers if c["estado"] == "inscrito"] # Filtra los campers inscritos
            if campers_inscritos:
                print(Fore.YELLOW + "Campers inscritos:" + Style.RESET_ALL)
                print("---------------------")
                for c in campers_inscritos: # Muestra los campers inscritos
                    print(Fore.CYAN + f"* {c['nombres']} {c['apellidos']}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No hay campers inscritos" + Style.RESET_ALL)
            input("Presione Enter para continuar...")

        elif opcion_reporte == 3: # Si la opción es 3, listar campers aprobados
            print("")
            campers_aprobados = [c for c in campers if c["estado"] == "aprobado"] # Filtra los campers aprobados
            if campers_aprobados:
                print(Fore.YELLOW + "Campers aprobados:" + Style.RESET_ALL)
                print("---------------------")
                for c in campers_aprobados: # Muestra los campers aprobados
                    print(Fore.CYAN + f"* {c['nombres']} {c['apellidos']}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No hay campers aprobados." + Style.RESET_ALL)
            input("Presione Enter para continuar...")

        elif opcion_reporte == 4: # Si la opción es 4, listar trainers
            if trainers:
                print(Fore.YELLOW + "Trainers de CampusLands:" + Style.RESET_ALL)
                print("---------------------")
                for t in trainers: # Muestra los trainers registrados
                    print(Fore.CYAN + f"* {t['nombres']} {t['apellidos']}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No hay trainers registrados." + Style.RESET_ALL)
            input("Presione Enter para continuar...")

        elif opcion_reporte == 5: # Si la opción es 5, listar campers con bajo rendimiento
            campers_bajo_rendimiento = [c for c in campers if c.get("rendimeinto") and c["rendimiento"] <0.6] # Filtra los campers con rendimiento menor a 0.6
            if campers_bajo_rendimiento:
                print(Fore.YELLOW + "Campers con bajo rendimiento:" + Style.RESET_ALL)
                print("---------------------")
                for c in campers_bajo_rendimiento: # Muestra los campers con bajo rendimiento
                    print(Fore.CYAN + f"* {c['nombres']} {c['apellidos']}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No hay campers con bajo rendimiento." + Style.RESET_ALL)
            input("Presione Enter para continuar...")
        
        elif opcion_reporte == 6: # Si la opción es 6, listar campers y trainers por ruta
            for ruta in rutas: # Itera sobre las rutas
                campers_en_ruta = [c for c in campers if "ruta_asignada" in c and c ["ruta_asignada"] == ruta["nombre"]] # Filtra los campers asignados a la ruta actual
                trainers_en_ruta = [t for t in trainers if ruta["nombre"] in t["rutas_asignadas"]]  # Filtra los trainers asignados a la ruta actual
                print(Fore.GREEN + f"Ruta: {ruta['nombre'].upper()}" + Style.RESET_ALL)
                print("============")
                if campers_en_ruta: # Si hay campers en la ruta actual
                    print(Fore.YELLOW + "Campers en esta ruta:" + Style.RESET_ALL)
                    print("----------------------")
                    for c in campers_en_ruta: # Muestra los campers en la ruta actual
                        print(Fore.CYAN + f"* {c['nombres']} {c['apellidos']}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "No hay campers en esta ruta." + Style.RESET_ALL)
                if trainers_en_ruta: # Si hay trainers en la ruta actual 
                    print(Fore.YELLOW + "trainers asignados a esta ruta:" + Style.RESET_ALL)
                    print("----------------------")
                    for t in trainers_en_ruta: # Muestra los trainers en la ruta actual 
                        print(Fore.CYAN + f"* {t['nombres']} {t['apellidos']}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "No hay trainers asignados a esta ruta." + Style.RESET_ALL)
                print()
            input("Presione Enter para continuar...")

        elif opcion_reporte == 7: # Si la opción es 7, mostrar estadísticas de módulos
            for ruta in rutas: # Itera sobre las rutas
                print(Fore.GREEN + f"Ruta: {ruta['nombre'].upper()}" + Style.RESET_ALL)
                print("=================")
                for modulo in ruta["modulos"]: # Itera sobre los módulos de la ruta
                    campers_aprobados=[c for c in campers if modulo["nombre"] in c and c [modulo["nombre"]]["estado_final"] == "aprobado"]  # Filtra los campers aprobados en el módulo
                    campers_reprobados=[c for c in campers if modulo["nombre"] in c and c [modulo["nombre"]]["estado_final"] == "reprobado"] # Filtra los campers reprobados en el módulo
                    print(Fore.YELLOW + f"Modúlo: {modulo['nombre']}" + Style.RESET_ALL)
                    print("------------------------------------------")
                    print(Fore.CYAN + f"Campers aprobados: {len(campers_aprobados)}" + Style.RESET_ALL) # Muestra la cantidad de campers aprobados en el módulo
                    print(Fore.CYAN + f"Campers reprobados: {len(campers_reprobados)}" + Style.RESET_ALL) # Muestra la cantidad de campers reprobados en el módulo
                    print("------------------------------------------")
                print()
            input("Presiona Enter para continuar...")

        else: # Si la opción de reporte es inválida
            print(Fore.RED + "Opcion invalida" + Style.RESET_ALL)
            input("Presiona Enter para continuar...")

    elif opcion == 8: # Si la opción es 8, gestionar matrículas 
        data = cargar() # Carga los datos existentes
        campers = [c for c in data["campers"] if c["estado"] == "aprobado"] # Filtra los campers aprobados
        rutas = data["rutas"]
        trainers = data["trainers"]
        areas = data["areas"]
        matriculas = data["matriculas"]

        if not campers: # Si no hay campers aprobados
            print(Fore.RED + "No hay campers aprobados para matricular." + Style.RESET_ALL)
        else:
            for camper in campers: # Itera sobre los campers aprobados
                print(Fore.YELLOW + f"Matriculando el camper {camper['nombres']} {camper['apellidos']}" + Style.RESET_ALL)
                print("------------------------------------------")
                for i, ruta in enumerate(rutas): # Muestra las rutas disponibles
                    print(Fore.CYAN + f"{i+1}. {ruta['nombre']}" + Style.RESET_ALL)
                print("------------------------------------------")
                opcion_ruta = enteros("Seleccione una ruta: ") # Solicita al usuario que seleccione una ruta
                print("------------------------------------------")
                ruta_seleccionada = rutas[opcion_ruta - 1] # Obtiene la ruta seleccionada

                trainer_disponible = None 
                for trainer in trainers: # Itera sobre los trainers
                    if ruta_seleccionada["nombre"] not in trainer["rutas_asignadas"]:
                        trainer_disponible = trainer # Encuentra un trainer disponible para la ruta seleccionada
                        trainer["rutas_asignadas"].append(ruta_seleccionada["nombre"])  # Asigna la ruta al trainer
                        break

                if not trainer_disponible: # Si no hay trainers disponibles para la ruta
                    print(Fore.RED + f"No hay trainers disponibles para la ruta {ruta_seleccionada['nombre']}." + Style.RESET_ALL)
                    continue # Continúa con el siguiente camper

                area_disponible = None
                for area in areas: # Itera sobre las áreas
                    if area["ruta"] == ruta_seleccionada["nombre"] and len(area["campers"]) < area["capacidad_maxima"]:
                        area_disponible = area # Encuentra un área disponible para la ruta seleccionada
                        break

                if not area_disponible:
                    print(Fore.RED + f"No hay areas disponibles para la ruta {ruta_seleccionada['nombre']}." + Style.RESET_ALL)
                    continue # Continúa con el siguiente camper

                fecha_inicio = input("Ingrese la fecha de inicio de la matricula (dd/mm/aaaa): ") # Solicita la fecha de inicio de la matrícula
                fecha_fin = input("Ingrese la fecha de finalizacion de la matricula (dd/mm/aaaa): ") # Solicita la fecha de finalización de la matrícula
                salon = input("Ingrese el salon de entrenamiento: ")
                print("-----------------------------------------------------------")

                matricula = { # Crea un diccionario con los detalles de la matrícula
                    "camper": camper,
                    "ruta": ruta_seleccionada["nombre"],
                    "trainer": trainer_disponible,
                    "area": area_disponible["nombre"],
                    "fecha_inicio": fecha_inicio,
                    "fecha_fin": fecha_fin,
                    "salon": salon
                }

                matriculas.append(matricula) # Agrega la matrícula a la lista de matrículas
                area_disponible["campers"].append(camper) # Agrega el camper al área disponible

                print(Fore.GREEN + f"Matricula registrada exitosamente para el camper {camper['nombres']} {camper['apellidos']}." + Style.RESET_ALL)  # Muestra un mensaje de confirmación

        guardar(data) # Guarda los datos actualizados
        input("Presione Enter para continuar...")

    elif opcion == 9:  # Si la opción es 9, Selecciona los horarios de los Trainers 
        print(Fore.YELLOW + "=== Seleccionar horario de trainers ===" + Style.RESET_ALL)
        data = cargar() # Carga los datos existentes
        trainers = data["trainers"] 
        horarios_disponibles = ["8:00 am - 12:00 pm", "1:00 pm - 5:00 pm", "6:00 pm - 10:00 pm"] # Define una lista de horarios disponibles para asignar a los trainers

        for i, trainer in enumerate(trainers): # Itera sobre la lista de trainers
            print(Fore.CYAN + f"{i+1}. {trainer['nombres']} {trainer['apellidos']}" + Style.RESET_ALL)

        print("")
        opcion_trainer = enteros("Seleccione el número del trainer para asignar el horario: ") # Solicita al usuario que ingrese el número del trainer al que desea asignar un horario

        if 1 <= opcion_trainer <= len(trainers): # Si la opción del trainer seleccionada es válida (dentro del rango de la lista de trainers)
            trainer_seleccionado = trainers[opcion_trainer - 1] # Obtiene el diccionario del trainer seleccionado desde la lista de trainers
            print(Fore.YELLOW + "Horarios disponibles:" + Style.RESET_ALL)
            for i, horario in enumerate(horarios_disponibles): # Itera sobre la lista de horarios disponibles
                print(Fore.CYAN + f"{i+1}. {horario}" + Style.RESET_ALL)

            opcion_horario = enteros("Seleccione el número del horario: ") # Solicita al usuario que ingrese el número del horario que desea asignar

            if 1 <= opcion_horario <= len(horarios_disponibles): # Si la opción del horario seleccionado es válida (dentro del rango de la lista de horarios disponibles)
                horario_seleccionado = horarios_disponibles[opcion_horario - 1] # Obtiene el horario seleccionado desde la lista de horarios disponibles
                trainer_seleccionado["horarios"] = [horario_seleccionado] # Asigna el horario seleccionado al trainer seleccionado en la clave "horarios"
                guardar(data) # Guarda los datos actualizados
                print(Fore.GREEN + f"Horario '{horario_seleccionado}' asignado exitosamente al trainer '{trainer_seleccionado['nombres']} {trainer_seleccionado['apellidos']}'." + Style.RESET_ALL)
            else: # Si la opción del horario es inválida
                print(Fore.RED + "Opción de horario inválida." + Style.RESET_ALL)
        else:  # Si la opción del trainer es inválida
            print(Fore.RED + "Opción de trainer inválida." + Style.RESET_ALL)

        input("Presiona Enter para continuar...")

print(Fore.GREEN + "¡Gracias por utilizar la Gestion Academica de CampusLands!" + Style.RESET_ALL) # Mensaje de despedida

#hecho por jaime barrera cc 1093925253 
#hecho por luis bautista cc 1091356439


# Fechas de subidas (NO BORRAR)

# 1 28-04-2024       10:00 pm    (por Jaime Barrera)
# 2 30-04-2024       12:45 pm    (por Jaime Barrera)
# 3 01-05-2024                   (por luis bautista)
# 4 02-05-2024       12:45 pm    (por Jaime Barrera)
# 5 02-05-2024       10:00 pm    (por Jaime Barrera)
# 6 03-05-2024       11:20 am    (por Jaime Barrera)
# 7 03-05-2024       1:00 pm     (por Jaime Barrera)
# 8 04-05-2024       8:07 pm     (por Jaime Barrera)
# 9 06-05-2024       12:18 am    (por Jaime Barrera)

#   Este código es un programa en Python que permite gestionar una academia llamada "CampusLands". 
#   A continuación, se describen las principales funciones del código línea por línea:

#  1. Las líneas 1-3 importan los módulos necesarios: os para interactuar con el sistema operativo, json para trabajar con archivos JSON, y Fore y Style del módulo colorama para imprimir texto en colores.
#  2. La línea 5 define la ruta del archivo JSON donde se almacenarán los datos.
#  3. Las líneas 7-12 definen la función limpiar() para limpiar la consola dependiendo del sistema operativo.
#  4. Las líneas 14-31 definen la función cargar() para cargar los datos desde el archivo JSON. Si el archivo no existe, se crean los datos iniciales.
#  5. Las líneas 23-36 definen la función guardar(data) para guardar los datos en el archivo JSON.
#  6. Las líneas 38-44 definen la función decimal(prompt) para solicitar un número decimal al usuario.
#  7. Las líneas 46-52 definen la función enteros(prompt) para solicitar un número entero al usuario.
#  8. Las líneas 54-59 definen la función instrucciones() para imprimir las instrucciones de uso del programa.
#  9. Las líneas 62-80 contienen el bucle principal del programa y el menú principal.
#  10. Las líneas 82-84 implementan la opción 0 del menú para salir del programa.
#  11. Las líneas 86-103 implementan la opción 1 del menú para registrar un nuevo camper.
#  12. Las líneas 105-117 implementan la opción 2 del menú para registrar un nuevo trainer.
#  13. Las líneas 119-130 implementan la opción 3 del menú para registrar un nuevo coordinador.
#  14. Las líneas 132-172 implementan la opción 4 del menú para crear una nueva ruta de entrenamiento.
#  15. Las líneas 174-198 implementan la opción 5 del menú para que el coordinador registre las notas de los campers.
#  16. Las líneas 200-246 implementan la opción 6 del menú para asignar campers y trainers a las rutas de entrenamiento.
#  17. Las líneas 248-400 implementan la opción 7 del menú para generar diversos reportes.
#  18. Las líneas 402-465 implementan la opción 8 del menú para gestionar las matrículas de los campers aprobados.
#  19. Las Líneas 467-497 implementan la opción 9 del menú para seleccionar el horario de los traines.
#  20. La línea 499 imprime un mensaje de despedida.
#  21. Las líneas 501-502 indican los autores del código.
#  22. Las líneas 505-516 contienen comentarios sobre las fechas de subida del código.

#  Este código utiliza estructuras de datos como diccionarios y listas para almacenar y manipular la información de los campers, trainers, coordinadores, rutas, áreas y matrículas. 
#  También utiliza funciones para separar las diferentes funcionalidades del programa y facilitar su mantenimiento y escalabilidad.