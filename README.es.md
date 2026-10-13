<!-- hide -->
<div align="center">

# Aprende Python Interactivamente (Principiante)

![Portada del curso con el texto "Learn Python Beginner interactive" junto al logo azul y amarillo de Python](https://raw.githubusercontent.com/4GeeksAcademy/python-beginner-programming-exercises/HEAD/.learn/assets/preview.png)

[![Tutorial interactivo](https://img.shields.io/badge/4Geeks_Academy-Tutorial_interactivo-2563eb?style=flat-square)](https://4geeks.com/es/interactive-exercise/python-beginner-programming-exercises)
[![Autocorregido con LearnPack](https://img.shields.io/badge/LearnPack-21_ejercicios_autocorregidos-2563eb?style=flat-square)](https://learnpack.co)
[![Abrir en GitHub Codespaces](https://img.shields.io/badge/Abrir_en-GitHub_Codespaces-fb5a1f?style=flat-square&logo=github&logoColor=white)](https://codespaces.new/?repo=4GeeksAcademy/python-beginner-programming-exercises)

</div>
<!-- endhide -->

Aprende Python Interactivamente es un curso para principiantes con 21 retos autocorregidos que se resuelven dentro del editor de código. Empiezas imprimiendo `Hello World!` y terminas escribiendo FizzBuzz, una función de ruleta rusa y la canción completa de las 99 botellas. Dura unas 10 horas, no exige experiencia previa programando y 19 de los ejercicios traen un vídeo explicativo paso a paso.

<!-- hide -->
## 📋 Sobre este tutorial

- **Dificultad**: fácil (`difficulty: "easy"` en `learn.json`)
- **Duración**: unas 10 horas
- **Ejercicios**: 22 carpetas — 1 página de bienvenida y 21 retos de código
- **Tecnologías**: Python 3, variables, cadenas, condicionales, funciones, bucles
- **Corrección**: automática, 21 ficheros `test.py` que se ejecutan con pytest
- **Vídeos**: 19 explicaciones de ejercicio más 1 vídeo de introducción
- **Idiomas**: [English](https://github.com/4GeeksAcademy/python-beginner-programming-exercises/blob/HEAD/README.md) · [Español](https://github.com/4GeeksAcademy/python-beginner-programming-exercises/blob/HEAD/README.es.md)
<!-- endhide -->

## 🎯 ¿Qué vas a aprender?

Los 21 retos presentan una idea cada vez, y ninguna idea se queda suelta: todas vuelven a aparecer en un ejercicio posterior.

- **La consola**: `print()` como la vía por la que un programa te responde y como tu principal herramienta para depurar.
- **Variables**: declararlas, asignarles cadenas y números, e imprimir varias en una sola llamada a `print()` separándolas con comas.
- **Aritmética**: multiplicar con `*` y guardar el resultado en una variable.
- **Entrada del usuario**: leer un valor con `input()` y trabajar con una variable cuyo contenido no conoces de antemano.
- **Concatenación de cadenas**: unir textos con el operador `+`, hasta construir un documento HTML entero a partir de 8 variables sueltas.
- **Condicionales**: cadenas de `if...else`, operadores relacionales (`>`, `<`, `==`, `!=`, `>=`, `<=`) y tramos de precios con varias ramas.
- **El módulo `random`**: `randint(min, max)` y `randrange(inicio, fin)`, y la diferencia entre un límite superior inclusivo y uno exclusivo.
- **Funciones**: llamar a una función escrita por otra persona, definir la tuya, pasar parámetros y distinguir `return` de `print`.
- **Bucles**: `for` con `range()`, repetir una acción cientos de veces y combinar bucles con condicionales.
- **Listas**: construir una lista elemento a elemento dentro de un bucle.

## 👀 ¿Qué vas a construir?

Cada ejercicio es un programa de Python real y ejecutable. Estos son los 21 retos evaluados, en orden:

- **`01` Console** — imprimir `Hello World!` en la terminal.
- **`02` Declare Variables** — declarar una variable con el valor `"Yellow"` e imprimirla.
- **`03` Print more Variables** — declarar `color = "red"` e `item = "marker"` e imprimir ambas en una sola llamada.
- **`04` Multiply Two Values** — guardar `2345 * 7323` en una variable e imprimir el resultado.
- **`05` User Inputed Values** — pedir la edad al usuario e imprimirla sumándole 10 años.
- **`06` String Concatenation** — dar valor a dos variables para que `my_var1 + my_var2` imprima `Hello World`.
- **`07` Create a Basic HTML** — concatenar 8 variables dadas hasta formar `<html><head><title></title></head><body></body></html>`.
- **`08.1` Your First If** — responder distinto según si el usuario tiene más de $100, más de $50 o $50 o menos.
- **`08.2` How Much The Wedding Costs** — calcular el precio de un catering de boda en cuatro tramos de invitados, desde $4.000 para un máximo de 50 hasta $20.000 para más de 200.
- **`09` Random Numbers** — devolver un número entero aleatorio entre 1 y 10 en lugar de un decimal.
- **`10` Calling Your First Function** — llamar a la función `is_odd` que ya viene escrita pasándole `45345` e imprimir lo que devuelve.
- **`10.1` Creating Your First Function** — rellenar el cuerpo de `add_numbers(a, b)` para que el programa imprima `7`.
- **`11` Create A New Function** — escribir `generate_random()`, que devuelve un número aleatorio entre 0 y 9.
- **`12` Rand From One to Twelve** — usar `randrange()` para generar enteros del 1 al 12, ambos incluidos.
- **`13` Your First Loop** — coger un bucle que cuenta hasta 9 y hacer que cuente hasta 11.
- **`14` Create A For Loop** — imprimir "I will ask questions if I am stuck" exactamente 300 veces.
- **`15` Looping With FizzBuzz** — el clásico de las entrevistas: imprimir del 1 al 100 con `Fizz`, `Buzz` y `FizzBuzz`.
- **`16` Random Colors (Loop)** — asignar a cada uno de 10 alumnos un color aleatorio de entre cuatro y devolver la lista resultante.
- **`17` Russian Roulette** — completar `fire_gun` para que compare la posición de la bala con la del tambor de un revólver de 6 recámaras.
- **`18` The Beatles** — escribir `sing()` para que imprima línea a línea el estribillo final de "Let It Be".
- **`19` Bottles Of Milk** — escribir `number_of_bottles()`, que imprime las 100 estrofas de la canción de las 99 botellas, singular incluido.

El ejercicio `00` es una página de bienvenida sin código: enumera los conceptos que vienen y enlaza a lecturas introductorias.

## 🎓 ¿Qué necesitas antes de empezar?

- **Experiencia programando**: ninguna. El primer reto es una sola llamada a `print()`, y el tutorial explica qué es una consola antes de pedirte que la uses.
- **Conocimientos de Python**: ninguno. Cada función que se usa (`print`, `input`, `int`, `str`, `range`, `randint`, `randrange`) se presenta en el ejercicio que la necesita.
- **Software, opción en la nube**: basta una cuenta de GitHub. Codespaces monta el entorno a partir del `.devcontainer` del repositorio, que instala por ti Python 3.10, Node 22, LearnPack y pytest.
- **Software, opción local**: Python 3 y Node.js 14 o superior, además de los paquetes `pytest`, `pytest-testdox` y `mock`.
- **Tiempo**: unas 10 horas en total, es decir, alrededor de 30 minutos por reto si ves los vídeos.
- **Idioma**: cada ejercicio incluye `README.md` en inglés y `README.es.md` en español.

## ✅ ¿Cómo funciona la corrección automática?

La corrección es real, no decorativa: 21 de las 22 carpetas de ejercicio contienen un fichero `test.py`, y se ejecutan con pytest.

- **Escribes tu respuesta en `app.py`**, el único fichero que debes tocar. Marcas como `# ✅↓ Write your code here ↓✅` y `# ❌ ↓ DON'T CHANGE THE CODE BELOW ↓ ❌` te señalan la zona editable.
- **Pulsas Run** para ejecutar el programa y ver su salida, y el botón de feedback para lanzar los tests.
- **Cada test lleva una etiqueta legible** escrita con `@pytest.mark.it(...)`, así que un fallo se lee como "The function `fizz_buzz` should exist" o "Your function needs to print the correct output" en vez de como una traza de error.
- **Se usan dos tipos de comprobación**: las de salida, que capturan lo que imprime tu programa y lo comparan con el texto esperado, y las de código fuente, que con expresiones regulares verifican que de verdad usaste la técnica que se enseña, por ejemplo que aparezca la palabra `for` en tu solución de FizzBuzz.
- **Junto a cada ejercicio evaluado hay un `solution.hide.py`**, así que siempre tienes una solución resuelta disponible cuando ya lo hayas intentado por tu cuenta.

![Captura del panel de instrucciones de LearnPack dentro de VS Code mostrando el ejercicio 01 Console, con una flecha roja señalando el botón Run junto a los botones Get feedback y Reset](https://raw.githubusercontent.com/4GeeksAcademy/python-beginner-programming-exercises/HEAD/.learn/assets/run-exercise.png)

## 💡 ¿Qué errores conviene evitar?

Casi todos los tests que fallan en este tutorial se explican por un puñado de causas:

- **Llegar al resultado correcto por el camino equivocado.** El ejercicio `12` solo acepta `random.randrange(1, 13)`; `randint(1, 12)` imprime exactamente los mismos números y aun así falla. El `15` exige que aparezca la palabra `for` en tu fichero, así que un `while` que imprime un FizzBuzz impecable queda rechazado.
- **Confundir `return` con `print`.** El ejercicio `19` pide explícitamente imprimir la letra, mientras que el `17` espera que `fire_gun` devuelva las cadenas `You are dead!` y `Keep playing!`. Intercambiarlos rompe el test aunque en pantalla parezca que todo funciona.
- **Equivocarte en el texto exacto.** Las comparaciones incluyen mayúsculas, puntuación y espacios: `"Yellow"` no es `"yellow"`, y la última estrofa de la canción cambia a "no more bottles" y "Go to the store and buy some more".
- **Olvidar el singular.** La canción de las botellas pasa de "bottles" a "bottle" al llegar a 1, y esa es la razón más habitual de que falle su último test.
- **Errores de uno en los rangos.** `randint(a, b)` incluye ambos extremos, `randrange(a, b)` excluye el último, y el bucle del ejercicio `13` tiene que llegar a 11, no quedarse en 10.
- **No llamar a tu propia función.** Varios tests comprueban que la función esté definida y además invocada; por ejemplo, que `print(get_randomInt())` aparezca de verdad en `app.py`.

## ❓ Preguntas frecuentes

### ¿Cuánto se tarda en aprender lo básico de Python con estos ejercicios?

El paquete está estimado en 10 horas repartidas entre 21 retos. La mayoría son unas pocas líneas de código; los que más cuestan son FizzBuzz, la lista de colores aleatorios y la canción de las 99 botellas, porque su salida esperada se compara carácter a carácter.

### ¿Hace falta saber programar antes de empezar?

No. El tutorial está marcado con dificultad `easy` y arranca imprimiendo una sola línea de texto. Los conceptos llegan en orden — consola, variables, entrada, condicionales, aleatoriedad, funciones, bucles, listas — y cada uno se reutiliza en un ejercicio posterior.

### ¿Tengo que instalar Python en mi ordenador?

No si usas Codespaces: el `.devcontainer` de este repositorio provisiona automáticamente Python 3.10, Node 22, LearnPack y pytest, y los ejercicios se abren en el navegador. La instalación local también está soportada y necesita Python 3, Node.js 14 o superior y los paquetes `pytest`, `pytest-testdox` y `mock`.

### Mi código funciona pero el test falla igual. ¿Es normal?

Sí, y conviene entender por qué. Algunos tests inspeccionan tu código fuente con expresiones regulares para verificar que usaste la construcción concreta que se está enseñando, así que una respuesta correcta escrita de otra manera puede ser rechazada. Los propios autores describen la corrección como rígida y recomiendan tomarla como sugerencia, no como veredicto. Ante la duda, compara tu fichero con el `solution.hide.py` que hay junto al ejercicio.

### ¿Es gratis y puedo reutilizar el código?

Acceder no cuesta nada y el código que escribes es tuyo. El contenido, en cambio, no es open source: la [LICENSE](https://github.com/4GeeksAcademy/python-beginner-programming-exercises/blob/HEAD/LICENSE.md) reserva todos los derechos de propiedad intelectual y prohíbe republicar, vender, reproducir o redistribuir el material. Puedes usarlo para aprender y estudiar por tu cuenta, que es justo para lo que lo publica 4Geeks Academy.

### ¿Qué hago cuando termine?

Sigue por los paquetes a los que apunta el propio tutorial: una serie dedicada a [listas y bucles](https://4geeks.com/es/interactive-exercise/python-lists-loops-programming-exercises) y más de 20 [ejercicios de funciones](https://4geeks.com/es/interactive-exercise/python-functions-programming-exercises) con dificultad creciente. Los ejercicios `10.1`, `13` y `15` enlazan a ellos directamente.

<!-- hide -->
## 📚 Tutoriales relacionados

- [Ejercicios de listas y bucles en Python](https://4geeks.com/es/interactive-exercise/python-lists-loops-programming-exercises) — el paso natural después del ejercicio `13`.
- [Ejercicios de funciones en Python](https://4geeks.com/es/interactive-exercise/python-functions-programming-exercises) — más de 20 retos, referenciados desde los ejercicios `10` y `10.1`.
- [Vídeo de introducción del curso](https://www.youtube.com/watch?v=IXNSwnN-YqM) — el que enlaza `learn.json` para español.

## 🚀 Cómo empezar

Instalación en un clic, la opción recomendada:

[Abrir en GitHub Codespaces](https://codespaces.new/?repo=4GeeksAcademy/python-beginner-programming-exercises)

Cuando se abra VS Code, los ejercicios de LearnPack deberían arrancar solos. Si no lo hacen, escribe esto en la terminal:

```bash
$ learnpack start
```

> 💡 También puedes seguir el mismo tutorial en la web, en [4geeks.com](https://4geeks.com/es/interactive-exercise/python-beginner-programming-exercises).

## 💻 Instalación local

1. Instala [LearnPack](https://learnpack.co), Node.js 14+ y Python 3+:

   ```bash
   $ npm i @learnpack/learnpack -g && learnpack plugins:install @learnpack/python
   ```

2. Clona el repositorio y entra en la carpeta:

   ```bash
   $ git clone https://github.com/4GeeksAcademy/python-beginner-programming-exercises.git
   $ cd python-beginner-programming-exercises
   ```

3. Instala las dependencias de test y arranca, desde el mismo nivel en el que está `learn.json`:

   ```bash
   $ pip3 install pytest==6.2.5 pytest-testdox mock
   $ learnpack start
   ```

## 📚 Cómo están organizados los ejercicios

Cada ejercicio vive en su propia carpeta dentro de [`exercises/`](https://github.com/4GeeksAcademy/python-beginner-programming-exercises/tree/HEAD/exercises). Los 21 evaluados contienen:

- **`app.py`** — el fichero de entrada que editas y ejecutas.
- **`README.md`** — las instrucciones en inglés.
- **`README.es.md`** — las instrucciones en español.
- **`test.py`** — el script de corrección; no necesitas abrirlo.
- **`solution.hide.py`** — una solución resuelta, que LearnPack mantiene oculta hasta que la pides.

## 🤝 Colaboradores

Gracias a estas personas maravillosas ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

1. [Alejandro Sánchez (alesanchezr)](https://github.com/alesanchezr) — (programador) 💻, (idea) 🤔, (build-tests) ⚠️, (pull-request-review) 👀, (build-tutorial) ✅, (documentación) 📖
2. [Paolo Lucano (plucodev)](https://github.com/plucodev) — (reporte de bugs) 🐛, (programador) 💻, (traducción) 🌎
3. [Marco Gómez (marcogonzalo)](https://github.com/marcogonzalo) — (traducción) 🌎

Este proyecto sigue la especificación [all-contributors](https://github.com/kentcdodds/all-contributors). Toda contribución es bienvenida — consulta la [lista completa de colaboradores](https://github.com/4GeeksAcademy/python-beginner-programming-exercises/graphs/contributors).

Este y muchos otros ejercicios los construyen los alumnos del [Coding Bootcamp de 4Geeks Academy](https://4geeks.com/es/inicio). Conoce más sobre el [programa de Desarrollo Full Stack](https://4geeks.com/es/programas-de-carrera/desarrollo-full-stack) y el [programa de Ciencia de Datos y Machine Learning](https://4geeks.com/es/programas-de-carrera/ciencia-de-datos-ml).
<!-- endhide -->
