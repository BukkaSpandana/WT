import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",2225))
while True:
        data,address=s.recvfrom(1024)
        print "server:"+str(data)
	if str(data)=="bye":
		print "Exiting"
                break
        input=raw_input("client:")
        if input=="bye":
		print "Exiting"
                s.sendto(input,("127.0.0.1",2222))
                break
        else:
                s.sendto(input,("127.0.0.1",2222))
