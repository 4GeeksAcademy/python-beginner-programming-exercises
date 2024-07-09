---
tutorial: "https://www.youtube.com/watch?v=6LhV15O9kvQ"
---

# `11` Create a New Function

Como sabes, las funciones son un bloque de código útil que puedes reusar tantas veces como necesites.

En el último ejercicio, tenías una función que recibía dos parámetros (dos entradas) y devolvía la suma de ellos. Así:

```py
def add_numbers(a, b):
    print(a + b)
```

Pero Python viene con un conjunto de funciones "pre-definidas" que puedes usar, por ejemplo:

```py
import random
# Genera un número aleatorio dentro de un rango positivo dado

r1 = random.randint(0, 10)
print("Random number between 0 and 10 is % s" % (r1))
```

Puedes usar la función `randint()` para obtener un número entero aleatorio. Esta es una función incorporada del **módulo random** en Python3.

El **módulo random** te da acceso a varias funciones útiles y una de ellas es, `randint()`, capaz de generar números aleatorios. 

## 📝 Instrucciones:

1. Por favor, crea una función llamada `generate_random` que devuelva un número aleatorio entre 0 y 9 cada vez que se llame.

2. Imprime el resultado que la función retorna al ser llamada.

## 💡 Pistas:

+ Una posible solución involucra el uso de una de dos funciones predefinidas: la función `randint` o `randrange`.

+ No olvides importar el módulo `random`.

+ Puedes consultar la documentación en: https://docs.python.org/3/library/random.html#functions-for-integers
