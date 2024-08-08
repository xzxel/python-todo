#Pagina 48
import random
donacion=random.randrange(100000, 1000000)
print("Donacion total: ", donacion)

cSalud=0.25*donacion
escuela=0.35*donacion
comedor=0.45*escuela
bibli=0.40*cSalud
asilo=donacion-cSalud-escuela-comedor-bibli

print("A centro de salud le corresponde: ", cSalud )
print("A la escuela le corresponde: ", escuela )
print("Al comedor le corresponde: ", comedor )
print("A la biblioteca le corresponde: ", bibli )
print("Al asilo le corresponde: ", asilo )