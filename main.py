def menu()-> None:
    while True:
        op = input("Ingrese una opción: ")
        if op == "a":
            cantidad = importar_datos(archivo_csv)
            if cantidad:
                print("archivo cargado con exito!!")
                print(f"La cantidad de universisdades es: {cantidad}")
        elif op == "b":
            nombre = input("Ingrese nombre o parte del nombre: ")
            buscar_universidad(nombre)
        elif op == "c":
            exportar_alumnos()
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
    
    try:    
        with open("archivo_csv", "r", encoding= "utf-8") as entrada:
            encabezado = entrada.readline().strip()

            while True:
                linea = entrada.readline()
                if not linea:
                    break
                columnas = linea.strip().split(",")

                if columnas[2].startswith("Universidad"):
                    universidades.append(columnas)
                    contador += 1

        with open("./unviersidades.csv", "w", encoding="utf-8") as salida:
            salida.write(encabezado)
            for filas in universidades:
                fila = ",".join(filas)
                salida.write(fila + "\n")

        return contador
    except FileNotFoundError:
        print("entrada no encontrado..")
 


def buscar_universidad(nombre):
    """
    Busca por nombre todas las universidades que coincidan con el nombre ingresado

    pre: recibe un string

    post: devuelve None
    """
    try:
        

    except FileNotFoundError:
        print("Archivo no encontrado...")

def exportar_alumnos():
    pass

def mujeres_egresadas():
    pass


archivo_csv = "./mujeres_programadoras.csv"

menu()



