"""1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
del rectángulo
class Rectangulo:
    def __init__ (self,Base,Altura):
        self.Base=Base
        self.Altura=Altura
    def metodo(self):
        calculo=int(self.Base)*int(self.Altura)
        print(calculo)

rectangulo1= Rectangulo(2,1342)

rectangulo1.metodo()
"""


"""2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.


class Mate:
    def __init__(self, cantidad_maxima_cebadas):
        self.cantidad_cebadas_restantes=cantidad_maxima_cebadas
        self.estado ="lleno"  
        self.cantidad_maxima_cebadas = cantidad_maxima_cebadas

    def cebar(self):
        if self.estado =="lleno":
            print("¡Cuidado! ¡Te quemaste!")
        else:
            self.estado ="lleno"
            print("Mate cebado con agua.")

    def beber(self):
        if self.estado == "vacío":
            print("¡El mate está vacío!")
        else:
            self.cantidad_cebadas_restantes -= 1
            if self.cantidad_cebadas_restantes < 0:
                print("Advertencia: el mate está lavado.")
            else:
                print("Se ha bebido del mate.")
            self.estado="vacío"

mate = Mate(3)
mate.cebar()  
mate.beber()  
mate.beber() 
mate.beber()  
mate.beber()  
mate.cebar()  
"""


"""Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho

class Corcho:
    def __init__(self,bodega):
        self.bodega =bodega
class Botella:
    def __init__(self,corcho):
        self.corcho = corcho  
class Sacacorchos:
    def __init__(self):
        self.corcho= None 
    def destapar(self,botella):
        if botella.corcho is None:
            print("La botella ya está destapada.")
            return 
        if self.corcho is not None:
            print("El sacacorchos ya tiene un corcho.")
            return  
        self.corcho =botella.corcho
        botella.corcho= None  
        print(f"Se ha destapado la botella de la bodega: {self.corcho.bodega}")

    def limpiar(self):
        if self.corcho is None:
            print("No hay un corcho en el sacacorchos para limpiar.")
            return  
        
        print(f"Se ha limpiado el corcho de la bodega: {self.corcho.bodega}")
        self.corcho=None  
corcho1 = Corcho("Bodega del Vino")
botella1 = Botella(corcho1)
sacacorchos = Sacacorchos()
sacacorchos.destapar(botella1)  
sacacorchos.limpiar()  
"""

"""4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
al método
class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre =restaurante_nombre
        self.tipo_comida =tipo_comida
    def describir_restaurante(self):
        print(f"Nombre del restaurante:{self.restaurante_nombre}")
        print(f"Tipo de comida:{self.tipo_comida}")

    def abrir_restaurante(self):
        print(f"El restaurante{self.restaurante_nombre} ahora está abierto.")
class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida
        self.sabores = sabores
    def mostrar_sabores(self):
        print("Sabores disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}")
mi_heladeria = Heladeria("Helados Deliciosos", "Helados", ["Vainilla", "Chocolate", "Fresa"])
mi_heladeria.describir_restaurante()
mi_heladeria.abrir_restaurante()"
"""

