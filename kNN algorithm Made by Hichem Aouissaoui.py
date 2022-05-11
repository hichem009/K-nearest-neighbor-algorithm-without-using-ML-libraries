import math 

print("this algorithm is made by student named Hichem Aouissaoui")
print("vous utilisez la division euclidienne")
k=int(input("donner k"))
array  = [["Mohamed", 35, 350 , 3 , "non"],
["Ali", 22, 500 , 2 , "oui"],
["Samia", 63, 2000 , 1 , "non"],
["Sami", 59, 1700 , 1 , "non"],
["Meriem", 25, 400 , 4 , "oui"]]
ch = input("donner le nom ")
val1= int(input("donner l age "))
val2= int(input("donner le revenu "))
val3= int(input("donner le nombre de carte credit "))
array_l = ["Lotfi" , 37 , 500 ,2 ]
a = math.sqrt(((array[0][1]-val1)**2)+((array[0][2]-val2)**2)+((array[0][3]-val3)**2))
b=math.sqrt(((array[1][1]-val1)**2)+((array[1][2]-val2)**2)+((array[1][3]-val3)**2))
c = math.sqrt(((array[2][1]-val1)**2)+((array[2][2]-val2)**2)+((array[2][3]-val3)**2))
d = math.sqrt(((array[3][1]-val1)**2)+((array[3][2]-val2)**2)+((array[3][3]-val3)**2))
e = math.sqrt(((array[4][1]-val1)**2)+((array[4][2]-val2)**2)+((array[4][3]-val3)**2))
arrayy = []
arrayyy=[]
arrayy.append(a)
arrayy.append(b)
arrayy.append(c)
arrayy.append(d)
arrayy.append(e)
arrayclasse =[]
for i in range (k):
    w=min(arrayy)
    arrayyy.append(w)
    if (w==a):
        arrayclasse.append("non")
    elif (w==b):
        arrayclasse.append("oui")
    elif (w==c):
        arrayclasse.append("non")
    elif (w==d):
        arrayclasse.append("non")
    elif (w==e):
        arrayclasse.append("oui")
    arrayy.remove(w)
print(arrayyy)
n=len(arrayclasse)
s=0
p=0
for i in range (n):
    if (arrayclasse[i] == "non"):
        s=s+1
    elif (arrayclasse[i] == "oui"):
        p=p+1
if(s>p):
    print("la classe est non")
elif (p>s):
    print("la classe est oui")
