import socket

def  main():
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
	tcp_socket.bind(("",7080))

	tcp_socket.listen(128)

	print("1-----")

	new_client_socket,client_addr = tcp_socket.accept()

	print(client_addr)

	print("2-----")

	recv_data = tcp_socket.recv(1024)

	print(recv_data)

	new_client_socket.send("hahahahaah".encode("utf-8"))

	new_client_socket.close()

	tcp_socket.close()
	


if __name__ == '__main__':
	main()
