# `23` Python Objects

Often you'll find yourself wanting to save more information in less space, especially if it's all related. For example:

Let's say that we want to represent cars into variables:

```py
car_1_Model = "corolla"
car_1_Make = "Toyota"
car_1_Color = "green"
car_1_Year = 2015

car_2_Model = "santa fe"
car_2_Make = "Hyundai"
car_2_Color = "purple"
car_2_Year = 2013
#... (you get the idea)
```

There's an optimized approach to this, it is called Objects. Objects are a type of variable that contains information (other variables) in a key: value manner.

So if we want to translate (and optimize) the variables from the car into an Object, we do:

```py
class ClassName:
      model = "Corolla"
      make = "Toyota"
      color = "Green"
      year = "2015"

```


Looks like a function, right? But it's not.

Now we are storing information into a more organized way, and if we want to get that information we can do:

```py

class Person:
    def __init__():
    self.name = "John"                   #String
    self.lastname = "Doe"
    self.age = 35                         #Number
    self.gender = "male"
    self.lucky_numbers = [ 7, 11, 13, 17] #List
    self.significant_other = person2       #Object, yes the same variable/object defined after

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
    self.members = [person, person2]       #List of objects

```
So, if on this scenario if we want to know the name of the first member of the Doe family we do:

```py
print(family.members[0].name)
```


Easy stuff :)
## 📝 Instructions:
1. **1** Programmatically, change the fourth lucky number of John Doe to 33 (use a command, don't manually change the code)
2. **2** Programmatically, create a new person and add it to the family object. Jimmy Doe, 13, male, lucky numbers: 1, 2, 3, 4; significant other: null. (use a command, don't manually change the code)
3. **3** Loop through all the family members to get all the lucky numbers.
3. **4** Now please print ( console.log() ) the SUM of all of the lucky numbers of the Doe family.


