import socket;
import sys;

#cantidad de argumentos.
cantidad_argumentos = len(sys.argv)
if(cantidad_argumentos!=2 or len(sys.argv[1])<2):
    sys.exit("Argumentos incorrectos.")

rango = slice(1,len(sys.argv[1]))
argumento = sys.argv[1]
numero = argumento[rango]

host = '127.0.0.1'
port = 65000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host,port))

socket.send(numero.encode('utf-8'))
print(f"Secuencia nro {numero} enviada al servidor para ser calculada.")
message = socket.recv(1024).decode('utf-8')
print(f"La secuencia de fibonacci es: {message}")
print(socket.recv(1024).decode('utf-8'))
socket.close()