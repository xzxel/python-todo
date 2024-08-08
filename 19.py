#pagina 48
import random
donacion= random.randrange(100000, 300000)
print("Donacion total: ", donacion)

aProduc=0.25*donacion
aSoport=0.20*donacion
aMarket=0.15*(aProduc+aSoport)
aContab=0.40*(aMarket+aSoport)
aRRHH=donacion-aSoport-aSoport-aMarket-aContab

print("Monto para Area Produccion: ", aProduc)
print("Monto para Area Soporte: ",aSoport)
print("Monto para Area Marketing: ",aMarket)
print("Monto para Area Contabilidad: ",aContab)
print("Monto para Area Recursos Humanos: ",aRRHH)