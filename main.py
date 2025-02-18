def menu()-> None:
    while True:
        op = input("Ingrese una opción: ")
        if op == "a":
            importar_datos()
        elif op == "b":
            buscar_universidad()
        elif op == "c":
            exportar_alumnos()
        elif op == "d":
            mujeres_egresadas()
        elif op == "z":
            print("salir...")
            break
        else:
            print("Opción incorrecta")

def importar_datos():
    """
    importa los datos de las lineas que contengan la palabra universidad
    y la guarda en un JSON

    pre: recive una direccion como parametro

    post: devuelve un entero
    """
    universidades = []
    contador = 0
    try:    
        with open("./mujeres_programadoras_27032018.csv", "r", encoding= "utf-8") as archivo:
            while True:
                linea = archivo.readline()
                if not linea:
                    break
                columnas = linea.strip().split(",")
                
                print(columnas[2])

                if columnas[2].startswith("Universidad"):
                    universidades.append(columnas)
                    contador += 1

        return contador   
    except FileNotFoundError:
        print("Archivo no encontrado..")
 


def buscar_universidad():
    pass

def exportar_alumnos():
    pass

def mujeres_egresadas():
    pass

menu()



