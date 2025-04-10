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
mi_heladeria.abrir_restaurante()