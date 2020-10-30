#! /usr/bin/env python3
from cliente import Cliente

class ClienteParticular(Cliente):
    '''Representa un cliente particular'''
    def __init__(self, nombre, apellido, telefono, mail, id_cliente = None):
        self.nombre = nombre
        self.apellido = apellido
        super().__init__(telefono, mail, id_cliente)
        
    def __str__(self):
        cadena = f"ID del cliente: {self.id_cliente}\nNombre: {self.nombre}\nApellido: {self.apellido}\nTipo de cliente: (Cliente particular)\n"
        cadena += f"Contactos: \nTeléfono: {self.telefono}\nMail: {self.mail}\n"
        return cadena
        
