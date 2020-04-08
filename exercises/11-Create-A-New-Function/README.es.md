# `11` Crear una nueva función

Como sabes, las funciones son un bloque de código útil que puedes reutilizar tantas veces 
como necesites o quieras. En el último ejercicio, tenías una función que recibía dos parámetros 
(dos entradas) y devolvía la suma de ellos. Así:

```py
def add_numbers(a, b):
  print(a + b)
```

Pero Python viene con un conjunto de funciones "predefinidas" que puedas usar, por ejemplo:

```py
import random
# Generates a random number between
# a given positive range
r1 = random.randint(0, 10)
print("Random number between 0 and 10 is % s" % (r1))
```

Puedes usar la función randint para obtener un número decimal aleatorio.
**randint()** es una función incorporada del módulo `random` en Python3.
El módulo random da acceso a varias funciones útiles y una de ellas
 es capaz de generar números aleatorios, que es **randint()**.

## 📝 Instrucciones:

1. Por favor, ahora, crea una función llamada **generate_random** que imprima Y devuelva un número 
aleatorio entre 0 y 9 cada vez que sea invocada.

## 💡 Sugerencia:

- Una posible solución involucra el uso de dos funciones predefinidas: las funciones **randint** o **randrange**.
- No olvides importar `random`
- Puedes consultar la documentación en: https://docs.python.org/3/library/random.html#functions-for-integers


