#librerias 
import random 
import numpy as np

#clases 
class persona:
    def int(self,nombre,actividad):
        self.vida=random.uniform(0.5,1)
        self.nombre = nombre
        self.actividad = actividad
    
class soldado (persona):
    def atacar (self, objetivo):
        vidae.vida= enemigo.vida - [0,0.25]

class enemigo (persona):
    def atacar (self, objetivo):
        vidae.vida= aliado.vida - [0,0.25]

class medico (persona):
    def cuarar(self, objetivo):
        vida.vida = aliado.vida + [0,0.25]
        print('vida del soldado', aliado.vida)

class medicoe (persona):
    def cuarar(self, objetivo):
        vida.vida = aliado.vida + [0,0.25]
        print('vida del soldado', aliado.vida)

class death (soldado):
    def muerto (self, vida):
        if enemigo.vida == 0:
            print ('un enemigo a muerto') 
        if aliado.vida == 0:
            print ('un aliado ha muerto')
print ('esta funcionando')
#BANDO Aliados 
al1 = soldado()
al2 = soldado()
al3 = soldado()
al4 = medico()

#BANDO Enemigo
En1 = enemigo()
En2 = enemigo()
En3 = enemigo()
En4 = medicoe()

aliado  = [al1, al2, al3, al4]
enemigo = [En1, En2, En3, En4]

vida = 0
vidae= 0
print('--------------------------------------------------------------------------------------------------------------------------------')
print ('menu')
print ('1 atacar a los enemigos ')#alatque 
print ('2 los enemigos atacan')
print ('0000 rendicion')
# turnos 
selector = input()
# menu
if selector == 000:
    aliado

if selector == 1:
    medico

if selector == 2:
     

if selector == 3:
   

if selector == 4:
       
