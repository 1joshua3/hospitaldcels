
"""(esto es para importar a el main lo de la clase)  from practica import cliente"""

class cliente:
	"""docstring for Cliente"""
	def __init__(self, idC, nombre, apellido, email, direccion):
		
		self.idC = idC
		self.nombre = nombre
		self.apellido = apellido
		self.email = email
		self.direccion = direccion

	def GetIdCliente(self):
		return self.idC

	def SetIdCliente(self, NuevoId):
		self.idC = NuevoId

	def GetNombreCliente(self):
		return self.nombre

	def SetNombreCliente(self, NuevoNombre):
		self.nombre = NuevoNombre

	def GetApellidoCliente(self):
		return self.apellido

	def SetApellidoCliente(self, NuevoApellido):
		self.apellido = NuevoApellido

	def GetEmailCliente(self):
		return self.email

	def SetDireccionCliente(self, NuevaDireccion):
		self.direccion = NuevaDireccion

	def (self):
        

