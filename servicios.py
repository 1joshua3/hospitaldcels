class servicios:
	"""docstring for servicios"""
	def __init__(self, limpieza, reparacion, liberacion, desbloqueo):
		
		self.limpieza = limpieza
		self.reparacion = reparacion
		self.liberacion = liberacion
		self.desbloqueo = desbloqueo


	def GetServLimpieza(self):
		return self.limpieza

	def SetServLimpieza(self, NuevaLimpieza):
		self.limpieza = NuevaLimpieza

	def GetServReparacion(self):
		return self.reparacion

	def SetServReparacion(self, NuevaReparacion):
		self.reparacion = NuevaReparacion

	def GetServLiberacion(self):
		return self.liberacion

	def SetServLiberacion(self, NuevaLiberacion):
		self.liberacion = NuevaLiberacion

	def GetServDesbloqueo(self):
		return self.desbloqueo

	def SetServDesbloqueo(self, NuevoDesbloqueo):
		self.desbloqueo = NuevoDesbloqueo


	"""def displayServicios(self):
         return limpieza + " " + reparacion + " " + liberacion + " " + desbloqueo  """