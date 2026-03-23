import json

# ricevo i dati
data, addr = s.recvfrom(1024)

if not data:
    print("Nessun dato ricevuto")
else:
     
    data = data.decode("UTF-8")
    
   
    data = json.loads(data)
 
    primoNumero = data["primoNumero"]
    operazione = data["operazione"]
    secondoNumero = data["secondoNumero"]

  
    if operazione == "+":
        risultato = primoNumero + secondoNumero
    elif operazione == "-":
        risultato = primoNumero - secondoNumero
    elif operazione == "*":
        risultato = primoNumero * secondoNumero
    elif operazione == "/":
        if secondoNumero == 0:
            risultato = "Errore: divisione per zero"
        else:
            risultato = primoNumero / secondoNumero
    else:
        risultato = "Operazione non valida"

  
    risposta = {
        "risultato": risultato
    }

    risposta = json.dumps(risposta)

   
    s.sendto(risposta.encode("UTF-8"), addr)