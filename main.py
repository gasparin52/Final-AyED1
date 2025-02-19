import json
from tabulate import tabulate


def menu()-> None:
    while True:
        op = input("Ingrese una opción: ")
        if op == "a":
            cantidad = importar_datos(archivo_csv)
            if cantidad:
                print("archivo cargado con exito!!")
                print(f"La cantidad de universisdades es: {cantidad}")
        elif op == "b":
            palabra = input("Ingrese nombre o parte del nombre: ")
            buscar_universidad(palabra)
        elif op == "c":
            nombre = input("Ingrese el nombre de la facultad: ")
            exportar_alumnos(nombre)
        elif op == "d":
            mujeres_egresadas()
        elif op == "z":
            print("salir...")
            break
        else:
            print("Opción incorrecta")

def importar_datos(archivo_csv):
    """
    importa los datos de las lineas que contengan la palabra universidad
    y la guarda en un csv.
    Cuenta la cantidad de universidades.

    pre: recive una direccion como parametro

    post: devuelve un entero
    """
    universidades = []
    contador = 0
    datos_uni = {}
    
    try:    
        with open(archivo_csv, "r", encoding= "utf-8") as entrada:
            linea_uno = entrada.readline()
            
            encabezado = [celda.strip() for celda in linea_uno.strip().split(",")]

            print(len(encabezado))

            while True:
                linea = entrada.readline()
                if not linea:
                    break
                columnas = [celda.strip() for celda in linea.strip().split(",")]
                

                if columnas and columnas[2].startswith("Universidad"):
                    universidades.append(columnas)
                    contador += 1
            
            for indice, columna in enumerate(encabezado):
                lista = []
                for fila in universidades:
                    if not fila[indice]:
                        lista.append("0")
                    else:        
                        lista.append(fila[indice])

                datos_uni[columna] = lista

    except FileNotFoundError:
        print("archivo no encontrado..")
    except IndexError as e:
        print(f"Error: {e}")

    try:        
        with open("./universidades.JSON", "w", encoding="utf-8") as f:
            json.dump(datos_uni, f, ensure_ascii=False, indent=4)
    
    except FileNotFoundError:
        print("El archivo no existe...") 

    return contador
    
 


def buscar_universidad(palabra):
    """
    Busca por nombre todas las universidades que coincidan con el nombre ingresado

    pre: recibe un string

    post: devuelve None
    """

    datos = {
        "Año": [],
        "Institución": [],
        "Título": [],
        "Egresados Mujeres": []
    }

    try:
        with open("universidades.JSON", "r", encoding="utf-8") as f:
            uni = json.load(f)
            print(len(uni["Año"]))
            print(len(uni["Institución"]))
            print(len(uni["Título"]))
            print(len(uni["Egresados Mujeres"]))
            for indice, universidad in enumerate(uni["Institución"]):
                if palabra.lower() in universidad.lower():
                    datos["Año"].append(uni["Año"][indice])
                    datos["Institución"].append(uni["Institución"][indice])
                    datos["Título"].append(uni["Título"][indice])
                    datos["Egresados Mujeres"].append(uni["Egresados Mujeres"][indice])
            if datos:
                print(tabulate(datos, headers="keys", tablefmt="pretty"))
            else:
                print("Aún no hay datos cargados.")

    except FileNotFoundError:
        print("El archivo no existe...")
    except IndexError as e:
        print(f"Error: {e}")
        
    return None

def exportar_alumnos(nombre):
    """
    exportar una los datos de una unviersidad de la cual el usuario ingresa el nombre
    
    pre: recibe un string

    post: devuelve None
    """
    with open("universidades.JSON", "r", encoding="utf-8") as entrada:
        datos = json.load(entrada)
        
        filtrado = {clave: [] for clave in datos}

        for indice, valor in enumerate(datos["Institución"]):
            if nombre.lower() == valor.lower():
                nombre_institucion = valor
                for clave in datos:
                    filtrado[clave].append(datos[clave][indice])

    with open(f"{nombre_institucion}.JSON", "w", encoding="utf-8") as salida:
        json.dump(filtrado, salida, ensure_ascii=False, indent=4)

    return None

def mujeres_egresadas():
    

archivo_csv = "mujeres_programadoras_27032018.csv"

menu()



