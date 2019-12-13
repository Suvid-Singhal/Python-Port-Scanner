import socket
print("--------------------------------")
print("Welcome to Python 3 Port Scanner")
print("--------------------------------\n")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('Enter host: ')
targetip = socket.gethostbyname(target)


def portscan(port,state):
    if state == 1:
        print('++++++++++++++++++++++')
        for x in range(1,1025):
            if portscan(x,2):
                
                print('Port ',x,':    Open')
                print('++++++++++++++++++++++\n')


    if state == 2:
        try:
            con = s.connect((targetip,port))
            return True
        except:
            return False



print("\nSelect an option:\n")
print("1. Scan for all well-known ports")
print("2. Scan for a particular port\n")

selection=int(input())


if selection==1:
    portscan(0,selection)
if selection==2:
    print("\nEnter the port:")
    port=int(input())
    print('')
    print('++++++++++++++++++++++')
    if portscan(port,selection) == True:
        print("Port "+str(port)+':   Open')
        print('++++++++++++++++++++++')
    else:
        print("Port "+str(port)+':   Closed')
        print('++++++++++++++++++++++++')

