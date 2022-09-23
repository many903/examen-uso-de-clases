#librerias 
import random 

#clases 
class persona:
    def int(self,nombre,actividad):
        self.vida=random.uniform(0.5,1)
        self.nombre = nombre
        self.actividad = actividad
    
class soldado (persona):
    def atacar (self, objetivo):
        enemigo.vida= enemigo.vida - [0,0.25]

class medico (persona):
    def cuarar(self, objetivo):
        aliado.vida = aliado.vida + [0,0.25]

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
En1 = soldado()
En2 = soldado()
En3 = soldado()
En4 = medico()

aliado = [al1, al2, al3, al4]
enemigo = [En1, En2, En3, En4]

