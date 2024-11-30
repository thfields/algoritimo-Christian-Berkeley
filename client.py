import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('server', 12345))  # 'server' é o nome do contêiner do servidor

start_time = time.time()
client.sendall(b'Qual eh o horário?')
server_time = float(client.recv(1024).decode())
end_time = time.time()

rtt = (end_time - start_time) / 2
adjusted_time = server_time + rtt
print(f"Hora do servidor: {server_time}")
print(f"RTT: {rtt:.6f} segundos")
print(f"Hora ajustada: {adjusted_time}")
client.close()
