# echoserver.py

import socket

#może być nazwą hostu, adresem IP lub pustym ciągiem
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
#port TCP - akceptowania połączeń od klientów - liczba między 1 a 65535
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

#poniżej tworzy obiekt gniazda która obsługuję context menager type
# AF INET - rodzina adresów internetowych IPv4
# SOCK_STREAM - typ gniazda dla tcp protokołu - który będzie używany do przesyłania
# wiadomości w sieci
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # metoda bind wiąze gniazdo z określonym interfejsem i numerem portu
        s.bind((HOST, PORT))
        #nasluchiwanie -backlog domyslny parametr
        s.listen()
    
        conn, addr = s.accept()
    
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
