#Pagina 45
import random
horas = random.randrange(48,70)
tarifa = random.randrange(70,120)

sBas=horas*tarifa
bonif=sBas*0.20
sBruto=sBas+bonif
desc=sBruto*0.10
Sneto=sBruto-desc

print("Sueldo basico: ", sBas)
print("Bonificacion: ", bonif)
print("Sueldo bruto: ", sBruto)
print("Descuento: ", desc)
print("Sueldo neto: ", Sneto)