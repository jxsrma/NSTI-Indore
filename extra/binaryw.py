bFile = open("Hello.dat","wb")
bFile.write(b"Hello World\nThis is Dat File")
bFile.close()

bFile = open("Hello.dat","rb")
data = bFile.readline()
print(data)
print(bFile.tell())
bFile.close()
