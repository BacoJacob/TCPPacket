import socket
import filecmp
from datetime import datetime

#initializing host, port
HOST = '192.168.5.67'
PORT = 9000
#starting the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
totalTime = 0
print('I am ready for any client side request \n')
totalFilesCount = 100
i=0;
incorrectTransfers = 0
fileName = 'CompareStandard.txt';
while True:
    conn, addr = s.accept()
    startTime = datetime.now()
    i =i + 1
    
    file = 'receive'+str(i)+'.txt';
    
    print('I am starting receiving file ', file, 'for the ',i,'th time')
    #opening the file to write
    f = open(file, 'wb')
    data = conn.recv(1024)
    while (data):
        f.write(data)
        data = conn.recv(1024)
    f.close()
    
    comp = filecmp.cmp(file, fileName)
    if not comp:
        incorrectTransfers += 1

    print('I am finishing receiving file ', file, 'for the ',i,'th time ')

    conn.close()
    endTime = datetime.now()
    timeDelta = endTime - startTime
    timeDelta = timeDelta.total_seconds()*1000
    print('The time used in millisecond to receive file', fileName,' for the ',i,'th  time is: ', timeDelta)
    totalTime = totalTime + timeDelta
    if i >= totalFilesCount:
        break

s.close()
averageTime = totalTime / totalFilesCount
print('The average time used in millisecond to receive file', fileName,' is: ', averageTime)
print('Total time used in millisecond to receive file', fileName,' is: ', totalTime)
print(incorrectTransfers,' out of ', totalFilesCount)
print('I am done')
# add the code to verify each received file here
# use function "filecmp.cmp('received.txt", fileName, ...)"




    


