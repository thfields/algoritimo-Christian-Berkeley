import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))  # Escuta em todas as interfaces
server.listen(5)
print("Servidor esperando conexoes...")

while True:
    conn, addr = server.accept()
    current_time = time.time()  # Tempo em segundos com fração
    conn.sendall(str(current_time).encode())
    conn.close()
