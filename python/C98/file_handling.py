f=open("C:\\Users\\Admin\\Desktop\\python\\abc.txt",'a')
f.write("Diksha is a good girl \n she is a teacher ")
f=open("C:\\Users\\Admin\\Desktop\\python\\abc.txt",'r')
filelines=f.readlines()
for line in filelines:
        print(line)

