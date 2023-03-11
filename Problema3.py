#Juan Esteban Clavijo García - 202225709
#Problema 3.
#Para ganar el curso la nota definitiva debe ser mayor o igual a 3

import numpy

estudiantes=numpy.zeros((6,5))
e=1

for i in range(0,6,1):
    print("Notas del estudiante",e)
    e+=1
    for j in range(0,4,1):
        nota=float(input("Digite una nota:"))
        estudiantes[i][j]=nota
    print("")

e=1
ganaron=0
for i in range(0,6,1):
    p1=estudiantes[i][0]*0.4
    p2=estudiantes[i][1]*0.3
    la=estudiantes[i][2]*0.2
    pr=estudiantes[i][3]*0.1

    definitiva=p1+p2+la+pr
    estudiantes[i][4]=definitiva
    
    print("La nota definitiva del estudiante",e,"es",estudiantes[i][4])
    e+=1

    if definitiva>2.9:
        ganaron+=1

if ganaron>0:
    print("La cantidad de estudiantes que ganaron el curso es",ganaron)
else:
    print("Nadie ganó el curso")

print("")
print(estudiantes)
