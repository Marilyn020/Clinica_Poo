from paciente import Paciente
from departameto import Departamento
Pacientes:list[Paciente]=[
    Paciente("11.111.111-1","Juan Perez", 30, "Fonasa"),
    Paciente("22.222.222-2", "Maria Gonzales", 25, "Isapre")
    ]
Departamentos:list[Departamento]=[]    

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def menu():
    print("="*20)
    print("Menu de clinica")
    print("="*20)
    print("1.- Agregar paciente")
    print("2.- Editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Mostrar un paciente")
    print("5.- Mostrar todos los pacientes")
    print("Opciones de departamento:")
    print("6.- Agregar departamento")
    print("7.- Editar departamento")
    print("8.- Eliminar departamento")
    print("9.- Mostrar un departamento")
    print("10.- Mostrar todos los departamentos")
    print("0- Salir")
    op=leer_numero("Ingrese una opción: ")
    return op

# Funciones para manejar departamentos

def agregar_departamento()-> None:
    ID_Depto=leer_numero("Ingrese el ID del departamento: ")
    nombre=input("Ingrese el nombre del departamento: ")
    nuevo_depto=Departamento(ID_Depto,nombre)
    piso=leer_numero("Ingrese el piso del departamento: ")
    nuevo_depto.Piso=piso
    Departamentos.append(nuevo_depto)
    print("Departamento agregado exitosamente.")
    print(f"Total de departamentos: {len(Departamentos)}")

def Buscar_departamento()->Departamento:
    ID_Depto=leer_numero("Ingrese el ID del departamento: ")
    for d in Departamentos:
        if d.Id_Departamento==ID_Depto:
            return d
    print("Departamento no encontrado.")
    return None

def imprimir_departamento()->None:
    Depto = Buscar_departamento()
    if Depto:
        print(Depto)
    else:
        print("No se encontró el departamento.")

def imprimir_departamentos()->None:
    if len(Departamentos)==0:
        print("No hay departamentos registrados.")
    else:
        for Depto in Departamentos:
            print(Depto)
            print("-"*20)

def editar_departamento()->None:
    Depto = Buscar_departamento()
    if Depto:
        print(Depto)
        print("Menu de edición")
        print("1.- Editar nombre")
        print("2.- Editar piso")
        print("0.- Salir")
        op=leer_numero("Ingrese una opción: ")
        if op==1:
            nombre_nuevo=input("Ingrese nuevo nombre: ")
            Depto.Nombre=nombre_nuevo
            print("Nombre actualizado.")
        elif op==2:
            piso_nuevo=leer_numero("Ingrese nuevo piso: ")
            Depto.Piso=piso_nuevo
            print("Piso actualizado.")
        elif op==0:
            print("Saliendo del menú de edición.")
        else:
            print("Opción inválida. No se realizaron cambios.")
    else:
        print("No se encontró el departamento.")

def eliminar_departamento()->None:
    Depto = Buscar_departamento()
    if Depto:
        Departamentos.remove(Depto)
        print("Departamento eliminado.")

# Funciones para manejar pacientes

def agregar_paciente()-> None:
    rut=input("Ingrese el RUT del paciente: ")
    nombre=input("Ingrese el nombre del paciente: ")
    edad=leer_numero("Ingrese la edad del paciente: ")
    print("Tipo de previsión del paciente:")
    print("1.- Fonasa")
    print("2.- Isapre")
    print("3.- Particular")
    print("4.- Otro")
    op=leer_numero("Seleccione la previsión del paciente: ")
    if op==1:
        prevision="Fonasa"
    elif op==2:
        prevision="Isapre"
    elif op==3:
        prevision="Particular"
    elif op==4:
        prevision="Otro"
    
    paciente=Paciente(rut,nombre,edad,prevision)
    Pacientes.append(paciente)
    print("Paciente agregado exitosamente.")
    print(f"Total de pacientes: {len(Pacientes)}")

def imprimir_pacientes()->None:
    if len(Pacientes)==0:
        print("No hay pacientes")
    else:
        for paciente in Pacientes:
            print(paciente.__str__())
            print("-"*20)

def buscar_paciente()->Paciente:
    rut=input("Ingrese el RUT del paciente: ")
    for p in Pacientes:
        if p.rut==rut:
            return p
    print("Paciente no encontrado.")
    return None

def imprimir_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
    else:
        print("No se encontró el paciente.")

def eliminar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        Pacientes.remove(paciente)
        print("Paciente eliminado")
    else:
        print("no se encontro el paciente")

def editar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
        print("Menu de edición")
        print("1.- Editar nombre")
        print("2.- Editar edad")
        print("3.- Editar previsión")
        print("0.- Salir")
        op=leer_numero("Ingrese una opción: ")
        if op==1:
            nombre_nuevo=input("ingrese nuevo nombre: ")
            paciente.nombre=nombre_nuevo
            print("Nombre actualizado")
        elif op==2:
            edad_nueva=input("Ingrese nueva edad: ")
            paciente.edad=edad_nueva
            print("Edad actualizada")
        elif op==3:
            print("tipo de prevision: ")
            print("1.- Fonasa")
            print("2.- Isapre")
            print("3.- Particular")
            print("4.- Otro")
            op=leer_numero("Seleccione la prevision: ")
            if op==1:
                paciente.prevision="Fonasa"
                print("Previsión actualizada")
            elif op==2:
                paciente.prevision="Isapre"
                print("Previsión actualizada")
            elif op==3:
                paciente.prevision="Particular"
                print("Previsión actualizada")
            elif op==4:
                paciente.prevision="Otro"
                print("Previsión actualizada")
            else:
                print("Opción inválida. No se actualizó la previsión.")
    else:
        print("No se encontró el paciente.")

# Bucle paciente

def main():
    while True:
        opcion=menu()
        if opcion==1:
            print("Agregar paciente")
            agregar_paciente()
        elif opcion==2:
            print("Editar paciente")
            editar_paciente()
        elif opcion==3:
            print("Eliminar paciente")
            eliminar_paciente()
        elif opcion==4:
            print("Mostrar un paciente")
            imprimir_paciente()
        elif opcion==5:
            print("Mostrar todos los pacientes")
            imprimir_pacientes()
        elif opcion==6:
            print("Agregar departamento")
            agregar_departamento()
        elif opcion==7:
            print("Editar departamento")
            editar_departamento()
        elif opcion==8:
            print("Eliminar departamento")
            eliminar_departamento()
        elif opcion==9:
            print("Mostrar un departamento")
            imprimir_departamento()
        elif opcion==10:
            print("Mostrar todos los departamentos")
            imprimir_departamentos()
        elif opcion==0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__=="__main__":
    main()
