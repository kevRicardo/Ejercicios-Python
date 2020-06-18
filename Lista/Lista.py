from Excepcion import Elemento
from Excepcion import Iter
from Excepcion import ListaVacia

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

	def __init__(self, cabeza, anterior = None):
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
		self.longitud += 1

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
		self.longitud += 1

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
			self.longitud += 1


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
			c += 1
		return it.siguiente

	'''
	Elimina un elemento de la lista. Si el elemento no está contenido en la
	lista, el método no la modifica

	param: elemento
		El elemento a eliminar
	'''
	def elimina(self, elemento):
		n = self.busca_nodo(elemento)
		if n is not None:
			self.elimina_nodo(n)

	def busca_nodo(self, elemento):
		it = Iterator(self.cabeza)
		while it.has_next():
			if it.next() is elemento:
				return it.anterior
		return None

	def elimina_nodo(self, n):
		if self.cabeza is self.rabo:
			self.cabeza = self.rabo = None
		elif self.cabeza is n:
			s = n.siguiente
			s.anterior = None
			self.cabeza = s
		elif self.rabo is n:
			a = n.anterior
			a.siguiente = None
			self.rabo = a
		else:
			a = n.anterior
			s = n.siguiente
			a.siguiente = s
			s.anterior = a
		self.longitud -= 1

	'''
	Elimina el primer elemento de la lista y lo regresa.

	return: El primer elemento de la lista antes de eliminarlo

	raise: ListaVacia
		Si la lista está vacía
	'''
	def elimina_primero(self):
		if self.esVacia():
			raise ListaVacia('Lista vacía')
		c = self.cabeza
		elimina_nodo(c)
		return c.elemento

	'''
	Elimina el último elemento de la lista y lo regresa.

	return: El último elemento de la lista antes de eliminarlo

	raise: ListaVacia
		Si la lista está vacía
	'''
	def elimina_ultimo(self):
		if self.esVacia():
			raise ListaVacia('Lista vacía')
		r = self.rabo
		elimina_nodo(r)
		return r.elemento

	'''
	Nos dice si un elemento está en la lista.

	param: elemento
		El elemento que queremos saber si está en la lista

	return: True si el elemento está en la lista, False en otro caso.
	'''
	def contiene(self, elemento):
		return busca_nodo(elemento) is not None

	'''
	Regresa la reversa de la lista

	return: Una nueva lista que es la reversa la que manda llamar el método
	'''
	def reversa(self):
		l = Lista
		it = Iterator(self.cabeza)
		while it.has_next():
			l.agrega_inicio(it.next())
		return l

	'''
	Regresa una copia de la lista. La copia tiene los mismo elementos que la
	lista que manda llamar el método, en el mismo orden.

	return: una copia de la lista
	'''
	def copia(self):
		l = Lista
		it = Iterator(self.cabeza)
		while it.has_next():
			l.agrega(it.next())
		return l

	'''
	Limpia la lista de elementos, dejándola vacía
	'''
	def limpia(self):
		self.cabeza = self.rabo = None
		self.longitud = 0

	'''
	Regresa el primer elemento de la lista.

	return: El primer elemento de la lista

	raise: ListaVacia
		Si la lista está vacía
	'''
	def get_primero(self):
		if self.esVacia():
			raise ListaVacia('Lista vacía')
		return self.cabeza.elemento

	'''
	Regresa el último elemento de la lista.

	return: El último elemento de la lista

	raise: ListaVacia
		Si la lista está vacía
	'''
	def get_ultimo(self):
		if self.esVacia():
			raise ListaVacia('Lista vacía')
		return self.rabo.elemento

	'''
	Regresa el i-esimo elemento de la lista.

	param: i
		El índice del elemento que queremos.

	return: El i-ésimo elemento de la lista.

	raise: Elemento
		Se lanza una excepción en caso de que el índice del elemento es inválido
	'''
	def get(self, i):
		if i < 0 and i >= self.longitud:
			raise Elemento('Elemento no válido')
		return self.iesimo_nodo(i).elemento

	def indice_de(self, elemento):
		c = 0
		it = Iterator(self.cabeza)
		while it.has_next():
			if it.next() is elemento:
				return c
			c += 1
		return -1

	'''
	Regresa una representación en cadena de la lista.

	return: Una representación en cadena de la lista
	'''
	def to_string(self):
		if self.esVacia():
			return '[]'
		it = Iterator(self.cabeza)
		r = '['
		while it.has_next():
			r += '{:s}, '.format(it.next())
		return r[0:len(r)-2] + ']'

	'''
	Nos dice si la lista es igual al objeto recibido.

	param: El objeto con el que hay que comparar.

	return: True si la lista es igual al objeto recibido, False en otro caso
	'''
	def equals(self, lista):
		if lista == None or type(lista) is not Lista:
			return False
		li = Lista(lista)
		n = Iterator(self.cabeza)
		m = Iterator(li.cabeza)
		while n.has_next() and m.has_next():
			if n.next() is not m.next():
				return False
		return True