'''
Clase para excepciones
'''

class Elemento(ValueError):
	
	def __init__(self, msg, *args):
		super(Elemento, self).__init__(msg, *args)

class Iter(ValueError):

	def __init__(self, msg, *args):
		super(Elemento, self).__init__(msg, *args)