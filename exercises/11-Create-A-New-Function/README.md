---
tutorial: "https://www.youtube.com/watch?v=XazswkTqKJI"
---

# `11` Create a New Function

As you know, functions are a useful block of code that you can re-use as many times as you need. In the last exercise, you had a function that received two parameters (two inputs) and returned the sum of those. Like this:

```py
def add_numbers(a, b):
  print(a + b)
```

But Python comes with a bunch of "pre-defined" functions that you can use, for example:

```py
import random
# Generates a random number between
# a given positive range
r1 = random.randint(0, 10)
print("Random number between 0 and 10 is % s" % (r1))
```

You can use the `randint()` function to get a random decimal number. `Randint()` is an inbuilt function of the **random module** in Python3. 

The **random module** gives access to various useful functions and one of them being able to generate random numbers, which is `randint()`.

## 📝 Instructions:

1. Please now create a function called `generate_random` that prints and returns a random number between 0 and 9 every time it is called.

## 💡 Hints:

+ One possible solution involves using two predefined functions: the `randint()` or `randrange()` function.

+ Don't forget to import the **random module**.

+ You can check the documentation here: https://docs.python.org/3/library/random.html#functions-for-integers