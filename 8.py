#Pagina 27
import random
e1=random.randrange(10,20)
e2= random.randrange(10,20)
e3= random.randrange(10,20)
print("Edad de la persona 1: ",e1)
print("Edad de la persona 2: ", e2)
print("Edad de la persona 3: ", e3)

dineroRepartir= random.randrange(1000,10000)
SumaTotalDeEdades= e1+e2+e3
print("Suma del las edades: ", SumaTotalDeEdades)

monto_de_la_persona1=e1*dineroRepartir/SumaTotalDeEdades
monto_de_la_persona2=e2*dineroRepartir/SumaTotalDeEdades
monto_de_la_persona3=e3*dineroRepartir/SumaTotalDeEdades

print("Monto de la persona 1", monto_de_la_persona1)
print("Monto de la persona 2: ", monto_de_la_persona2)
print("Monto de la persona 3: ", monto_de_la_persona3)
