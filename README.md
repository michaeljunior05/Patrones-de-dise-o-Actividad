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



   

