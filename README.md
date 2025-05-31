# Patrones-de-diseño-Actividad:

## Ejercicio 1:
Investigar y documentar críticas a los patrones de diseño. Mencione ejemplos concretos.

## Ejercicio 2:
Seleccione 3 patrones de diseño e implementarlos en Python. Arme ejemplos concretos de uso. Lo ideal es 
elegir un patrón de cada clasificación.

## Ejercicio 3:
Piense en 3 problemas habituales de su vida diaria en los cuales podría aplicar patrones de diseño.

## Ejercicio 4:
Los patrones de diseño suelen poseer distintos nombres o denominaciones. Busque y arme una tabla con 
los posibles distintos nombres usados.

## Ejercicio 5:
 ¿Qué son los antipatrones de diseño? Ejemplifique algunos casos.

## Ejercicio 6:
Investigue el uso de otras buenas prácticas, como por ejemplo SOLID.

# Resolucion:

## Ejercicio 1:

### Criticas a los Patrones de diseño:
Aunque los patrones de diseño son una herramienta fundamental en la programación, no siempre son la solución ideal.Su aplicacion excesiva o incorrecta puede traer mas problemas que ventajas.

- Complejidad innecesaria.
Uno de los problemas principales es la tendencia a la sobreingeniería. A veces, usamos patrones donde una solución más sencilla bastaría. Esto añade capas de complejidad al código, haciendo que sea más difícil de entender, mantener y corregir errores.
 - Ejemplo:
    Usar un Factory Method para crear objetos que casi nunca cambian, en lugar de simplemente crearlos de forma directa. La simplicidad se pierde al introducir interfaces y clases adicionales sin necesidad.
- Curva de aprendizaje y mal uso.
  Comprender y aplicar correctamente los patrones requiere tiempo y experiencia. Si los desarrolladores no los entienden bien, pueden implementarlos de forma incorrecta, lo que compromete la calidad del software. Además, en lenguajes de programación modernos, algunas funcionalidades hacen que ciertos patrones resulten redundantes o menos eficientes.
 - Ejemplo:
   El patrón Strategy, que permite intercambiar algoritmos, puede ser reemplazado en muchos lenguajes (como Python o Java 8+) simplemente pasando funciones como argumentos. No es necesario crear clases separadas para cada estrategia.

- Dogmatismo y "Por si acaso"
Hay una tendencia a aplicar los patrones de forma rígida, sin adaptarlos al contexto específico del proyecto. Esto lleva a un código menos flexible y más difícil de modificar. Otra mala práctica es añadir patrones pensando en cambios futuros que quizás nunca ocurran, una filosofía conocida como "You Ain't Gonna Need It" (YAGNI).
 - Ejemplo:
   Implementar una compleja jerarquía de Abstract Factory y Factory Method para un producto que actualmente solo tiene una variación, solo porque "tal vez en el futuro" necesite más. Esto genera código innecesario.


## Ejercicio 2: (Estan en el archivo .py)


## Ejercicio 3:

### 1. Preparar el desayuno de la familia (Patrón Factory Method)

Imagina que cada miembro de tu familia tiene una preferencia diferente para el desayuno: uno quiere tostadas, otro cereales y tú, quizás, huevos revueltos. La forma de preparar cada uno es distinta.

- El Problema: Cada mañana, tienes que recordar los pasos específicos para cada desayuno, y si alguien pide algo nuevo, tienes que aprender una nueva "receta". Esto puede ser ineficiente y propenso a errores si estás medio dormido.
- La Solución con Factory Method: Podrías tener una "fábrica de desayunos". En lugar de preparar cada desayuno directamente, delegas la "creación" de cada tipo a una "receta" específica.
-- Tendrías una interfaz genérica de "desayuno" (que podría ser simplemente "lo que se come").
-- Luego, una "receta de tostadas", una "receta de cereales" y una "receta de huevos".
-- Cuando alguien pide un desayuno, la "fábrica" simplemente invoca la "receta" correspondiente, y esta se encarga de todos los pasos para preparar el desayuno específico sin que tú tengas que saber todos los detalles internos de cada uno. Si un nuevo miembro de la familia quiere tortitas, solo creas una "receta de tortitas" y la añades a tu "fábrica", sin cambiar cómo gestionas los otros desayunos.


