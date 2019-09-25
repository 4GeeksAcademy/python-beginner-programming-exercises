# `14` Your First Switch

Python does not have a simple switch case construct. Coming from a Javascript or C++ background, you may find this to be a bit odd.
So, to get around this, we use Python’s built-in dictionary construct to implement cases and decided what to do when a case is met.
We can also specify what to do when none is met.

One way out would be to implement an if-elif-else ladder. Rather, we can use a dictionary to map cases to their functionality. Here,
we define a function week() to tell us which day a certain day of the week is. A switcher is a dictionary that performs this mapping.

```py
def week(i):
        switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }
         return switcher.get(i,"Invalid day of week")

```

Now, we make calls to week() with different values.

```py
week(2)

```
## 📝 Instructions:

1. Complete this switch statement with 3 possible colors: Red, Green and Blue.

The function needs to return **true** if the color is available or **false** if the color is not available.

