
f=open("definition.txt","r")
y=open("empty.txt","w")

str= f.readline()

while str:
    y.write(str)
    print(str)
    str =f.readline()
    
f.close()
y.close()

