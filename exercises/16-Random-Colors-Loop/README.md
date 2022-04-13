---
tutorial: "https://www.youtube.com/watch?v=8zH3JT3AuAw"
---

# `16` Random Colors (Loop)

We have created a function that returns a color based on a number between 0 and 3 (for any different number, it will return the color `black`).

Let's say that we are teachers in a 10 student classroom and we want to randomly assign ONE color, between `red`, `yellow`, `blue` and `green`, to EACH student.

(only 1 color per student)

## 📝 Instructions:

1. Change the function `get_allStudentColors` so it returns a list of 10 colors, were each item in the list represents the color assigned to each student.

## 💡 Hints:

- You have 10 students, you need the loop to iterate 10 times and add these values to a list.

- In each iteration, generate a random number between 0 and 3 using the `randint()` function that we have seen in previous exercises.

- Use the `get_color` function, in this exercise to find out what color corresponds to the number obtained.

- Call (execute) the function `get_allStudentColors` and print its result in the console.