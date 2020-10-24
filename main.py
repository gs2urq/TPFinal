import sys
from listaClientes import ListaClientes
class Menu:
    def __init__(self):
        self.lista_clientes = ListaClientes()
        self.opciones= {
            "4": self.actualizar_cliente,
            "3": self.borrar_cliente,
            "2": self.mostrar_clientes,
            "1": self.nuevo_cliente,
            "0": self.salir
            }
    def mostrar_menu(self):
        print("""
Menú del sistema:
1. Nuevo Cliente
2. Mostrar Clientes
3. Borrar Cliente
4. Actualizar Cliente
0. Salir
""")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opcion: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opcion valida".format(opcion))

    def mostrar_clientes(self, lista = None):
        print("""
1. Mostrar todos los clientes
2. Mostrar clientes corporativos
3. Mostrar clientes particulares
""")
        opcion=input("Ingrese una opcion: ")
        if opcion == "1":
            if lista == None:
                lista = self.lista_clientes.lista
                print("Todos los clientes")
                for cliente in lista:
                    print ("=="*25)
                    print (cliente)
        elif opcion == "2":
            if lista == None:
                lista = self.lista_clientes.listac
                print("Clientes corporativos")
                for cliente in lista:
                    print ("=="*25)
                    print (cliente)
        else:
            if lista == None:
                lista = self.lista_clientes.listap
                print("Clientes particulares")
                for cliente in lista:
                    print ("=="*25)
                    print (cliente)
              
    def nuevo_cliente(self):
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente: C:Corporativo / P:Particular: ")
        nombre = input("Ingrese el nombre: ")
        if tipo in ("C", "c"):
            contacto = input("Ingrese el nombre del contacto: ")
            tc = input("Ingrese el telefono de contacto: ")
        else:
            apellido = input("Ingrse el apellido: ")
        tel = input("Ingrese el telefono: ")
        mail = input("Ingrese el correo electronico: ")
        if tipo in ("C", "c"):
            c = self.lista_clientes.nuevo_cliente_corporativo(nombre, contacto,
                                                          tc, tel, mail)
        else:
            c = self.lista_clientes.nuevo_cliente_particular(nombre, apellido,
                                                         tel, mail)
        if c is None:
            print("Error al cargar el cliente")
        else:
            print("Cliente cargado correctamente")

    def actualizar_cliente(self):
        l = self.lista_clientes.lista
        c = self.lista_clientes.listac
        p = self.lista_clientes.listap
        print("Si el tipo de cliente que desea modificar es Corporativo ingrese c")
        print("Si el tipo de cliente que desea modificar es Particular ingrese p")
        tipo = input("Ingrese el tipo de cliente: ")
        if tipo == "c" or tipo == "C":
            print("Estos son todos los clientes corporativos")
            for i in c:
                print("=="*25)
                print(i)
                print("=="*25)
            opcion=int(input("Ingrese el ID del cliente que desea modificar: "))
            n = self.lista_clientes.busca_id(opcion)
            if n != None:
                for i in c:
                    if i.id_cliente == n.id_cliente:
                        print(n)
                        print("Si no desea cambiar este dato presione enter")
                        ne=input("Ingrese el nombre de la empresa: ")
                        nc=input("Ingrese el nombre de contacto: ")
                        tc=input("Ingrese el telefono de contacto: ")
                        tel=input("Ingrese un telefono: ")
                        mail=input("Ingrese un correo electronico: ")
                        if ne == "":
                            ne = n.nombre_empresa
                        else:
                            n.nombre_empresa = ne
                        if nc == "":
                            nc = n.nombre_contacto
                        else:
                            n.nombre_contacto = nc
                        if tc == "":
                            tc = n.telefono_contacto
                        else:
                            n.telefono_contacto = tc
                        if tel == "":
                            tel = n.telefono
                        else:
                            n.telefono = tel
                        if mail == "":
                            mail = n.mail
                        else:
                            n.mail = mail
                        for i in l:
                            if i.id_cliente == n.id_cliente:
                                i = n
                        print(f"Cliente actializado {n}")
                        self.lista_clientes.rc.update(n)
            print(f"ID {opcion} no es cliente corporativo o se actualizo recientemente")
        else:
            print("Estos son todos los clientes particulares")
            for i in p:
                print("=="*25)
                print(i)
                print("=="*25)
            opcion=int(input("Ingrese el ID del cliente que desea modificar: "))
            n = self.lista_clientes.busca_id(opcion)
            if n != None:
                for i in p:
                    if i.id_cliente == n.id_cliente:
                        print("Si no desea cambiar este dato precione enter")
                        nombre=input("Ingrese el nombre: ")
                        apellido=input("Ingrese el apellido: ")
                        tel=input("Ingrese un telefono: ")
                        mail=input("Ingrese un correo electronico: ")
                        if n == "":
                            nombre = n.nombre
                        else:
                            n.nombre = nombre
                        if apellido == "":
                            apellido = n.apellido
                        else:
                            n.apellido = apellido
                        if tel == "":
                            tel = n.telefono
                        else:
                            n.telefono = tel
                        if mail == "":
                            mail = n.mail
                        else:
                            n.mail = mail
                        for i in l:
                            if i.id_cliente == n.id_cliente:
                                i = n
                        print(f"Cliente actualizado {n}")
                        self.lista_clientes.rc.update(n)
                else:
                    print(f"ID {opcion} no es cliente particular o se actualizo recientemente")
            else:
                print(f"Error. El ID {opcion} no existe")
        
    def borrar_cliente(self):
        c = self.lista_clientes.lista
        for i in c:
            print("=="*25)
            print (i)
        opcion = int(input("Ingrese el ID del cliente que desea eliminar: "))
        for i in c:
            if i.id_cliente == opcion:
                j = self.lista_clientes.rc.delete(i)
                c.remove(i)
                if j is False:
                    print(f"Error al borrar cliente. ID", opcion, "no existe")
                else:
                    print("Cliente borrado exitosamente")
                    print("Lista de clientes actualizada")
                    self.mostrar_clientes()
                


    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)


if __name__ == "__main__":
    m = Menu()
    m.ejecutar()
