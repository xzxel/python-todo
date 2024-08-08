#Pagina 18
import random
edad = random.randrange(0,10)
peso = random.randrange(3400, 60000)

print("Edad verificada: ", edad)
print("Peso verifcado: ", peso)

frecuencia = 210 - (0.5*edad)-(0.01*peso/4)

print("Frecuencia cadiaca: ", frecuencia)