### 2. Vestirte para diferentes ocasiones (Patrón Strategy)

Tu forma de vestir cambia drásticamente si vas al gimnasio, a una reunión de trabajo o a una fiesta.

- El Problema: Tienes que decidir qué ropa ponerte en función de la ocasión. Si la ocasión cambia, o si añades un nuevo tipo de evento a tu vida (como empezar clases de baile), tienes que volver a pensar todo el atuendo desde cero.
- La Solución con Strategy: Podrías tener un "sistema" para seleccionar tu atuendo basado en la ocasión.
-- Tendrías una interfaz "estrategia de vestir" (por ejemplo, "CómoVestirPara").
-- Luego, distintas "estrategias concretas": "VestirParaGimnasio", "VestirParaTrabajo", "VestirParaFiesta". Cada una sabe qué tipo de ropa (y accesorios) son adecuados para su propósito.
-- Cuando te preparas, simplemente "seleccionas la estrategia" para la ocasión actual (ej. "hoy voy a usar la estrategia 'VestirParaTrabajo'"). Tu "sistema de vestimenta" simplemente aplica esa estrategia sin necesidad de que tú recuerdes cada detalle de cada atuendo. Si mañana vas a un picnic, solo necesitas una nueva estrategia "VestirParaPicnic" y tu "sistema" ya sabrá cómo aplicarla.

### 3. Gestionar tus notificaciones del celular (Patrón Observer)

Constantemente recibes notificaciones de diferentes aplicaciones: mensajes de texto, correos, noticias, redes sociales, etc.

- El Problema: Necesitas una forma de que las aplicaciones te "avisen" de algo nuevo sin que tú tengas que estar revisándolas activamente todo el tiempo. Además, quieres poder decidir qué aplicaciones te notifican y cuáles no.
- La Solución con Observer: Tu celular actúa como el "sujeto" que emite notificaciones, y cada aplicación es un "observador".
-- El "sujeto" (tu celular) tiene una lista de "observadores" (las aplicaciones que te han pedido que les envíes notificaciones).
-- Cuando sucede un evento (llega un nuevo mensaje, hay una noticia de última hora), el celular "notifica" a todos los "observadores" que están "suscritos" a ese tipo de evento.
-- Cada "observador" (aplicación), al recibir la notificación, reacciona de su propia manera (muestra un ícono, reproduce un sonido, etc.). Puedes "suscribirte" o "desuscribirte" fácilmente de las notificaciones de una aplicación sin afectar cómo funcionan las otras.

## Ejercicio 4

| Nombre principal | Clasificacion | Nombres Alternativos |
|---|---|---|
| Abstract Factory	 | Creacional | Kit, Fábrica de Fábricas, Fábrica Abstracta
| Builder | Creacional | Constructor, Separador de Construcción 
| Factory Method | Creacional | Método de Fábrica, Fábrica Virtual
| Prototype | Creacional | Clonador, Prototipo
| Singleton | Creacional | Instancia Única, Objeto Único, Dios Objeto (a veces como antipatrón)
| Adapter | Estructural | Wrapper, Envoltorio, Clase Adaptadora, Object Adapter
| Bridge | Estructural | Puente, Handle/Body
| Composite | Estrctural | Composición, Objeto Compuesto
| Decorator | Estructural | Envoltorio, Decorador de Objetos, Smart Proxy
| Facade | Estructural | Fachada, Interfaz Simple, Sistema Subsistema
| Flyweight | Estructural | Peso Ligero, Objeto Compartido
| Proxy | Estructural | Sustituto, Apoderado, Delegado, Wrapper
| Chain of Responsibility | Comportamiento | Cadena de Responsabilidad, Pipeline
| Command | Comportamiento | Acción, Transacción
| Interpreter | Comportamiento | Interprete
| Iterator | Comportamiento | Cursor, Enumerador
| Mediator | Comportamiento | Intermediario, Centro de Control
| Memento | Comportamiento | Token, Instantánea
| Observer | Comportamiento | Publicador-Subscriptor, Pub-Sub, Dependiente
| State | Comportamiento | Objeto Estado, Máquina de Estados Objeto
| Strategy | Comportamiento | Política, Algoritmo Intercambiable
| Template Method | Comportamiento | Metodo Plantilla |
| Visitor | Comportamiento | Visitante |



