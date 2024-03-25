import socket
import uuid
from recognition import run_recognition
import datetime

HOST = "0.0.0.0" 
PORT = 2040

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
while True:
     conn, addr = s.accept()
     print("Alert from: ")
     data = conn.recv(4096)
     data += conn.recv(4096)
     data += conn.recv(4096)
     if data:
          print(data[:5])
          uuid_name = "static/images/"+str(uuid.uuid1())+".jpg"
          with open(uuid_name,"wb") as image_file:
               image_file.write(data[5:])
          results = run_recognition(uuid_name)
          with open("logs/log.csv","a") as log_file:
               log_file.write(str(datetime.datetime.now())+","+str(results[0])+","+uuid_name+","+str(data[:5].decode("utf-8"))+"\n")
     else:
          continue
