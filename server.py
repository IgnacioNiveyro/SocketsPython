import socket;

def fibonacci(n):
    if(n == 0 or n ==1):
        return n
    else:     
        return fibonacci(n-1) + fibonacci(n-2)

host = '127.0.0.1'
port = 65000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))

server.listen(5)

while True:
    socket_comunicacion , address = server.accept()
    print(f"Estableciendo conexión con: {address}")
    message = socket_comunicacion.recv(1024).decode('utf-8')
    resultado = str(fibonacci(int(message)))
    print(f"Secuencia de fibonacci nro {message} calculada y enviada exitosamente!")
    socket_comunicacion.send(resultado.encode('utf-8'))
    socket_comunicacion.close()
    print(f"La conexión con {address} finalizó")