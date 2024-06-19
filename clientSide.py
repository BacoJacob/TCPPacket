import socket
from datetime import datetime
#initializing host, port, filename, total time and number of times to send the file
host = '192.168.5.67'
port = 9000
fileName = "send.txt"
totalTime =  0
numTimesSend = 100

print('I am connecting to server side: ', host,'\n')
x = 0
for x in range(numTimesSend):
    startTime = datetime.now()
    s = socket.socket()
    s.connect((host, port))
    x = x + 1
     
    print('I am sending file', fileName,' for the ',x,'th  time')
    #opening file to read
    file_to_send = open(fileName, 'rb')    
    #reading the first 1024 bytes
    data = file_to_send.read(1024)
    while data:
        s.send(data)
        #reading the next 1024 bits
        data = file_to_send.read(1024)
    print('I am finishing sending file', fileName,' for the ',x,'th  time')
    file_to_send.close()

    s.close()
    endTime = datetime.now()
    timeDelta = endTime - startTime
    timeDelta = timeDelta.total_seconds()*1000
    print('The time used in millisecond to receive file', fileName,' for the ',x,'th  time is: ', timeDelta)
    totalTime = totalTime + timeDelta

averageTime = totalTime / numTimesSend
print('The average time used in millisecond to receive file', fileName,' is: ', averageTime)
print('Total time used in millisecond to receive file', fileName,' is: ', totalTime)
print('I am done')
