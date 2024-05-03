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
                {"nombre":"Area 1", "capacidad_maxima":33, "ruta":None, "campers":[], "horarios": ["8:00 am - 12:00 pm"]},  
                {"nombre":"Area 2", "capacidad_maxima":33, "ruta":None, "campers":[], "horarios": ["1:00 pm - 5:00 pm"]},
                {"nombre":"Area 3", "capacidad_maxima":33, "ruta":None, "campers":[], "horarios": ["6:00 pm - 10:00 pm"]}
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
    print("")
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
    print("-------------------------------")

    if opcion == 1: #crear camper
        camper = {
            "# de Identificacion" : int(input("Ingrese el numero de CC o TI del camper: ")),  
            "nombres" : input("Ingrese el nombre del camper: "),
            "apellidos" : input("Ingrese el apellido del camper: "),
            "direccion" : input("Ingrese la dirección del camper: "),
            "acudiente" : input("Ingrese nombre del acudiente del camper: "),
            "Fijo" : int(input("Ingrese el numero de fijo del camper: ")),
            "Telefono" : int(input("Ingrese el numero de telefono del camper: ")),
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
        data["coordinador"] = coordinador  #asigno diccionario al coordinador
        save_data(data)
        print("")
        print("Coordinador creado!!")
        print("")
    
    elif opcion == 4: #crear nueva ruta de entrenamiento
        ruta_nombre=input("Ingrese el nombre de la ruta (NodeJS, Java, NetCore): ")
        print("")
        if ruta_nombre.lower() in ["nodejs","java","netcore"]:
            ruta={
                "nombre": ruta_nombre.lower(),
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
                    print(f"Configurando módulo: {modulo}")
                    detalle_modulo={
                        "nombre": modulo,
                        "contenido":input(f"ingrese el contenido del módulo '{modulo}': ")
                    }
                    print("")
                    ruta["modulos"].append(detalle_modulo)

            data=load_data()
            data["rutas"].append(ruta)
            save_data(data)
            print("")
            print("Ruta de entrenamiento creada!!")
            print("")
        else:
            print("Ruta de entrenamiento no valida. Las opciones validas son: NodeJS, Java, NetCore.")

    elif opcion == 5: #registrar la nota de los campers
        data = load_data()
        campers=data["campers"]
        coordinador=data["coordinador"]

        if not coordinador:
            print("No hay coordinador registrado.")
        else:
            print(f"Binvenido, coordinador {coordinador['nombres']} {coordinador['apellidos']}")
            print("==============================================================================")
            
            for camper in campers:
                if camper['estado'] == "ingreso":
                    nota_teorica=float(input(f"Ingrese la nota teorica del camper {camper['nombres']} {camper['apellidos']}: "))
                    print("-------------------------------------------------------------------------------")
                    nota_practica=float(input(f"Ingrese la nota practica del camper {camper['nombres']} {camper['apellidos']}: "))
                    promedio = (nota_teorica * 0.3) + (nota_practica* 0.6) 
                    if promedio >= 0.6:
                        camper["estado"] = "aprobado"
                    else: 
                        camper["estado"] = "inscrito"
                    camper["nota_final"] = promedio
            save_data(data)
            print("")
            print("Notas registradas !!")
            print("")
            
    elif opcion == 6: #Asignar campers y trainers a rutas de entrenamiento
        data=load_data()
        campers=[c for c in data["campers"] if c["estado"] == "aprobado"]
        rutas=data["rutas"]
        areas=data["areas"]
        trainers=data["trainers"]

        for camper in campers:
            print(f"Asignando ruta para el camper {camper['nombres']} {camper['apellidos']}")
            print("")
            for i, ruta in enumerate(rutas):
                print(f"{i+1}. {ruta['nombre']}")

            print("")
            opcion_ruta=int(input("Seleccione una ruta: "))
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
                print(f"El camper {camper['nombres']} {camper['apellidos']} ha sido asignado a la ruta {ruta_seleccionada['nombre']} en el area {area_disponible['nombre']}.")

                trainer_disponible=None
                for trainer in trainers:
                    if ruta_seleccionada["nombre"] not in trainer["rutas_asignadas"]:
                        trainer_disponible=trainer
                        trainer["rutas_asignadas"].append(ruta_seleccionada["nombre"])
                        break

                if trainer_disponible:
                    print("---------------------------------------------------------------------------------")
                    print(f"El trainer {trainer_disponible['nombres']} {trainer_disponible['apellidos']} ha sido asignado a la ruta {ruta_seleccionada['nombre']}.")
                else:
                    print(f"No hay trainers disponibles para asignar a la ruta {ruta_seleccionada['nombre']}.")
            else: 
                print(f"No hay areas disponibles para la ruta {ruta_seleccionada['nombre']}. El camper {camper['nombres']} {camper['apellidos']} no puede ser asignado.")

        save_data(data)

    elif opcion == 7: #generar reportes
        datal=load_data()
        campers=data["campers"]
        trainers=data["trainers"]
        rutas=data["rutas"]

        print("----Modulo de Reportes----")
        print("")
        print("1. Evaluar campers")
        print("2. Listar campers inscritos")
        print("3. listar campers aprobados")
        print("4. Listar trainers")
        print("5. Listar campers con bajo rendimiento")
        print("6. listar camper y trainers por ruta")
        print("7. mostrar estadisticas de modulos" )
        print("")
        
        opcion_reporte=int(input("Eliga un numero del 1 al 7: "))
        print("")

        if opcion_reporte == 1: #evaluar campers
            for ruta in rutas:
                print(f"Ruta: {ruta['nombre'].upper()}")
                for modulo in ruta["modulos"]:
                    print("")
                    print(f"Evaluando modulo {modulo['nombre']}")
                    print("====================================================")
                    for camper in campers:
                        if"ruta_asignada" in camper and camper["ruta_asignada"] == ruta["nombre"]:
                            nota_teorica=float(input(f"Ingrese la nota teorica del camper {camper['nombres']} {camper['apellidos']} para el modulo {modulo['nombre']}: "))
                            print("-------------------------------------------------------------------------------------------")
                            nota_practica=float(input(f"Ingrese la nota practica del camper {camper['nombres']} {camper['apellidos']} para el modulo {modulo['nombre']}: "))
                            print("-------------------------------------------------------------------------------------------")
                            promedio_pruebas=(nota_teorica * 0.3) + (nota_practica * 0.6)
                            if promedio_pruebas >= 0.6:
                                estado_pruebas="aprobado"
                            else:
                                estado_pruebas="reprobado"
                            
                            quizes_trabajos = []
                            num_quizes_trabajos = int(input(f"Ingrese el numero de quices y trabajos del camper {camper['nombres']} {camper['apellidos']} para el modulo {modulo['nombre']}: "))
                            for i in range(num_quizes_trabajos):
                                print("-------------------------------------------------------------------------------------------")
                                nota_quiz_trabajo = float(input(f"Ingrese la nota del quiz/trabajo {i+1}: "))
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
            save_data(data)
            print("")
            print("Evaluacion de campers completada.")

        elif opcion_reporte == 2: #listar campers inscritos
            campers_inscritos = [c for c in campers if c["estado"] == "inscrito"]
            if campers_inscritos:
                print("Campers inscritos:")
                print("---------------------")
                for c in campers_inscritos:
                    print(f"* {c['nombres']} {c['apellidos']}")
                else:
                    print("No hay campers inscritos")

        elif opcion_reporte == 3: #listar campers aprobados
            print("")
            campers_aprobados = [c for c in campers if c["estado"] == "aprobado"]
            if campers_aprobados:
                print("Campers aprobados:")
                print("---------------------")
                for c in campers_aprobados:
                    print(f"* {c['nombres']} {c['apellidos']}")
                else:
                    print("No hay campers aprobados.")

        elif opcion_reporte == 4: #listar trainers 
            if trainers:
                print("Trainers de CampusLands:")
                print("---------------------")
                for t in trainers:
                    print(f"* {t['nombres']} {t['apellidos']}")
            else:
                print("No hay trainers registrados.")

        elif opcion_reporte == 5: #Listar campers con bajo rendimiento
            campers_bajo_rendimiento = [c for c in campers if c.get("rendimeinto") and c["rendimiento"] <0.6]
            if campers_bajo_rendimiento:
                print("Campers con bajo rendimiento:")
                print("---------------------")
                for c in campers_bajo_rendimiento:
                    print(f"* {c['nombres']} {c['apellidos']}")
            else:
                print("No hay campers con bajo rendimiento.")
        
        elif opcion_reporte == 6: #listar campers y trainers por ruta
            for ruta in rutas:
                campers_en_ruta = [c for c in campers if c.get("ruta_asignada") == ruta["nombre"]]
                trainers_en_ruta = [t for t in trainers if ruta["nombre"] in t["rutas_asignadas"]]
                print(f"Ruta: {ruta['nombre'].upper()}")
                print("============")
                if campers_en_ruta:
                    print("Campers en esta ruta:")
                    print("----------------------")
                    for c in campers_en_ruta:
                        print(f"* {c['nombres']} {c['apellidos']}")
                else:
                    print("No hay campers en esta ruta.")
                if trainers_en_ruta: 
                    print("trainers asignados a esta ruta:")
                    print("----------------------")
                    for t in trainers_en_ruta:
                        print(f"* {t['nombres']} {t['apellidos']}")
                else:
                    print("No hay trainers asignados a esta ruta.")
                print()

        elif opcion_reporte == 7: #mostrar estadisticas de modulos
            for ruta in rutas:
                print(f"Ruta: {ruta['nombre'].upper()}")
                print("=================")
                for modulo in ruta["modulos"]:
                    campers_aprobados=[c for c in campers if c.get(modulo["nombre"], {}).get("estado_final") == "aprobado"]
                    campers_reprobados=[c for c in campers if c.get(modulo["nombre"], {}).get("estado_final") == "reprobado"]
                    print(f"Modúlo: {modulo['nombre']}")
                    print("------------------------------------------")
                    print(f"Campers aprobados: {len(campers_aprobados)}")
                    print(f"Campers reprobados: {len(campers_reprobados)}")
                    print("------------------------------------------")
                print()

        else:
            print("Opcion invalida")

    elif opcion == 8:# Gestionar matriculas 
        data = load_data()
        campers = [c for c in data["campers"] if c["estado"] == "aprobado"]
        rutas = data["rutas"]
        trainers = data["trainers"]
        areas = data["areas"]
        matriculas = data["matriculas"]

        if not campers:
            print("No hay campers aprobados para matricular.")
        else:
            for camper in campers:
                print(f"Matriculando el camper {camper['nombres']} {camper['apellidos']}")
                print("------------------------------------------")
                for i, ruta in enumerate(rutas):
                    print(f"{i+1}. {ruta['nombre']}")
                print("------------------------------------------")
                opcion_ruta = int(input("Seleccione una ruta: "))
                print("------------------------------------------")
                ruta_seleccionada = rutas[opcion_ruta - 1]

                trainer_disponible = None 
                for trainer in trainers:
                    if ruta_seleccionada["nombre"] not in trainer["rutas_asignadas"]:
                        trainer_disponible = trainer
                        trainer["rutas_asignadas"].append(ruta_seleccionada["nombre"])
                        break

                if not trainer_disponible:
                    print(f"No hay trainers disponibles para la ruta {ruta_seleccionada['nombre']}.")
                    continue

                area_disponible = None
                for area in areas:
                    if area["ruta"] == ruta_seleccionada["nombre"] and len(area["campers"]) < area["capacidad_maxima"]:
                        area_disponible = area
                        break

                if not area_disponible:
                    print(f"No hay areas disponibles para la ruta {ruta_seleccionada['nombre']}.")
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

                print(f"Matricula registrada exitosamente para el camper {camper['nombres']} {camper['apellidos']}.")

        save_data(data)

    elif opcion == 9:
        break

#hecho por jaime barrera cc 1093925253 
#hecho por luis bautista cc 1091356439


#fechas de subidas (NO BORRAR)

#1 28-04-2024       10:00 pm    (por Jaime Barrera)
#2 30-04-2024       12:45 pm    (por Jaime Barrera)
#3 01-05-2024                   (por luis bautista)
#4 02-05-2024       12:45 pm    (por Jaime Barrera)
#5 02-05-2024       10:00 pm    (por Jaime Barrera)
#6 03-05-2024       11:20 am    (por Jaime Barrera)
#6 03-05-2024       1:00 pm    (por Jaime Barrera)

#COSAS POR ARREGLAR

#1 documentar
#2 dar espacion con print("") para que se vea estetico