## Ejercicio 5

¿Qué son los Antipatrones de Diseño?
Mientras que un patrón de diseño es una solución probada y recurrente a un problema común en el diseño de software, un antipatrón de diseño es lo opuesto. Un antipatrón es una solución comúnmente aplicada a un problema que, en realidad, resulta ineficaz y contraproducente, llevando a consecuencias negativas y a menudo difíciles de revertir en el sistema de software.

En otras palabras, los antipatrones son "malas prácticas" o "soluciones fallidas" que se repiten con frecuencia en el desarrollo de software. Reconocerlos es tan importante como conocer los patrones, ya que ayuda a evitar errores comunes que pueden llevar a:
- Mayor complejidad: El código se vuelve más difícil de entender y mantener.
- Menor rendimiento: La aplicación puede volverse lenta o ineficiente.
- Baja reusabilidad: Los componentes son difíciles de reutilizar en otras partes del sistema o en otros proyectos.
- Dificultad en las pruebas: El código es complicado de probar de forma aislada.
- Acoplamiento excesivo: Los componentes dependen demasiado unos de otros, haciendo los cambios muy riesgosos.
- Baja cohesión: Las clases o módulos tienen responsabilidades mezcladas o poco relacionadas.

Ejemplos Comunes de Antipatrones de Diseño
Aquí te presento algunos de los antipatrones más conocidos y sus implicaciones:

1. El Objeto Dios (God Object / God Class)
- Descripción: Una clase que centraliza demasiadas responsabilidades y funcionalidades. Intenta hacer "demasiadas cosas" y tiene un conocimiento o control excesivo sobre otras partes del sistema.

- Problema: Viola el Principio de Responsabilidad Única (SRP). Se convierte en un cuello de botella, es extremadamente difícil de probar, mantener y modificar. Cualquier cambio en una pequeña parte de su funcionalidad puede tener efectos secundarios inesperados en otras partes.

- Ejemplo Concreto:
Imagina una clase GestorSistema en una aplicación. Esta clase se encarga de:

-Manejar la autenticación de usuarios.

-Gestionar la base de datos (conexiones, consultas).

-Procesar pagos.

-Enviar correos electrónicos de notificación.

-Generar informes.

Si necesitas cambiar cómo se gestionan los pagos, es probable que tengas que modificar esta clase GestorSistema masiva, arriesgándote a introducir errores en la autenticación o el envío de correos. Además, probar solo la funcionalidad de pago de esta clase sería muy complicado.

2. Lava Flow (Flujo de Lava)
- Descripción: Partes del código que son "intocables" o extremadamente difíciles de modificar porque nadie entiende completamente cómo funcionan o por qué están ahí. A menudo, son secciones de código antiguas, mal documentadas o con dependencias ocultas.

- Problema: Impide la evolución del software, aumenta el riesgo de introducir errores al intentar modificarlas y reduce la productividad, ya que los desarrolladores evitan interactuar con ellas.

- Ejemplo Concreto:
En un sistema heredado, existe un módulo CalculadorImpuestosLegado. Nadie en el equipo actual sabe exactamente cómo calcula los impuestos para todas las casuísticas, solo saben que "funciona" y que cualquier intento de refactorizarlo o tocarlo ha causado problemas en el pasado. El código está lleno de lógica compleja, sin comentarios y con nombres de variables crípticos. Es como un flujo de lava solidificado: está ahí, es parte del paisaje, pero es intocable.

