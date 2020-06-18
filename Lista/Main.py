from Lista import Lista
from Lista import Nodo

def main():
	l = Lista()
	longitud = l.get_longitud()
	print("Longitud ", longitud)
	vacia = l.esVacia()
	print("Lista vacia", vacia)
	l.agrega("Hola")
	print(l.cabeza.elemento)
	print(l.rabo.elemento)
	longitud = l.get_longitud()
	print("Longitud ", longitud)
	l.agrega("como")
	l.agrega("has")
	l.agrega("estado")
	l.agrega("yo")
	l.agrega("estoy")
	l.agrega("bien")
	print(l.iesimo_nodo(3).elemento)
	print(l.busca_nodo("yO"))
	l.elimina("bien")
	print(l.to_string())

if __name__ == '__main__':
	main()