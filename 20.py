#Pagina 49
import random
precio= random.randrange(10,40)
cantidad=random.randrange(5,15)

impCompra=precio*cantidad
desc=0.15*impCompra
impPagar=impCompra-desc

print("Importe de compra: ", impCompra)
print("Importe del descuento: ", desc)
print("Importe a pagar: ", impPagar)