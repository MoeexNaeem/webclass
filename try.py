import csv


d=f.readline()
e=f.readline()
r=f.readline()
t=f.readline()
y=f.readline()
u=f.readline()
i=f.readline()
print(d,e,r,t,y,u,i)

name =input("Name of the city :")

if (name == d,e,r,t,y,u,i ):
    print("Matched")
else : print("Not Found")

d = open("class.txt")
f = d.readline()
f.replace("Pakistan", "Germany")
d.close()

d =  open('class.txt', 'w')
d.write("Germany")


d = open("class.txt")
line =  d.readline()
values = line.split(',')
data = values[4]
print(llne)