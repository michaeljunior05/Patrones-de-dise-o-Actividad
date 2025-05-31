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