"""5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
devuelva la cantidad cosechada

class Personaje:
    def __init__(self, vida, posicion, velocidad):
        self.vida=vida
        self.posicion=posicion
        self.velocidad=velocidad
    def recibir_ataque(self,cantidad):
        self.vida-=cantidad
        if self.vida <=0:
            raise Exception("El personaje ha sido derrotado.")
    def mover(self, direccion):
        if direccion=="arriba":
            self.posicion[1]+=self.velocidad
        elif direccion =="abajo":
            self.posicion[1]-=self.velocidad
        elif direccion=="izquierda":
            self.posicion[0]-=self.velocidad
        elif direccion=="derecha":
            self.posicion[0]+=self.velocidad
        else:
            print("Dirección no válida.")
class Soldado(Personaje):
    def __init__(self,vida,posicion,velocidad,ataque):
        super().__init__(vida,posicion,velocidad)
        self.ataque=ataque
    def atacar(self,otro_personaje):
        otro_personaje.recibir_ataque(self.ataque)
class Campesino(Personaje):
    def __init__(self,vida,posicion,velocidad,cosecha):
        super().__init__(vida,posicion,velocidad)
        self.cosecha=cosecha
    def cosechar(self):
        return self.cosecha
soldado=Soldado(vida=100, posicion=[0,0],velocidad=5,ataque=20)
print(f"Soldado inicial: Vida={soldado.vida}, Posición={soldado.posicion}")
campesino = Campesino(vida=50, posicion=[10, 10], velocidad=2, cosecha=30)
print(f"Campesino inicial: Vida={campesino.vida}, Posición={campesino.posicion}")
soldado.atacar(campesino)
print(f"Después del ataque: Vida del campesino={campesino.vida}")
campesino.mover("izquierda")
print(f"Posición del campesino después de moverse: {campesino.posicion}")
cantidad_cosechada = campesino.cosechar()
print(f"Cantidad cosechada por el campesino: {cantidad_cosechada}")
"""
 


"""
6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno

class usuario:
    def __init__(self,nombre, apellido, mail, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.mail=mail
        self.edad=edad

    def describir_usuario(self):
        print(f"tu usuario es {self.nombre}, tu apellido es {self.apellido}, tu mail es {self.mail}, y tu edad es {self.edad}")
    def saludar_usuario(self):
        print(f"Hola {self.nombre} {self.apellido}, te enviamos un mensaje a tu mail {self.mail} para hablarte de tu fiesta de {self.edad} años")
    
usuario1= usuario("jorge","flores","nicoyjorge10@gmail.com","17")
usuario2= usuario("salome","parada","salomenomeacuerdo@gmail.com","16")
usuario3= usuario("zacarias","ocampos","zacarias99@gmail.com","18")
usuario4= usuario("toloza","rodrigo","skibtolozo@gmail.com","17")
usuario1.saludar_usuario()
usuario2.saludar_usuario()
usuario3.saludar_usuario()
usuario4.saludar_usuario()
usuario1.describir_usuario()
usuario2.describir_usuario()
usuario3.describir_usuario()
usuario4.describir_usuario()
"""
"""
7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.
class Usuario:
    def __init__(self,nombre):
        self.nombre =nombre
class Admin(Usuario):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.privilegios = [
            "puede postear en el foro",
            "puede borrar un post",
            "puede banear usuario"
        ]
    def mostrar_privilegios(self):
        print(f"Privilegios de {self.nombre}:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")
admin1 = Admin("toloza")
admin1.mostrar_privilegios()
"""




"""8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
el método para mostrar privilegios.


class Privilegios:
    def __init__(self):
        self.privilegios = [
            "puede agregar un usuario",
            "puede eliminar un usuario",
            "puede modificar un usuario",
            "puede ver todos los usuarios",
            "puede gestionar contenido"
        ]
    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")
class Admin:
    def __init__(self, nombre):
        self.nombre = nombre
        self.privilegios = Privilegios() 
    def mostrar_privilegios(self):
        self.privilegios.mostrar_privilegios()  
admin = Admin("zacañas")
admin.mostrar_privilegios()
"""
"""9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
funcionó

from restaurante import Restaurante


mi_restaurante = Restaurante("villa lavalle delux", "Comida jujeña")
mi_restaurante.describir_restaurante()
mi_restaurante.abrir_restaurante()
"""


"""
10) (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. ¿Qué se necesita para que funcione la
importación?


from restaurante import Heladeria
mi_heladeria = Heladeria("Helados elaos", "Heladería", ["Vainilla", "Chocolate", "Fresa"])

mi_heladeria.describir_restaurante()
mi_heladeria.mostrar_sabores()
mi_heladeria.abrir_restaurante()
"""