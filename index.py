from cliente import cliente
def menu():
	opcion = 0
	while opcion != 4:
		print("\n \n \t \tEl changarro de yoshua el que rifa\n \n")
		print("\t \tPreciona 1 para registrar nuevo cliente")
		print("\t \tPreciona 2 para registrar nuevo celular y servicio")
		print("\t \tPreciona 3 para mostrar los servicos por hacer")
		print("\t \tPreciona 4 para salir")
		opcion = int(raw_input("\t \tOpcion: "))
		if opcion == 1:
			registroCliente()
		else:
			if opcion == 2:
				print("\t \tRegistro de nuevo celular y servicio")
			else:
				if opcion == 3:
					print("\t \tMostrando servicios")
				else:
					if opcion == 4:
						print("\n \n \t \tGracias por tu estancia")
					else:
						if opcion > 4:
							print("\n \n \t \tUyyy! joven se equivoco de opcion regrece despues ya me voy a comer JOJOJO")

def registroCliente():
	print("Registro del cliente")
	idCliente = raw_input("Id de asignacion: ")
	nombre = raw_input("Nombre del cliente: ")
	
def registro():
	print("\n \n \t \tRegistro de un nuevo cliente")
	nombre = raw_input("\n \t \t Nombre del nuevo cliente: ")
menu()