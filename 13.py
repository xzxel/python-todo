#Pagina 42
import random
precio= camisa=random.randrange(20,40)
cantidad=random.randrange(5,10)

impCompra=precio*cantidad
prmrDesc=impCompra*0.07
sgndDesc=(impCompra-prmrDesc)*0.07
impDescTotal=prmrDesc+sgndDesc
impPagar=impCompra-impDescTotal

print("Importe de compra: ",impCompra)
print("Primer descuento de: ",prmrDesc)
print("Segundo descuento de: ",sgndDesc)
print("Importe del descuento total: ",impDescTotal)
print("Importe a pagar: ",impPagar)