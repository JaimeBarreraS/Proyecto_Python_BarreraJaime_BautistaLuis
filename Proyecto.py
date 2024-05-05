import os
import json
from colorama import Fore, Style

DATA_FILE="campus_lands.json" #Ruta del archivo

def limpiar():
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear')

#cargar los archivos desde el json
def cargar():
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
                {"nombre":"Area 1", "capacidad_maxima":33, "ruta":None, "campers":[], "horarios": ["8:00 am - 12:00 pm"]},  
                {"nombre":"Area 2", "capacidad_maxima":33, "ruta":None, "campers":[], "horarios": ["1:00 pm - 5:00 pm"]},
                {"nombre":"Area 3", "capacidad_maxima":33, "ruta":None, "campers":[], "horarios": ["6:00 pm - 10:00 pm"]}
            ],
            "matriculas": [],
        }
    return data

#guardar los archivos
def guardar(data):
    with open(DATA_FILE, 'w' ) as file:
        json.dump(data,file, indent=4)

def decimal(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(Fore.RED + "Entrada inválida. Ingrese un número decimal." + Style.RESET_ALL)

def enteros(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print(Fore.RED + "Entrada inválida. Ingrese un número entero." + Style.RESET_ALL)

def instrucciones():
    print(Fore.YELLOW + "Instrucciones de uso:" + Style.RESET_ALL)
    print("1. Selecciona una opcion del menú ingresando el número correspondiente.")
    print("2. Sigue las instrucciones en pantalla para completar la acción seleccionada.")
    print("3. Para salir del programa, selecciona la opcion 0.")
    print(Fore.GREEN + "Presiona Enter para continuar..." + Style.RESET_ALL)


#menu principal
while True:
    limpiar()
    print(Fore.GREEN + "==== Gestion Academica CampusLands ====" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Registrar Camper" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Registrar Trainer" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Registar Coordinador" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. Crear ruta de entrenamiento" + Style.RESET_ALL)
    print(Fore.YELLOW + "5. Registar notas de campers (coordinador)" + Style.RESET_ALL)
    print(Fore.YELLOW + "6. Asignar campers y traines a rutas" + Style.RESET_ALL)
    print(Fore.YELLOW + "7. Generar reportes" + Style.RESET_ALL)
    print(Fore.YELLOW + "8. Gestionar matriculas" + Style.RESET_ALL)
    print(Fore.RED + "0. Salir" + Style.RESET_ALL)
    print("")

    opcion = enteros(Fore.GREEN + "Eliga una opcion: " + Style.RESET_ALL)
    print("-------------------------------")

    if opcion == 0: # salir
        print(Fore.GREEN + "¡Hasta Luego!" + Style.RESET_ALL)
        break

    elif opcion == 1: #crear camper
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
        data = cargar()
        data["campers"].append(camper)
        guardar(data)
        print(Fore.GREEN + "Camper creado exitosamente." + Style.RESET_ALL)
        input("Presiona Enter para continuar...")

    elif opcion == 2: #registrar un nuevo trainer
        print(Fore.YELLOW + "=== Registrar Trainer ===" + Style.RESET_ALL)
        trainer={
            "# de Identificacion" : enteros("Ingrese el numero de CC del Trainer: "),
            "nombres" : input("Ingrese el nombre del Trainer: "),
            "apellidos" : input("Ingrese el apellido del Trainer: "),
            "rutas_asignadas":[]
        }
        data = cargar()
        data["trainers"].append(trainer)
        guardar(data)
        print(Fore.GREEN + "Trainer creado exitosamente." + Style.RESET_ALL)
        input("Presiona Enter para continuar...")
    
    elif opcion == 3: #registrar un nuevo coordinador
        print(Fore.YELLOW + "=== Registrar Coordinador ===" + Style.RESET_ALL)
        coordinador={
            "# de Identificacion" : enteros("Ingrese el numero de CC del Coordinador: "),
            "nombres" : input("Ingrese el nombre del Coordinador: "),
            "apellidos" : input("Ingrese el apellido del Coordinador: "),
        }
        data = cargar()
        data["coordinador"] = coordinador  #asigno diccionario al coordinador
        guardar(data)
        print(Fore.GREEN + "Coordinador creado exitosamente." + Style.RESET_ALL)
        input("Presiona Enter para continuar...")
    
    elif opcion == 4: #crear nueva ruta de entrenamiento
        print(Fore.YELLOW + "=== Crear Ruta de Entrenamiento ===" + Style.RESET_ALL)
        ruta_nombre=input("Ingrese el nombre de la ruta (NodeJS, Java, NetCore): ").lower()
        if ruta_nombre in ["nodejs","java","netcore"]:
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
            for modulo in modulos:
                if isinstance(modulo, dict):
                    ruta["modulos"].append(modulo)
                else: 
                    print("---------------------------------------------------------")
                    print(Fore.YELLOW + f"Configurando módulo: {modulo}" + Style.RESET_ALL)
                    detalle_modulo={
                        "nombre": modulo,
                        "contenido":input(f"Ingrese el contenido del módulo '{modulo}': ")
                    }

                    ruta["modulos"].append(detalle_modulo)

            data=cargar()
            data["rutas"].append(ruta)
            guardar(data)
            print(Fore.GREEN + "Ruta de entrenamiento creada exitosamente." + Style.RESET_ALL)
            input("Presiona Enter para continuar...")
        else:
            print(Fore.RED + "Ruta de entrenamiento no valida. Las opciones validas son: NodeJS, Java, NetCore." + Style.RESET_ALL)
            input("Presiona Enter para continuar...")

    elif opcion == 5: #registrar la nota de los campers
        data = cargar()
        campers=data["campers"]
        coordinador=data["coordinador"]

        if not coordinador:
            print(Fore.RED + "No hay coordinador registrado." + Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"Binvenido, coordinador {coordinador['nombres']} {coordinador['apellidos']}" + Style.RESET_ALL)
            print("==============================================================================")
            
            for camper in campers:
                if camper['estado'] == "ingreso":
                    nota_teorica=decimal(f"Ingrese la nota teorica del camper {camper['nombres']} {camper['apellidos']}: ")
                    print("-------------------------------------------------------------------------------")
                    nota_practica=decimal(f"Ingrese la nota practica del camper {camper['nombres']} {camper['apellidos']}: ")
                    promedio = (nota_teorica * 0.3) + (nota_practica* 0.6) 
                    if promedio >= 0.6:
                        camper["estado"] = "aprobado"
                    else: 
                        camper["estado"] = "inscrito"
                    camper["nota_final"] = promedio
            guardar(data)
            print(Fore.GREEN + "Notas registradas exitosamente." + Style.RESET_ALL)
            input("Presiona Enter para continuar...")
            
    elif opcion == 6: #Asignar campers y trainers a rutas de entrenamiento
        data=cargar()
        campers=[c for c in data["campers"] if c["estado"] == "aprobado"]
        rutas=data["rutas"]
        areas=data["areas"]
        trainers=data["trainers"]

        for camper in campers:
            print(Fore.GREEN + f"Asignando ruta para el camper {camper['nombres']} {camper['apellidos']}" + Style.RESET_ALL)
            print("")
            for i, ruta in enumerate(rutas):
                print(Fore.CYAN + f"{i+1}. {ruta['nombre']}" + Style.RESET_ALL)

            print("")
            opcion_ruta=enteros("Seleccione una ruta: ")
            ruta_seleccionada=rutas[opcion_ruta-1]

            area_disponible=None
            for area in areas:
                if area["ruta"] is None or (area["ruta"] == ruta_seleccionada["nombre"] and len(area["campers"]) < area["capacidad_maxima"]):
                    area_disponible = area
                    break

            if area_disponible:
                area_disponible["ruta"]=ruta_seleccionada["nombre"]
                camper["ruta_asignada"]=ruta_seleccionada["nombre"]
                area_disponible["campers"].append(camper)
                print("---------------------------------------------------------------------------------")
                print(Fore.GREEN + f"El camper {camper['nombres']} {camper['apellidos']} ha sido asignado a la ruta {ruta_seleccionada['nombre']} en el area {area_disponible['nombre']}." + Style.RESET_ALL)

                trainer_disponible=None
                for trainer in trainers:
                    if ruta_seleccionada["nombre"] not in trainer["rutas_asignadas"]:
                        trainer_disponible=trainer
                        trainer["rutas_asignadas"].append(ruta_seleccionada["nombre"])
                        break

                if trainer_disponible:
                    print(Fore.GREEN + f"El trainer {trainer_disponible['nombres']} {trainer_disponible['apellidos']} ha sido asignado a la ruta {ruta_seleccionada['nombre']}." + Style.RESET_ALL)
                    print("---------------------------------------------------------------------------------")
                else:
                    print(Fore.RED + f"No hay trainers disponibles para asignar a la ruta {ruta_seleccionada['nombre']}." + Style.RESET_ALL)
            else: 
                print(Fore.RED + f"No hay areas disponibles para la ruta {ruta_seleccionada['nombre']}. El camper {camper['nombres']} {camper['apellidos']} no puede ser asignado." + Style.RESET_ALL)

        guardar(data)
        input("Presiona Enter para Continuar...")

    elif opcion == 7: #generar reportes
        data=cargar()
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
        
        opcion_reporte=enteros("Eliga una opcion: ")
        print("")

        if opcion_reporte == 1: #evaluar campers
            for ruta in rutas:
                print(Fore.GREEN + f"Ruta: {ruta['nombre'].upper()}" + Style.RESET_ALL)
                for modulo in ruta["modulos"]:
                    print("")
                    print(Fore.YELLOW + f"Evaluando modulo {modulo['nombre']}" + Style.RESET_ALL)
                    print("====================================================")
                    for camper in campers:
                        if"ruta_asignada" in camper and camper["ruta_asignada"] == ruta["nombre"]:
                            nota_teorica=decimal(f"Ingrese la nota teorica del camper {camper['nombres']} {camper['apellidos']} para el modulo {modulo['nombre']}: ")
                            print("-------------------------------------------------------------------------------------------")
                            nota_practica=decimal(f"Ingrese la nota practica del camper {camper['nombres']} {camper['apellidos']} para el modulo {modulo['nombre']}: ")
                            print("-------------------------------------------------------------------------------------------")
                            promedio_pruebas=(nota_teorica * 0.3) + (nota_practica * 0.6)
                            if promedio_pruebas >= 0.6:
                                estado_pruebas="aprobado"
                            else:
                                estado_pruebas="reprobado"
                            
                            quizes_trabajos = []
                            num_quizes_trabajos = enteros(f"Ingrese el numero de quices y trabajos del camper {camper['nombres']} {camper['apellidos']} para el modulo {modulo['nombre']}: ")
                            for i in range(num_quizes_trabajos):
                                print("-------------------------------------------------------------------------------------------")
                                nota_quiz_trabajo = decimal(f"Ingrese la nota del quiz/trabajo {i+1}: ")
                                print("")
                                quizes_trabajos.append(nota_quiz_trabajo)
                            promedio_quizes_trabajos = sum(quizes_trabajos) / num_quizes_trabajos

                            nota_final = (promedio_pruebas * 0.9) + (promedio_quizes_trabajos * 0.1)
                            if nota_final >= 0.6:
                                estado_final="aprobado"
                            else:
                                estado_final="reprobado"

                            camper[modulo['nombre']]={
                                "nota_teorica": nota_teorica,
                                "nota_practica": nota_practica,
                                "promedio_pruebas": promedio_pruebas,
                                "estado_pruebas": estado_pruebas,
                                "quizes_trabajos": quizes_trabajos,
                                "promedio_quizes_trabajos": promedio_quizes_trabajos,
                                "nota_final": nota_final,
                                "estado_final": estado_final
                            }
            guardar(data)
            print(Fore.GREEN + "Evaluacion de campers completada." + Style.RESET_ALL)
            input("Presione Enter para continuar...")

        elif opcion_reporte == 2: #listar campers inscritos
            campers_inscritos = [c for c in campers if c["estado"] == "inscrito"]
            if campers_inscritos:
                print(Fore.YELLOW + "Campers inscritos:" + Style.RESET_ALL)
                print("---------------------")
                for c in campers_inscritos:
                    print(Fore.CYAN + f"* {c['nombres']} {c['apellidos']}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No hay campers inscritos" + Style.RESET_ALL)
            input("Presione Enter para continuar...")

        elif opcion_reporte == 3: #listar campers aprobados
            print("")
            campers_aprobados = [c for c in campers if c["estado"] == "aprobado"]
            if campers_aprobados:
                print(Fore.YELLOW + "Campers aprobados:" + Style.RESET_ALL)
                print("---------------------")
                for c in campers_aprobados:
                    print(Fore.CYAN + f"* {c['nombres']} {c['apellidos']}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No hay campers aprobados." + Style.RESET_ALL)
            input("Presione Enter para continuar...")

        elif opcion_reporte == 4: #listar trainers 
            if trainers:
                print(Fore.YELLOW + "Trainers de CampusLands:" + Style.RESET_ALL)
                print("---------------------")
                for t in trainers:
                    print(Fore.CYAN + f"* {t['nombres']} {t['apellidos']}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No hay trainers registrados." + Style.RESET_ALL)
            input("Presione Enter para continuar...")

        elif opcion_reporte == 5: #Listar campers con bajo rendimiento
            campers_bajo_rendimiento = [c for c in campers if c.get("rendimeinto") and c["rendimiento"] <0.6]
            if campers_bajo_rendimiento:
                print(Fore.YELLOW + "Campers con bajo rendimiento:" + Style.RESET_ALL)
                print("---------------------")
                for c in campers_bajo_rendimiento:
                    print(Fore.CYAN + f"* {c['nombres']} {c['apellidos']}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No hay campers con bajo rendimiento." + Style.RESET_ALL)
            input("Presione Enter para continuar...")
        
        elif opcion_reporte == 6: #listar campers y trainers por ruta
            for ruta in rutas:
                campers_en_ruta = [c for c in campers if "ruta_asignada" in c and c ["ruta_asignada"] == ruta["nombre"]]
                trainers_en_ruta = [t for t in trainers if ruta["nombre"] in t["rutas_asignadas"]]
                print(Fore.GREEN + f"Ruta: {ruta['nombre'].upper()}" + Style.RESET_ALL)
                print("============")
                if campers_en_ruta:
                    print(Fore.YELLOW + "Campers en esta ruta:" + Style.RESET_ALL)
                    print("----------------------")
                    for c in campers_en_ruta:
                        print(Fore.CYAN + f"* {c['nombres']} {c['apellidos']}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "No hay campers en esta ruta." + Style.RESET_ALL)
                if trainers_en_ruta: 
                    print(Fore.YELLOW + "trainers asignados a esta ruta:" + Style.RESET_ALL)
                    print("----------------------")
                    for t in trainers_en_ruta:
                        print(Fore.CYAN + f"* {t['nombres']} {t['apellidos']}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "No hay trainers asignados a esta ruta." + Style.RESET_ALL)
                print()
            input("Presione Enter para continuar...")

        elif opcion_reporte == 7: #mostrar estadisticas de modulos
            for ruta in rutas:
                print(Fore.GREEN + f"Ruta: {ruta['nombre'].upper()}" + Style.RESET_ALL)
                print("=================")
                for modulo in ruta["modulos"]:
                    campers_aprobados=[c for c in campers if modulo["nombre"] in c and c [modulo["nombre"]]["estado_final"] == "aprobado"]
                    campers_reprobados=[c for c in campers if modulo["nombre"] in c and c [modulo["nombre"]]["estado_final"] == "reprobado"]
                    print(Fore.YELLOW + f"Modúlo: {modulo['nombre']}" + Style.RESET_ALL)
                    print("------------------------------------------")
                    print(Fore.CYAN + f"Campers aprobados: {len(campers_aprobados)}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"Campers reprobados: {len(campers_reprobados)}" + Style.RESET_ALL)
                    print("------------------------------------------")
                print()
            input("Presiona Enter para continuar...")

        else:
            print(Fore.RED + "Opcion invalida" + Style.RESET_ALL)
            input("Presiona Enter para continuar...")

    elif opcion == 8:# Gestionar matriculas 
        data = cargar()
        campers = [c for c in data["campers"] if c["estado"] == "aprobado"]
        rutas = data["rutas"]
        trainers = data["trainers"]
        areas = data["areas"]
        matriculas = data["matriculas"]

        if not campers:
            print(Fore.RED + "No hay campers aprobados para matricular." + Style.RESET_ALL)
        else:
            for camper in campers:
                print(Fore.YELLOW + f"Matriculando el camper {camper['nombres']} {camper['apellidos']}" + Style.RESET_ALL)
                print("------------------------------------------")
                for i, ruta in enumerate(rutas):
                    print(Fore.CYAN + f"{i+1}. {ruta['nombre']}" + Style.RESET_ALL)
                print("------------------------------------------")
                opcion_ruta = enteros("Seleccione una ruta: ")
                print("------------------------------------------")
                ruta_seleccionada = rutas[opcion_ruta - 1]

                trainer_disponible = None 
                for trainer in trainers:
                    if ruta_seleccionada["nombre"] not in trainer["rutas_asignadas"]:
                        trainer_disponible = trainer
                        trainer["rutas_asignadas"].append(ruta_seleccionada["nombre"])
                        break

                if not trainer_disponible:
                    print(Fore.RED + f"No hay trainers disponibles para la ruta {ruta_seleccionada['nombre']}." + Style.RESET_ALL)
                    continue

                area_disponible = None
                for area in areas:
                    if area["ruta"] == ruta_seleccionada["nombre"] and len(area["campers"]) < area["capacidad_maxima"]:
                        area_disponible = area
                        break

                if not area_disponible:
                    print(Fore.RED + f"No hay areas disponibles para la ruta {ruta_seleccionada['nombre']}." + Style.RESET_ALL)
                    continue

                fecha_inicio = input("Ingrese la fecha de inicio de la matricula (dd/mm/aaaa): ")
                fecha_fin = input("Ingrese la fecha de finalizacion de la matricula (dd/mm/aaaa): ")
                salon = input("Ingrese el salon de entrenamiento: ")
                print("-----------------------------------------------------------")

                matricula = {
                    "camper": camper,
                    "ruta": ruta_seleccionada["nombre"],
                    "trainer": trainer_disponible,
                    "area": area_disponible["nombre"],
                    "fecha_inicio": fecha_inicio,
                    "fecha_fin": fecha_fin,
                    "salon": salon
                }

                matriculas.append(matricula)
                area_disponible["campers"].append(camper)

                print(Fore.GREEN + f"Matricula registrada exitosamente para el camper {camper['nombres']} {camper['apellidos']}." + Style.RESET_ALL)

        guardar(data)
        input("Presione Enter para continuar...")

print(Fore.GREEN + "¡Gracias por utilizar la Gestion Academica de CampusLands!" + Style.RESET_ALL)

#hecho por jaime barrera cc 1093925253 
#hecho por luis bautista cc 1091356439


#fechas de subidas (NO BORRAR)

#1 28-04-2024       10:00 pm    (por Jaime Barrera)
#2 30-04-2024       12:45 pm    (por Jaime Barrera)
#3 01-05-2024                   (por luis bautista)
#4 02-05-2024       12:45 pm    (por Jaime Barrera)
#5 02-05-2024       10:00 pm    (por Jaime Barrera)
#6 03-05-2024       11:20 am    (por Jaime Barrera)
#7 03-05-2024       1:00 pm     (por Jaime Barrera)
#8 04-05-2024       8:07 pm     (por Jaime Barrera)

#COSAS POR ARREGLAR

#1 documentar ## PENDIENTE ##
#3 UBICAR INSTRUCCIONES DE USO DEL PROGRAMA EN UN LUGAR ESTRATEGICO ## PENDIENTE ##
#4 ORTOGRAFIA #PENDIENTE#