import socket
import os
import threading

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)
def multi_threaded_client(connection, address):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        data_decoded = data.decode('utf-8')
        if not data:
          print('Disconnected client: ' + address[0] + ':' + str(address[1]))
          break
          
        print("Got message: " + data_decoded)
        response = 'Server message: ' + data_decoded
        connection.sendall(str.encode(response))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    thread = threading.Thread(target=multi_threaded_client, args=(Client, address, ), daemon=True)
    thread.start()
    print('Thread Number: ' + str(threading.active_count()))
ServerSideSocket.close()