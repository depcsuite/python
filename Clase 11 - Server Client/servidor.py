from http.server import *
class EchoServer(BaseHTTPRequestHandler):
    #GET : En general, buscamos solamente OBTENER contenido, sin enviar ningún dato especial
    # Si se envían datos,se envían en la dirección web
    def do_GET(self):
        respuesta = "<h2>Enviando desde server Python!</h2>" #Texto que irá en la respuesta
        enviar = respuesta.encode('utf-8') #Codificación del texto para enviar
        self.wfile.write(enviar) #Envío auténtico del payload
        print("ATENCIÓN . . . SOLICITUD DE CONEXIÓN SERVIDA")
    def do_POST(self):
        recibido = self.rfile.read(int(self.headers['Content-length']))
        recibido = recibido.decode('utf-8')
        print("ATENCIÓN . . .SOLICITUD SERVIDA . . . CLIENTE ENVIO . . .")
        respuesta = recibido.upper() + " CRYPTOOOOOO"
        respuesta = respuesta.encode('utf-8')
        self.wfile.write(respuesta)
        print(recibido)
es = HTTPServer(("localhost", 8080), EchoServer)
es.serve_forever()