# Ejercicio 2
# Patron Creacional: Factory Method
#El patrón Factory Method (Método de Fábrica) define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase instanciar. 
# Permite que una clase delegue la responsabilidad de instanciar un objeto a sus subclases.

# Caso de Uso: Imagina que tienes una aplicación de logística que necesita calcular el costo de envío para diferentes tipos de transporte
# (terrestre, aéreo, marítimo). Cada tipo de transporte tiene su propia lógica de cálculo de costo.

from abc import ABC, abstractmethod

# Interfaz del Producto
class Transporte(ABC):
    @abstractmethod
    def entregar(self) -> str:
        pass

# Productos Concretos
class Camion(Transporte):
    def entregar(self) -> str:
        return "Entrega por tierra en camión."

class Avion(Transporte):
    def entregar(self) -> str:
        return "Entrega por aire en avión."

class Barco(Transporte):
    def entregar(self) -> str:
        return "Entrega por mar en barco."

# Creador (Interfaz del Creador)
class CreadorEnvio(ABC):
    @abstractmethod
    def crear_transporte(self) -> Transporte:
        pass

    def planificar_entrega(self) -> str:
        # Aquí podria haber lógica de negocio que utiliza el transporte
        transporte = self.crear_transporte()
        resultado = f"Planificando envío... {transporte.entregar()}"
        return resultado

# Creadores Concretos
class CreadorEnvioTerrestre(CreadorEnvio):
    def crear_transporte(self) -> Transporte:
        return Camion()

class CreadorEnvioAereo(CreadorEnvio):
    def crear_transporte(self) -> Transporte:
        return Avion()

class CreadorEnvioMaritimo(CreadorEnvio):
    def crear_transporte(self) -> Transporte:
        return Barco()


# El cliente no necesita saber los detalles de cómo se crea el transporte,
# solo interactúa con la interfaz del creador.
# Si agregamos un nuevo tipo de transporte (ej. Drone), solo necesitamos
# crear un nuevo CreadorEnvioDrone y una clase Drone.













# Patrón Estructural: Decorator
# El patrón Decorator (Decorador) permite añadir nuevas funcionalidades a un objeto existente dinámicamente, sin alterar su estructura. 
# Funciona envolviendo el objeto original con un objeto "decorador" que añade el comportamiento extra.
# Caso de Uso: Imagina una aplicación de cafetería donde puedes pedir un café y añadirle extras (leche, azúcar, nata, etc.), cada uno con un costo adicional.

from abc import ABC, abstractmethod

# Componente (Interfaz)
class Cafe(ABC):
    @abstractmethod
    def get_costo(self) -> float:
        pass

    @abstractmethod
    def get_descripcion(self) -> str:
        pass

# Componente Concreto
class CafeSimple(Cafe):
    def get_costo(self) -> float:
        return 2.0

    def get_descripcion(self) -> str:
        return "Café simple"

# Decorador (Clase Base del Decorador)
class DecoradorCafe(Cafe, ABC):
    def __init__(self, cafe: Cafe):
        self._cafe = cafe

    @abstractmethod
    def get_costo(self) -> float:
        pass

    @abstractmethod
    def get_descripcion(self) -> str:
        pass

# Decoradores Concretos
class Leche(DecoradorCafe):
    def __init__(self, cafe: Cafe):
        super().__init__(cafe)
        self.costo_extra = 0.5
        self.descripcion_extra = "con leche"

    def get_costo(self) -> float:
        return self._cafe.get_costo() + self.costo_extra

    def get_descripcion(self) -> str:
        return f"{self._cafe.get_descripcion()} {self.descripcion_extra}"

class Azucar(DecoradorCafe):
    def __init__(self, cafe: Cafe):
        super().__init__(cafe)
        self.costo_extra = 0.2
        self.descripcion_extra = "con azúcar"

    def get_costo(self) -> float:
        return self._cafe.get_costo() + self.costo_extra

    def get_descripcion(self) -> str:
        return f"{self._cafe.get_descripcion()} {self.descripcion_extra}"

class Nata(DecoradorCafe):
    def __init__(self, cafe: Cafe):
        super().__init__(cafe)
        self.costo_extra = 1.0
        self.descripcion_extra = "con nata"

    def get_costo(self) -> float:
        return self._cafe.get_costo() + self.costo_extra

    def get_descripcion(self) -> str:
        return f"{self._cafe.get_descripcion()} {self.descripcion_extra}"





# Patrón Comportamental: Strategy
# El patrón Strategy (Estrategia) define una familia de algoritmos, encapsula cada uno de ellos y los hace intercambiables. 
# Permite que el algoritmo varíe independientemente de los clientes que lo usan.

# Caso de Uso: Imagina una aplicación de comercio electrónico que ofrece diferentes métodos de pago (tarjeta de crédito, PayPal, transferencia bancaria), 
#cada uno con su propia lógica de procesamiento.

from abc import ABC, abstractmethod

# Interfaz de la Estrategia
class EstrategiaPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float):
        pass

# Estrategias Concretas
class PagoTarjetaCredito(EstrategiaPago):
    def procesar_pago(self, monto: float):
        print(f"Procesando pago de ${monto:.2f} con Tarjeta de Crédito.")
        # Lógica real de procesamiento de tarjeta...

class PagoPayPal(EstrategiaPago):
    def procesar_pago(self, monto: float):
        print(f"Procesando pago de ${monto:.2f} con PayPal.")
        # Lógica real de procesamiento de PayPal...

class PagoTransferenciaBancaria(EstrategiaPago):
    def procesar_pago(self, monto: float):
        print(f"Procesando pago de ${monto:.2f} con Transferencia Bancaria.")
        # Lógica real de procesamiento de transferencia...

# Contexto
class CarritoCompras:
    def __init__(self, estrategia_pago: EstrategiaPago):
        self._estrategia = estrategia_pago
        self._items = []

    def agregar_item(self, nombre: str, precio: float):
        self._items.append({"nombre": nombre, "precio": precio})

    def set_estrategia_pago(self, estrategia: EstrategiaPago):
        self._estrategia = estrategia

    def checkout(self):
        monto_total = sum(item["precio"] for item in self._items)
        print(f"\nArtículos en el carrito: {self._items}")
        print(f"Total a pagar: ${monto_total:.2f}")
        self._estrategia.procesar_pago(monto_total)









