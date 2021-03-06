import socketserver
import socket
## Python 3.7

puerto1=9997
host1 = "localhost"
socket1=socket.socket()
socket1.connect((host1,puerto1))

puerto2=9996
socket2=socket.socket()
socket2.connect((host1,puerto2))

puerto3= 9995
socket3=socket.socket()
socket3.connect((host1,puerto3))

def MenuOperacion(x,y,op):
	print(x,y,op)

	if op=='1':
		socket1.send(x.encode("UTF-8"))
		socket1.send(y.encode("UTF-8"))
		socket1.send(op.encode("UTF-8"))
	
	elif op=='2':
		socket2.send(x.encode("UTF-8"))
		socket2.send(y.encode("UTF-8"))
		socket2.send(op.encode("UTF-8"))

	elif op=='3':
		socket3.send(x.encode("UTF-8"))
		socket3.send(y.encode("UTF-8"))
		socket3.send(op.encode("UTF-8"))	
    
	else: pass

class miHandler(socketserver.BaseRequestHandler):


	def handle(self):
		self.numero1=str(self.request.recv(1024).decode("UTF-8"))
		self.numero2=str(self.request.recv(1024).decode("UTF-8"))
		self.operacion=str(self.request.recv(1024).decode("UTF-8"))

		MenuOperacion(self.numero1, self.numero2, self.operacion)
		
		print ("los numeros recibidos son: ",self.numero1,"y", self.numero2, "y la operacion es: ", self.operacion)

		if self.operacion == '1':
			self.suman=socket1.recv(1024).decode("UTF-8")
			print ("La suma es: ", self.suman)
			self.request.send(self.suman.encode("UTF-8"))
			
		elif self.operacion == '2':
			self.restan=socket2.recv(1024).decode("UTF-8")
			print ("La resta es: ", self.restan)
			self.request.send(self.restan.encode("UTF-8"))

		elif self.operacion == '3':
			self.multiplican=socket3.recv(1024).decode("UTF-8")
			print ("La multiplicacion es: ", self.multiplican)
			self.request.send(self.multiplican.encode("UTF-8"))

		else: pass


		
def main():
	print ("Servidor intermedio escuchando...")
	host2="localhost"
	puerto=9999   #entre 0 y 10000, por los 9000 no estan usados

	server1= socketserver.TCPServer((host2,puerto),miHandler)
	print ("server corriendo")
	server1.serve_forever()
main()