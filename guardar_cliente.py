from cliente import Cliente
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioClientes import RepositorioClientes

class Guardar_Cliente:
    def __init__(self):
     self.rc = RepositorioClientes()
     self.lista = self.rc.get_all()

    def nuevo_cliente_corporativo(self, nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail):
        c = ClienteCorporativo(nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail)
        c.id_cliente = self.rc.store(c)
        if c.id_cliente == 0:
            return False
        else:
            self.lista.append(c)
            return c

    def nuevo_cliente_particular(self, nombre, apellido, telefono, mail):
        c = ClienteParticular(nombre, apellido, telefono, mail)
        c.id_cliente = self.rc.store(c)
        if c.id_cliente == 0:
            return False
        else:
            self.lista.append(c)
            return c

    def buscar_por_id(self, id_cliente):
        '''Buscar al cliente con el id dado'''
        for buscar_id in self.lista:
            if buscar_id.id_cliente == id_cliente:
                return (buscar_id)
        return None

    def modificar_nombre(self, nombre, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.nombre = nombre
            return self.rc.update(clientes)
        return None

    def modificar_apellido(self, apellido, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.apellido = apellido
            return self.rc.update(clientes)
        return False

    def modificar_telefono(self, telefono, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.telefono = telefono
            return self.rc.update(clientes)
        return False

    def modificar_mail(self, mail, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.mail = mail
            return self.rc.update(clientes)
        return False

    def eliminar_cliente(self, id_cliente):
        ''' elimina un cliente cancelado'''
        c = self.buscar_por_id(id_cliente)
        if c:
            return self.rc.delete(c)
        return None

    def modificar_nombre_empresa(self, nombre_empresa, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.nombre_empresa = nombre_empresa
            return self.rc.update(clientes)
        return False

    def modificar_nombre_contacto(self, nombre_contacto, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.nombre_contacto = nombre_contacto
            return self.rc.update(clientes)
        return False

    def modificar_telefono_contacto(self, telefono_contacto, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.telefono_contacto = telefono_contacto
            return self.rc.update(clientes)
        return False
