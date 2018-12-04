clients = 'Cristian,Hernandez,'

def create_client(client_name):
	global clients

	if client_name not in clients:
		clients += client_name
		_add_comma()
	else:
		print('Cliente ya existe')


def list_clients():
	global clients
	print(clients)


def update_client(client_name, updated_client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', updated_client_name + ',')
	else: 
		print('Cliente no registrado')


def delete_client(client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', '')
	else:
		print('Cliente no registrado')


def _add_comma():
	global clients
	clients += ','

def _print_welcome():
	print('Bienvenidos a Platzi Ventas')
	print('*' * 50)
	print('Que te gustaría hacer hoy?')
	print('[C] Crear Cliente')
	print('[A] Actualizar Cliente')
	print('[E] Eliminar Cliente')


def _get_client_name():
	return input('Cual es el nombre del cliente?')


if __name__ == '__main__':
	_print_welcome()

	command = input('')
	command = command.upper()

	if command == 'C':
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	elif command == 'E':
		client_name = _get_client_name()
		delete_client(client_name)
		list_clients()
		
	elif command == 'A':
		client_name = _get_client_name()
		updated_client_name = input('Cual es el nombre del cliente Actualizado')
		update_client(client_name, updated_client_name)
		list_clients()
	else:
		print('Comando Invalido')