3. Acoplamiento de Concreto (Hard-coded Dependencies / Concrete Coupling)
Descripción: Un módulo o clase depende directamente de la implementación concreta de otro módulo o clase, en lugar de depender de una interfaz o abstracción.

- Problema: Viola el Principio de Inversión de Dependencias (DIP). Hace que el código sea rígido y difícil de cambiar. Si la implementación concreta cambia, todas las clases que dependen de ella deben ser modificadas. Dificulta enormemente las pruebas unitarias.

- Ejemplo Concreto:
Tienes una clase ProcesadorPedidos que necesita guardar los pedidos en una base de datos. En lugar de depender de una interfaz RepositorioPedidos, la clase ProcesadorPedidos crea directamente una instancia de BaseDeDatosMySQL:





```
python 
class BaseDeDatosMySQL:
    def guardar_pedido(self, pedido):
        print(f"Guardando pedido en MySQL: {pedido}")

class ProcesadorPedidos:
    def __init__(self):
        # Acoplamiento directo a la implementación concreta
        self.db = BaseDeDatosMySQL()

    def procesar(self, pedido):
        # ... lógica de procesamiento ...
        self.db.guardar_pedido(pedido)
```

Si más tarde decides cambiar a PostgreSQL o a una base de datos NoSQL, tendrías que modificar la clase ProcesadorPedidos (y cualquier otra clase que dependa directamente de BaseDeDatosMySQL). Además, es muy difícil probar ProcesadorPedidos sin una base de datos MySQL real.

4. Bola de Barro (Spaghetti Code / Big Ball of Mud)
- Descripción: Un sistema con una estructura desorganizada, sin una arquitectura clara, donde los componentes están fuertemente acoplados entre sí y la lógica de negocio se mezcla con la lógica de presentación y persistencia.

- Problema: Es el resultado de la falta de diseño o de un diseño pobre. El sistema es extremadamente difícil de entender, mantener, escalar y refactorizar. Cada cambio es un riesgo de romper algo más.

- Ejemplo Concreto:
Un sistema web donde el código HTML, JavaScript, las consultas SQL y la lógica de negocio están todos mezclados en archivos PHP monolíticos. Una función puede acceder directamente a variables globales, modificar la interfaz de usuario y guardar datos en la base de datos, todo en el mismo bloque de código. No hay separación de capas ni de responsabilidades.

5. El Problema del Yo-Yo (Yo-Yo Problem)
- Descripción: Una jerarquía de herencia excesivamente profunda, donde para entender el comportamiento de un método, tienes que "saltar" arriba y abajo en la jerarquía de clases (como un yo-yo) para seguir la cadena de llamadas a super().

- Problema: Dificulta la comprensión del código, el debugging y el mantenimiento. Los cambios en una clase base pueden tener efectos en cascada difíciles de prever.

- Ejemplo Concreto:

```
python
class Animal:
    def hacer_sonido(self):
        print("Sonido genérico de animal")

class Mamifero(Animal):
    def hacer_sonido(self):
        super().hacer_sonido()
        print("Sonido de mamífero")

class Perro(Mamifero):
    def hacer_sonido(self):
        super().hacer_sonido()
        print("Guau guau")

class Labrador(Perro):
    def hacer_sonido(self):
        super().hacer_sonido()
        print("Guau guau (Labrador)")

# Para entender qué hace Labrador.hacer_sonido(),
# tienes que seguir la cadena hasta Animal.
lab = Labrador()
lab.hacer_sonido()
```
Si esta jerarquía se extiende a 10 o 15 niveles, seguir el flujo de un método se vuelve una tarea tediosa y propensa a errores.

Reconocer y evitar estos antipatrones es fundamental para construir software robusto, mantenible y escalable.
