import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 
primoNumero = float(input("Inserisci il primo numero: "))
operazione = input("Inserisci l'operazione (+, -, *, /): ")
secondoNumero = float(input("Inserisci il secondo numero: "))

 
messaggio = {
    "primoNumero": primoNumero,
    "operazione": operazione,
    "secondoNumero": secondoNumero
}

 
messaggio = json.dumps(messaggio)

 
s.sendto(messaggio.encode("UTF-8"), (SERVER_IP, SERVER_PORT))

 
risposta, _ = s.recvfrom(1024)
risposta = risposta.decode("UTF-8")

 
risultato = json.loads(risposta)

print("Risultato:", risultato["risultato"])