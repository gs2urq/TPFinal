from listaClientes import ListaClientes
from trabajo import Trabajo
from repositorioTrabajos import RepositorioTrabajos
from datetime import datetime
import datetime

class Trabajos:
    def __init__(self):
        self.rt = RepositorioTrabajos()
        self.hoy = datetime.date.today()
        self.lista_clientes = ListaClientes()

        

    def nuevo_trabajo(self):
        listac = self.lista_clientes.listac
        listap = self.lista_clientes.listap
        lista = self.lista_clientes.lista
        hoy = self.hoy
        fecha_ingreso = hoy
        fer = None
        retirado = False
        busca = self.lista_clientes.busca_id
        
        tipo = input("Ingrese a que tipo de cliente pertenece: C (corporativo) o P (particular)")
        if tipo == "c" or tipo == "C":
            for i in listac:
                print(i)
        else:
            for i in listap:
                print(i)
        opcion = int(input("Ingrese el ID del cliente al que pertenece el trabajo: "))
        c = busca(opcion)
        if c == None:
            print("Error. ID no existe")
        fecha = input("Ingrese la fecha de entrega propuesta (yyyy,mm,d): ")
        fep = datetime.datetime.strptime(fecha, "%Y,%m,%d")
        descripcion = input("Ingrese una breve descripcion sobre el trabajo; ")
        nt = Trabajo(c, hoy, fep, fer, descripcion, retirado)
        print(nt)
        self.rt.store(nt)

    def trabajo_finalizado(self):
        hoy = self.hoy
        opcion = int(input("Ingrese el ID del trabajo finalizado: "))
        trabajo = self.rt.get_one(opcion)
        if trabajo == None:
            print(f"Error. ID {opcion} no existe")
        else:
            trabajo.fecha_entrega_real = hoy
            self.rt.update(trabajo)
            print ("Registrado como finalizado")

    def trabajo_entregado(self):
        hoy = self.hoy
        opcion = int(input("Ingrese el ID del trabajo entregado: "))
        trabajo = self.rt.get_one(opcion)
        if trabajo == None:
            print(f"Error. ID {opcion} no existe")
        else:
            trabajo.retirado = True
            self.rt.update(trabajo)
            print("Trabajo entregado")

    def trabajo_cancelado(self):
        opcion = int(input("Ingrese el ID del trabajo cancelado: "))
        trabajo = self.rt.get_one(opcion)
        if trabajo == None:
            print(f"Error. ID {opcion} no existe")
        else:
            self.rt.delete(trabajo)
            print("Trabajo cancelado")

    
