# `25` Javascript Objects

Often you'll find yourself wanting to save more information in less space, especially if it's all related. For example:

Let's say that we want to represent cars into variables:

```Javascript
var car1Model = "corolla";
var car1Make = "Toyota";
var car1Color = "green";
var car1Year = 2015;

var car2Model = "santa fe";
var car2Make = "Hyundai";
var car2Color = "purple";
var car2Year = 2013;
//... (you get the idea)
```

There's an optimized approach to this, it is called Objects. Objects are a type of variable that contains information (other variables) in a key: value manner.

So if we want to translate (and optimize) the variables from the car into an Object, we do:

```js
var car1 = { model: "corolla", make: "toyota", color: "green",  year: 2015};

```

You can see the key: value separated by a comma.

And for us (developers) to read it easier we write it like this:

```js
var car1 = {
    model: "corolla",
    make: "toyota",
    color: "green",
    year: 2015
};

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

```js
console.log(family.members[0].name);
```

Or the 3rd lucky number of the significant other of the second member of Doe's family:

```Javascript
console.log( family.members[1].significant_other.lucky_numbers[2]);
```

Easy stuff :)
## 📝 Instructions:
1. Programmatically, change the fourth lucky number of John Doe to 33 (use a command, don't manually change the code)
2. Programmatically, create a new person and add it to the family object. Jimmy Doe, 13, male, lucky numbers: 1, 2, 3, 4; significant other: null. (use a command, don't manually change the code)
3. Now please print ( console.log() ) the SUM of all of the lucky numbers of the Doe family.

## 💡 Hint:

- You can get each array of lucky numbers from each person object inside the family object.
- Once you get each array just loop over it adding every element (like we've been doing so far). And then add each sum of the 3 family members.
- Null is also an object.
