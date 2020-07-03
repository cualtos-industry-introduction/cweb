if __name__ == "__main__":
    alumnos = {"nombre": ''}
    lista = [alumnos]
   
    for registro in lista:
        registro["nombre"] = input("ingresa el codigo del alumno: ")
    
    print(lista[:])