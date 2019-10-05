# `25` Python Objects

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
    def __init__():
        self.model = "Corolla"
        self.make = "Toyota"
        self.color = "Green"
        self.year = "2015"

```


Looks like a function, right? But it's not.

Now we are storing information into a more organized way, and if we want to get that information we can do:

```js

var person = {
    name: "John",                    //String
    lastname: "Doe",
    age: 35,                         //Number
    gender: "male",
    lucky_numbers: [ 7, 11, 13, 17], //Array
    significant_other: person2       //Object, yes the same variable/object defined after
};

var person2 = {
    name: "Jane",
    lastname: "Doe",
    age: 38,
    gender: "female",
    lucky_numbers: [ 2, 4, 6, 8],
    significant_other: person
};

var family = {
    lastname: "Doe",
    members: [person, person2]       //Array of objects
};
```
So, if on this scenario if we want to know the name of the first member of the Doe family we do:

```py
print(family.members[0].name);
```

Or the 3rd lucky number of the significant other of the second member of Doe's family:

```Javascript
console.log( family.members[1].significant_other.lucky_numbers[2]);
```

Easy stuff :)
## 📝 Instructions:
1. **1** Programmatically, change the fourth lucky number of John Doe to 33 (use a command, don't manually change the code)
2. **2** Programmatically, create a new person and add it to the family object. Jimmy Doe, 13, male, lucky numbers: 1, 2, 3, 4; significant other: null. (use a command, don't manually change the code)
3. **3** Loop through all the family members to get all the lucky numbers.
3. **4** Now please print ( console.log() ) the SUM of all of the lucky numbers of the Doe family.


