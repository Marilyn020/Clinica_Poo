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

def menu_Clinica()-> int:
    print("="*20)
    print("MENÚ CLÍNICA")
    print("="*20)
    print("1.- Gestionar Pacientes")
    print("2.- Gestionar Departamentos")
    print("0.- Salir del programa")
    return leer_numero("Ingrese una opción: ")

def menu_Pacientes()->int:
    print("="*20)
    print("MENÚ PACIENTES")
    print("="*20)
    print("1.- Agregar paciente")
    print("2.- Editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Mostrar un paciente")
    print("5.- Mostrar todos los pacientes")
    print("0.- Volver al Menú Clínica")
    return leer_numero("Ingrese una opción: ")

def menu_Departamentos()->int:
    print("="*20)
    print("MENÚ DEPARTAMENTOS")
    print("="*20)
    print("1.- Agregar departamento")
    print("2.- Editar departamento")
    print("3.- Eliminar departamento")
    print("4.- Mostrar un departamento")
    print("5.- Mostrar todos los departamentos")
    print("0.- Volver al Menú Clínica")
    return leer_numero("Ingrese una opción: ")

# Funciones para manejar departamentos

def agregar_departamento()-> None:
    ID_Depto =leer_numero("Ingrese el ID del departamento: ")
    nombre =input("Ingrese el nombre del departamento: ")
    piso=leer_numero("Ingrese el piso del departamento: ")
    nuevo_depto=Departamento(ID_Depto, nombre, piso)
    
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
        opcion_clinica=menu_Clinica()
        if opcion_clinica ==1:
            while True:
                op_paciente = menu_Pacientes()
                if op_paciente == 1:
                    agregar_paciente()
                elif op_paciente == 2:
                    print("Editar paciente")
                    editar_paciente()
                elif op_paciente == 3:
                    print("Eliminar paciente")
                    eliminar_paciente()
                elif op_paciente == 4:
                    print("Mostrar un paciente")
                    imprimir_paciente()
                elif op_paciente == 5:
                    print("Mostrar todos los pacientes")
                    imprimir_pacientes()
                elif op_paciente == 0:
                    break
                else:
                    print("Opción Invalida.")
        elif opcion_clinica == 2:
            while True:
                op_deptos = menu_Departamentos()
                if op_deptos == 1:
                    print("Agregar departamento")
                    agregar_departamento()
                elif op_deptos == 2:
                    print("Editar departamento")
                    editar_departamento()
                elif op_deptos == 3:
                    print("Eliminar departamento")
                    eliminar_departamento()
                elif op_deptos == 4:
                    print("Mostrar un departamento")
                    imprimir_departamento()
                elif op_deptos == 5:
                    print("Mostrar todos los departamentos")
                    imprimir_departamentos()
                elif op_deptos==0:
                    break
                else:
                    print("Opción inválida.")
        elif opcion_clinica == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción Invalida...Intente nuevamente.")

if __name__=="__main__":
    main()
