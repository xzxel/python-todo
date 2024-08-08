#Pagina 36

import random
dineDeb = random.randrange(10000, 100000)
dineRaq = random.randrange(10000, 100000)
dineSef = random.randrange(10000, 100000)

capital = dineDeb + dineRaq + dineSef

porceDeb=dineDeb*100/capital
porceRaq=dineRaq*100/capital
porceSef=dineSef*100/capital

print("Porcentaje en el aporte de capital de Debora: ", porceDeb)
print("Porcentaje en el aporte de capital de Raquel: ", porceRaq)
print("Porcentaje en el aporte de capital de Sefora: ", porceSef)