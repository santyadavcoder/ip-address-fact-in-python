import socket
computer_name = socket.gethostname()
getip= socket.gethostbyname(computer_name)

print( "computer name: " + computer_name )
print("my ip is : " + getip)

