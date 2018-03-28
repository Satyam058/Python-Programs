filedata = open("file1.txt", "r")
filedata1 = open("file2.txt", "r")
filedata2 = open("file3.txt", "r")
#filedata3 = open("file4.txt", "r")

ls = []
ls1 = []
ls2 = []
ls3 = []
ls4 = []
ls.append((filedata.read()).split(','))
ls.append((filedata1.read()).split(','))
ls.append((filedata2.read()).split(','))
for i in range(len(ls)):
    for j in ls[i]:
        if j == "info":
            ls1.append(j)
        elif j == "error":
            ls2.append(j)
        elif j == "critical":
            ls3.append(j)
        elif j == "warning":
            ls4.append(j)       
f=open("info.txt", "w")
for i in range(len(ls1)):
 f.write(ls1[i])
 f.write("\n")
f1=open("error.txt", "w")
for i in range(len(ls2)):
 f1.write(ls2[i])
 f1.write("\n")
f2=open("critical.txt", "w")
for i in range(len(ls3)):
 f2.write(ls3[i])
 f2.write("\n")
f3=open("warning.txt", "w")
for i in range(len(ls4)):
 f3.write(ls4[i])
 f3.write("\n")
