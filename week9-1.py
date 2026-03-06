#write
file=open("file.txt","w")
file.write("Hello World!")
file.write("welcome to python programming")
file.close()
#writelines
file=open("file.txt","a")
lines=("In codd lab\n","In lee lab\n","In panini Lab\n")
file.writelines(lines)
file.close()
#read
file=open("file.txt","r")
content=file.read()
print("using read():")
print(content)
file.close()
#readlines
file=open("file.txt","r")
print("using readlines():")
print(file.readlines())
file.close()
#readline
file=open("file.txt","r")
print("using readline():")
print(file.readline())
file.close()
