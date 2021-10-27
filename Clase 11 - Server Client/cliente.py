from http.client import *
clt = HTTPConnection("localhost", 8080)
pload = input("Ingresa tu mensaje y el servidor te a va a responder (o FIN para terminar)...")
while pload!="FIN":
    pload = pload.encode('utf-8')
    response = clt.request("POST","",pload)
    response = clt.getresponse()
    print(response.status)
    print("Server responde . . . ")
    print(response.read())
    pload = input("Ingresa tu mensaje y el servidor te a va a responder (o FIN para terminar)...")
clt.close()