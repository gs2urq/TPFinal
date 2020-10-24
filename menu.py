
from datetime import date
from guardar_cliente import Guardar_Cliente
import sys
class Menu:
    # Mostrar un menú y responder a las opciones
     def __init__(self):
        self.lista_clientes = Guardar_Cliente()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.modificar_cliente_particular,
            "4": self.modificar_cliente_corporativo,
            "5": self.buscar_cliente,
        }
     def mostrar_menu(self):
        print(
            """Menú del anotador:
        1. Mostrar clientes
        2. Nuevo cliente
        3. Modificar cliente particular
        4. Modificar cliente corporativo
        5. Buscar cliente
        6. Agregar trabajo
        7. Mostrar trabajo
        8. Modificar trabajo
        9. Terminar un trabajo
        10. Irabajo retirado
        : """)

     def ejecutar(self):
        # Mostrar el menu y responder a las opciones.
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))

     def mostrar_clientes(self, lista=None):
        if lista == None:
            lista = self.lista_clientes.lista
        for cliente in lista:
            print(cliente)

     def nuevo_cliente(self):
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente: C:Corporativo / P: Particular: ")
        nombre = input("Ingrese el nombre: ")
        if tipo in ("C", "c"):
             contacto = input("Ingrese el nombre del contacto: ")
             tc = input("Ingrese el teléfono del contacto: ")
        else:
                apellido = input("Ingrese el apellido: ")
        tel = input("Ingrese el teléfono: ")
        mail = input("Ingrese el correo electrónico: ")
        if tipo in ("C", "c"):
             c = self.lista_clientes.nuevo_cliente_corporativo(nombre, contacto, tc, tel, mail)
        else:
            c = self.lista_clientes.nuevo_cliente_particular(nombre, apellido, tel, mail)
        if c is None:
            print("Error al cargar el cliente")
        else:
            print(c)
            print("Cliente cargado correctamente")

     def buscar_por_id(self, id_trabajo):
        '''Buscar al cliente con el id dado'''
        for buscar_id in self.listatrabajo:
            if buscar_id.id_cliente == int(id_trabajo):
                return (buscar_id)
        return None

     def modificar_cliente_particular(self):
        id_cliente = int(input("Ingrese el id del cliente a modificar: "))
        opc = int(input(""""Elija una opción para modificar o eliminar un trabajo:
                         1. Nombre
                         2. Apellido
                         3. Teléfono
                         4. Mail
                         5. Eliminar cliente
                         0. Salir
                         """))
        if opc == 1:
            nombre = input("Ingrese el nuevo nombre: ")
            c = self.lista_clientes.modificar_nombre(nombre, id_cliente)
            if c == None:
                print("ERROR AL MODIFICAR CLIENTE")
            else:
                print("MODIFICADO CORRECTAMENTE")
        if opc == 2:
            apellido = input("Ingrese el nuevo apellido: ")
            c = self.lista_clientes.modificar_apellido(apellido, id_cliente)
            if c == None:
                print("ERROR AL MODIFICAR CLIENTE")
            else:
                print("MODIFICADO CORRECTAMENTE")

        if opc == 3:
            telefono = input("Ingrese el nuevo telefono: ")
            c = self.lista_clientes.modificar_telefono(telefono, id_cliente)
            if c == None:
                print("ERROR AL MODIFICAR CLIENTE")
            else:
                print("MODIFICADO CORRECTAMENTE")

        if opc == 4:
            mail = input("Ingrese el nuevo mail: ")
            c = self.lista_clientes.modificar_mail(mail, id_cliente)
            if c == None:
                print("ERROR AL MODIFICAR CLIENTE")
            else:
                print("MODIFICADO CORRECTAMENTE")

        if opc == 5:
            self.lista_clientes.eliminar_cliente(id_cliente)
            c = self.lista_clientes.eliminar_cliente(id_cliente)
            self.lista_clientes = Guardar_Cliente()
            if c == None:
                print("ERROR AL BORRAR CLIENTE")
            else:
                print("BORRADO CORRECTAMENTE")

     def modificar_cliente_corporativo(self):
        id_cliente = int(input("Ingrese el id del cliente a modificar: "))
        opc = int(input(""""Elija una opción para modificar o eliminar un trabajo:
         1. Nombre empresa
         2. Nombre contacto
         3. Teléfono contacto
         4. Teléfono
         5. Mail
         6. Eliminar cliente
         0. Salir
            """))
        if opc == 1:
            nombre_empresa = input("Ingrese el nuevo nombre de la empresa: ")
            c = self.lista_clientes.modificar_nombre_empresa(nombre_empresa, id_cliente)
            if c == None:
                print("ERROR AL MODIFICAR CLIENTE")
            else:
                print("MODIFICADO CORRECTAMENTE")
        if opc == 2:
            nombre_contacto = input("Ingrese el nuevo nombre del contacto: ")
            c = self.lista_clientes.modificar_nombre_empresa(nombre_contacto, id_cliente)
            if c == None:
                print("ERROR AL MODIFICAR CLIENTE")
            else:
                print("MODIFICADO CORRECTAMENTE")
        if opc == 3:
            telefono_contacto = input("Ingrese el nuevo teléfono del contacto: ")
            c = self.lista_clientes.modificar_nombre_empresa(telefono_contacto, id_cliente)
            if c == None:
                print("ERROR AL MODIFICAR CLIENTE")
            else:
                print("MODIFICADO CORRECTAMENTE")
        if opc == 4:
            telefono = input("Ingrese el nuevo telefono: ")
            c = self.lista_clientes.modificar_telefono(telefono, id_cliente)
            if c == None:
                print("ERROR AL MODIFICAR CLIENTE")
            else:
                print("MODIFICADO CORRECTAMENTE")

        if opc == 5:
            mail = input("Ingrese el nuevo mail: ")
            c = self.lista_clientes.modificar_mail(mail, id_cliente)
            if c == None:
                print("ERROR AL MODIFICAR CLIENTE")
            else:
                print("MODIFICADO CORRECTAMENTE")
        if opc == 6:
            self.lista_clientes.eliminar_cliente(id_cliente)
            c = self.lista_clientes.eliminar_cliente(id_cliente)
            self.lista_clientes = Guardar_Cliente()
            if c == None:
                print("ERROR AL BORRAR CLIENTE")
            else:
                print("BORRADO CORRECTAMENTE")


     def buscar_cliente(self):
        listas = self.lista_clientes.lista
        filtro = int(input("Buscar id: "))
        for i in listas:
            if i.id_cliente == filtro:
                print(i)
     def salir(self):
            print("Gracias por utilizar el sistema.")
            sys.exit(0)

if __name__ == "__main__":
    m= Menu()
    m.ejecutar()