from listaClientes import ListaClientes
from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo
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
        hoy = datetime.date.today()
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
