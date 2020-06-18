from Excepcion import Elemento
from Excepcion import Iter

'''
Clase para los nodos de la lista. Se tiene un nodo anterior y uno siguiente

param: elemento
	El elemento del nodo

'''
class Nodo:

	def __init__(self, elemento):
		# El elemento del nodo
		self.elemento = elemento
		# El nodo anterior
		self.anterior = None
		# El nodo siguiente
		self.siguiente = None

'''
Clase para los iteradores
'''
class Iterator:
	def __init__(self, anterior = None, cabeza):
		# Nodo siguiente
		self.siguiente = cabeza
		# Nodo anterior
		self.anterior = anterior

	'''
	Nos dice si hay un elemento siguiente
	return: True si hay un elemento siguiente, False en otro caso
	'''
	def has_next(self):
		return self.siguiente != None

	'''
	Nos da el elemento siguiente
	return: El elemento del nodo siguiente
	'''
	def next(self):
		if not self.has_next():
			raise Iter('No hay nodo siguiente')
		self.anterior = self.siguiente
		self.siguiente = self.siguiente.siguiente
		return self.anterior.elemento

	'''
	Nos dice si hay un elemento anterior
	return: True si hay un elemento anterior, False en otro caso
	'''
	def has_previous(self):
		return self.anterior != None

	'''
	Nos da el elemento anterior
	return: El elemento del nodo anterior
	'''
	def previous(self):
		if not self.has_previous():
			raise Iter('No hay nodo anterior')
		self.siguiente = self.anterior
		self.anterior = self.anterior.anterior
		return self.siguiente.elemento

	'''
	Mueve el iterador al inicio de la lista
	'''
	def start(self):
		self.anterior = None
		self.siguiente = cabeza

	'''
	Mueve el iterador al final de la lista
	'''
	def end(self):
		self.siguiente = None
		self.anterior = rabo

'''
Clase génerica para listas doblemente ligadas

Las listas permiten agregar elementos al inicio o final de la lista,
eliminar elementos de la lisa, comprobar si un elemento está p no en la
lista, y otras operaciones básicas

Las listas no aceptan None como elemento
'''
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
	Agrega un elemento a la lista. Si la lista no tiene elementos, 
	el elemento a agregar será el primero y el último.

	param: elemento. 
		El elemento a agregar

	raise: Elemento
		Se lanza una excepción en caso de que el elemento a agregar es inválido
	'''
	def agrega(self, elemento):
		if elemento == None:
			raise Elemento('Elemento no válido')
		n = Nodo(elemento)
		if self.esVacia():
			self.cabeza = self.rabo = n
		else:
			n.anterior = self.rabo
			self.rabo.siguiente = n
			self.rabo = n
		self.longitud = self.get_longitud() + 1

	'''
	Agrega un elemento al final de la lista. Si la lista no tiene elementos, 
	el elemento a agregar será el primero y el último.

	param: elemento. 
		El elemento a agregar

	raise: Elemento
		Se lanza una excepción en caso de que el elemento a agregar es inválido
	'''
	def agrega_final(self, elemento):
		self.agrega(elemento)

	'''
	Agrega un elemento al inicio de la lista. Si la lista no tiene elementos, 
	el elemento a agregar será el primero y el último.

	param: elemento. 
		El elemento a agregar

	raise: Elemento
		Se lanza una excepción en caso de que el elemento a agregar es inválido
	'''
	def agrega_inicio(self, elemento):
		if elemento == None:
			raise Elemento('Elemento no válido')
		n = Nodo(elemento)
		if self.esVacia():
			self.cabeza = self.rabo = n
		else:
			n.siguiente = self.cabeza
			self.cabeza.anterior = n
			self.cabeza = n
		self.longitud = self.get_longitud() + 1

	'''
	Inserta un elemento en un índice explícito.
	Si el índice es menor o igual que cero, el elemento se agrega al incio de la lista.
	Si el índice es mayor o igual que el número de elementos en la lista, el elemento se agrega
	al final de la misma. En otro caso, después de mandar llamar el método, el elemento tendrá 
	el índice que se especifica en la lista

	param: i.
		El índice dónde insertar el elemento. Si es menor que 0 el elemento se agrega
		al inicio de la lista, y si es mayor o igual que el número de elementos en la lista 
		se agrega al final.
	param: elemento
		El elemento a insertar

	raise: Elemento
		Se lanza una excepción en caso de que el elemento a agregar es inválido
	'''
	def inserta(self, i, elemento):
		if elemento == None:
			raise Elemento('Elemento no válido')
		if i < 1:
			self.agrega_inicio(elemento)
		elif i > self.get_longitud()-1:
			agrega(elemento)
		else:
			n = Nodo(elemento)
			s = iesimo_nodo(i)
			a = s.anterior
			n.anterior = a
			a.siguiente = n
			n.siguiente = s
			s.anterior = n
			self.longitud = self.get_longitud() + 1


	'''
	Obtiene el iesimo nodo dado un índice

	param: i
		El índice del nodo

	return: El iesimo nodo
	'''
	def iesimo_nodo(self, i):
		it = Iterator(self.cabeza)
		c = 0
		while c < i:
			it.next()
			c = c+1
		return it.siguiente