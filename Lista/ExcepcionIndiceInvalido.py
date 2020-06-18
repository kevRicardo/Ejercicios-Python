'''
Clase para excepciones de índices de lista inválidos
'''

class ExcepcionIndiceInvalido(Exception):
	
	def _IndiceInvalido_(self, msg):
		self.msg = msg

		def _str_(self):
			return repr(self.msg)