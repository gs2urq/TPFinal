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
        self.lista_trabajos = self.rt.get_all()
        

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
        print("Trabajo guardado exitosamente")
        self.rt.store(nt)

    def trabajo_finalizado(self):
        hoy = self.hoy
        lista = self.lista_trabajos
        for i in lista:
            print(f"ID trabajo:{i.id_trabajo}")
            print(f"Descripcion trabajo: {i.descripcion}")
            print(f"Cliente: {i.cliente}")
            print("=="*25)
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
        lista = self.lista_trabajos
        for i in lista:
            print(f"ID trabajo:{i.id_trabajo}")
            print(f"Descripcion trabajo: {i.descripcion}")
            print(f"Cliente: {i.cliente}")
            print("=="*25)
        opcion = int(input("Ingrese el ID del trabajo entregado: "))
        trabajo = self.rt.get_one(opcion)
        if trabajo == None:
            print(f"Error. ID {opcion} no existe")
        else:
            trabajo.retirado = True
            self.rt.update(trabajo)
            print("Trabajo entregado")

    def trabajo_cancelado(self):
        lista = self.lista_trabajos
        for i in lista:
            print(f"ID trabajo:{i.id_trabajo}")
            print(f"Descripcion trabajo: {i.descripcion}")
            print(f"Cliente: {i.cliente}")
            print("=="*25)
        opcion = int(input("Ingrese el ID del trabajo cancelado: "))
        trabajo = self.rt.get_one(opcion)
        if trabajo == None:
            print(f"Error. ID {opcion} no existe")
        else:
            self.rt.delete(trabajo)
            print("Trabajo cancelado")

    def modificar_trabajo(self):
        lista = self.lista_trabajos
        for i in lista:
            print(f"ID trabajo:{i.id_trabajo}")
            print(f"Descripcion trabajo: {i.descripcion}")
            print(f"Cliente: {i.cliente}")
            print("=="*25)
        opcion = int(input("Ingrese el ID del trabajo que desea modificar: "))
        trabajo = self.rt.get_one(opcion)
        if trabajo == None:
            print(f"Error. ID {opcion} no existe")
        else:
            print("Si no desea cambiar este dato presione enter")
            fi = input("Ingrese la fecha de ingreso (yyyy,mm,d): ")
            fep = input("Ingrese la fecha de entrega propuesta (yyyy,mm,d): ")
            descripcion = input("Ingrese una breve descripcion sobre el trabajo; ")
            retirado = input("Si el trabajo fue entregado ingrese s de lo contrario n: ")
            if fi == "":
                fi = trabajo.fecha_ingreso
            else:
                fecha = datetime.datetime.strptime(fi, "%Y,%m,%d")
                trabajo.fecha_ingreso = fecha
            if fep == "":
                fep = trabajo.fecha_entrega_propuesta
            else:
                fechap = datetime.datetime.strptime(fep, "%Y,%m,%d")
                trabajo.fecha_entrega_propuesta = fechap
            if descripcion == "":
                descripcion = trabajo.descripcion
            else:
                trabajo.descripcion = descripcion
            if retirado == "":
                retirado = t.retirado
            else:
                if retirado == "s" or retirado == "S":
                    trabajo.retirado = True
                else:
                    trabajo.retirado = False
            print("Datos de trabajo actualizados")
            self.rt.update(trabajo)

    def informe_trabajos(self):
        trabajos = []
        lista = self.lista_trabajos
        hoy = self.hoy
        for i in range(365):
            f = hoy - datetime.timedelta(days=i)
            trabajos.append(f)
        alerta=[]
        for i in (lista):
            if i.fecha_entrega_propuesta != None:
                n=i.fecha_entrega_propuesta
                for a in trabajos:
                    if n == a :
                        alerta.append((i.id_trabajo, i.descripcion,
                                       i.cliente, i.fecha_entrega_propuesta,
                                       i.retirado))
        if alerta !=[]:
            print("Trabajos con fechas de entrega vencidas")
            for i in alerta:
                if i[4] == 0:
                    print("=="*25)
                    print (f"ID del trabajo:{i[0]}")
                    print (f"Descripcion del trabajo:{i[1]}")
                    print (f"Fecha que se habia propuesto la entrega:{i[3]}")
                    print (f"Cliente:{i[2]}")
                    print("=="*25)
        else:
            print("Hasta el momento los trabajos se entregaron a tiempo")

        
