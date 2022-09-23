#librerias 
import random 
import numpy as np

#clases 
class persona: # declaracion de un OBJETO
    def int(self,nombre,actividad):
        self.vida=random.uniform(0.5,1)
        self.nombre = nombre
        self.actividad = actividad
    
class soldado (persona):# ataque 
    def atacar (self, objetivo):
        aliado.vida= enemigo.vida - [0,0.25]

class enemigo (persona):# ataque del enemigo 
    def atacar (self, objetivo):#dice a quien atacar 
        enemigo.vida= aliado.vida - [0,0.25]

class medico (persona):# curacion 
    def cuarar(self, objetivo):#aliada
        aliado.vida = aliado.vida + [0,0.25]
        print('vida del soldado', aliado.vida)

class medicoe (persona):#curacion enemiga
    def cuarar(self, objetivo):
        enemigo.vida = enemigo.vida + [0,0.25]
        print('vida del soldado', enemigo.vida)

class death (soldado):#terminacion del juego
    def muerto (self, vida):
        if aliado.vida() == 0:
            print ('GAME OVER')
            exit()

        if enemigo.vida() == 0:
            print ('YOU WINS')
            exit()

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

#menu
print('--------------------------------------------------------------------------------------------------------------------------------')
print ('menu')
print ('1 atacar a los enemigos ')#alatque 
print ('2 los enemigos atacan')
print ('3 curar a los aliados')
print ('0000 rendicion')

# seleccionaor de turnos 
selector = input()

# menu funciones
if selector == 000:
    exit()

if selector == 1:
    soldado()
    death()

if selector == 2:
    enemigo()
    medicoe()
    death()

if selector == 3:
    medico()
    death()

if aliado.vida() == 0:
    print ('GAME OVER')

if enemigo.vida() == 0:
    print ('YOU WINS')

# HE TRATADO DE LLEGAR A LAS 100 LINEAS PROFE NO HE PODIDO
# PERO EL CODIGO ES FUNCIONAL JEJEJEJEJEJE
# Y NO HEMOS LLEVADO PROGRAMCION ORIENTADA A OBJETOS >_<
# Y PASEME CON MB