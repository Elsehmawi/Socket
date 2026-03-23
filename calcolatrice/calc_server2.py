import socket

HOST = '127.0.0.1'
PORT = 65432

def calcola(operazione):
    try:
        
        num1, op, num2 = operazione.split()
        num1 = float(num1)
        num2 = float(num2)

        if op == '+':
            return str(num1 + num2)
        elif op == '-':
            return str(num1 - num2)
        elif op == '*':
            return str(num1 * num2)
        elif op == '/':
            if num2 == 0:
                return "Errore: divisione per zero"
            return str(num1 / num2)
        else:
            return "Operatore non valido"
    except Exception:
        return "Formato non valido (usa: numero operatore numero)"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    print("Server in ascolto...")

    while True:
        conn, addr = server.accept()
        with conn:   
            print("Connesso a", addr)

            data = conn.recv(1024)
            if not data:
                continue

            operazione = data.decode()
            risultato = calcola(operazione)

            conn.sendall(risultato.encode())