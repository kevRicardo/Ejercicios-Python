from Lista import Lista
from Lista import Nodo

def main():
	l = Lista()
	longitud = l.get_longitud()
	print("Longitud ", longitud)
	vacia = l.esVacia()
	print("Lista vacia", vacia)

if __name__ == '__main__':
	main()