# `23` Objetos en Python

Con el tiempo te encontrarás con que quieres almacenar más información en menos espacio, especialmente si todo está relacionado. Por ejemplo:

Digamos que queremos representar vehículos en variables:

```py
car_1_Model = "corolla"
car_1_Make = "Toyota"
car_1_Color = "green"
car_1_Year = 2015

car_2_Model = "santa fe"
car_2_Make = "Hyundai"
car_2_Color = "purple"
car_2_Year = 2013
#... (captas la idea)
```

Hay un acercamiento optimizado para esto, se llaman objetos. Los objetos son un tipo de variable que contienen información (otras variables) en un enfoque clave: valor.

Así que, si queremos traducir (y optimizar) las variables de un vehículo en un `Object`, nosotros haremos:

```py
class ClassName:
      model = "Corolla"
      make = "Toyota"
      color = "Green"
      year = "2015"

```


Se ve como una función, ¿cierto? Pero no lo es.

Ahora estamos almacenando la información en una forma más organizada, y si nosotros queremos obtener esa información, hacemos:

```py

class Person:
    def __init__():
    self.name = "John"                   #String
    self.lastname = "Doe"
    self.age = 35                         #Number
    self.gender = "male"
    self.lucky_numbers = [ 7, 11, 13, 17] #Array
    self.significant_other = person2       #Object, sí el mismo variable/objeto definido después

class Person2:
    def __init__():
    self.name = "Jane"
    self.lastname = "Doe"
    self.age = 38
    self.gender = "female"
    self.lucky_numbers = [ 2, 4, 6, 8]


class Family:
    def __init__():
    self.lastname = "Doe"
    self.members = [person, person2]       //Array de objetos

```
Así que, en este escenario si nosotros queremos saber el nombre del primer miembro de la familia Doe, hacemos:

```py
print(family.members[0].name)
```

Algo fácil :)

## 📝 Instrucciones:
1. **1** Programando, cambia el cuarto lucky_number de John Doe a 33 (usa un comando, no cambies el código manualmente)
2. **2** Programando, crea una nueva persona y agrégala al objeto familia. Jimmy Doe, 13, male, lucky numbers: 1, 2, 3, 4; significant other: null. (usa un comando, no manualmente, cambia el código)
3. **3** Itera sobre los miembros de la familia para obtener todos los lucky_numbers.
3. **4** Ahora, por favor, imprime la SUMA de todos los  lucky_numbers de la familia Doe.


