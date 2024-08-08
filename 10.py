#Pagina 33
import random
Total=random.randrange(1000,3000)
print("Dinero a repartir: ", Total)
Josue=0.27*Total
Daniel=0.25*Total
Tamar=Josue*0.85
caleb=0.23*(Josue+Daniel)

print("Dinero para Josue:",Josue)
print("Dinero para Daniel:",Daniel)
print("Dinero para Tamar:",Tamar)
print("Dinero para Caleb:",caleb)

David=Total-Josue-Daniel-Tamar-caleb

print("Dinero para David:",David)


