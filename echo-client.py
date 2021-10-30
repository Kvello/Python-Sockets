import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
blink_rate=6
emotion=[0,0,0,1,0,0,0]
focused=0.5
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message=str(blink_rate)+str('; ')+str(emotion)+str('; ')+str(focused)
    print(message)
    s.sendall(bytes(message,'utf-8'))
    data = s.recv(1024)
    rec=bytes.decode(data,'utf-8')
    blink_rate_rcv,emotion_rcv,focused_rcv=rec.split(';')
#print(data_rcv)
print('Blink_rate: ',blink_rate_rcv)
print('Emotion: ',emotion_rcv)
print('Focused: ',focused_rcv)