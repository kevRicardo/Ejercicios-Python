class Nodo:

	def __init__(self, elemento):
		# El elemento del nodo
		self.elemento = elemento
		# El nodo anterior
		self.anterior = None
		# El nodo siguiente
		self.siguiente = None

class Lista:

	def __init__(self, longitud = 0, cabeza = None, rabo = None):
		# El primer elemento de la lista
		self.cabeza = cabeza
		# El último elemento de la lista
		self.rabo = rabo
		# La longitud de la lista
		self.longitud = longitud

	'''
	Regresa la longitud de la lista

	return: La longitud de la lista, el número de elementos que contiene
	'''
	def get_longitud(self):
		return self.longitud

	'''
	Regresa el número de elementos en la lista

	return: El número de elementos en la lista
	'''
	def get_elementos(self):
		return self.longitud

	'''
	Nos dice si la lista es vacía

	return: True si la lista es vacía, False en otro caso
	'''
	def esVacia(self):
		return self.cabeza == None

	'''
	Agrega un elemento a la lista. Si la lista no tiene elementos, el elemento a agregar será el primero y el último.

	'''
	def agrega(self, elemento):
		pass