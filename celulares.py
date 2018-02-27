class celulares:
	"""docstring for celulares"""
	def __init__(self, marca, modelo, imei, falla):
	
		self.marca = marca
		self.modelo = modelo
		self.imei = imei
		self.falla = falla

	def GetMarcaCelular(self):
		return self.marca

	def SetMarcaCelular(self, NuevaMarca):
		self.marca = NuevaMarca

	def GetModeloCelular(self):
		return self.modelo

	def SetModeloCelular(self):
		self.modelo = NuevoModelo

	def GetImeiCelular(self):
		return self.imei

	def SetFallaCelular(self):
		self.falla = NuevaFalla


"""def displayCelulares(self):
         return marca + " " + modelo + " " + imei + " " + falla""" 

		