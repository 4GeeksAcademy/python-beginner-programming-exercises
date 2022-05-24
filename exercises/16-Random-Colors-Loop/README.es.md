# `16` Random Colors (Loop)

Hemos creado una función que devuelve un color basado en un número entre 0 y 3 (cualquier número diferente, debe retornar el color `black`).

Digamos que somos profesores en un aula con 10 estudiantes y queremos asignar a **cada estudiante** un color aleatorio entre `red` (rojo), `yellow` (amarillo), `blue` (azul) y `green` (verde).

(solo 1 color por estudiante)

## 📝 Instrucciones:

1. Cambia la función `get_allStudentColors` para que devuelva una lista con 10 colores, en donde cada elemento de la lista representa el color asignado a cada estudiante.

## 💡 Pistas:

+ Tienes 10 estudiantes, necesitas que el ciclo itere 10 veces y añadir estos valores a una lista.

+ En cada iteración, genera un número aleatorio entre 0 y 3 usando la función `randint()` que hemos visto en ejercicios anteriores.

+ Usa la función `get_color`, en este ejercicio para saber qué color le corresponde al número obtenido.

+ Llama (ejecuta) la funcion `get_allStudentColors` e imprime su resultado en la consola.