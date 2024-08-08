#Pagina 39

import random
precio = random.randrange(10,20)
cantidad = random.randrange(0,10)
print("Precio del producto: ", precio)
print("Cantidad adquirida: ", cantidad)

impCompra=precio*cantidad

impDesc=impCompra*0.11

impPagar=impCompra-impDesc
Obsequios=2*cantidad

print("Importe de compra: ", impCompra)
print("importe de Descuento: ", impDesc)
print("Importe a pagar: ", impPagar)
print("Cantidad de obsequios: ", Obsequios)