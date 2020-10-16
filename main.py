import sys
from listaClientes import ListaClientes
class Menu:
    def __init__(self):
        self.lista_clientes = ListaClientes()
        self.opciones= {
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
        
        if lista == None:
            lista = self.lista_clientes.lista

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
