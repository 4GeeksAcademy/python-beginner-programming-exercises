<!-- hide -->
<div align="center">

# Learn Python Interactively (beginner)

![Course cover art reading "Learn Python Beginner interactive" next to the blue and yellow Python logo](https://raw.githubusercontent.com/4GeeksAcademy/python-beginner-programming-exercises/HEAD/.learn/assets/preview.png)

[![Interactive tutorial](https://img.shields.io/badge/4Geeks_Academy-Interactive_tutorial-2563eb?style=flat-square)](https://4geeks.com/en/interactive-exercise/python-beginner-programming-exercises)
[![Auto-graded with LearnPack](https://img.shields.io/badge/LearnPack-21_auto--graded_exercises-2563eb?style=flat-square)](https://learnpack.co)
[![Open in GitHub Codespaces](https://img.shields.io/badge/Open_in-GitHub_Codespaces-fb5a1f?style=flat-square&logo=github&logoColor=white)](https://codespaces.new/?repo=4GeeksAcademy/python-beginner-programming-exercises)

</div>
<!-- endhide -->

Learn Python Interactively is a beginner course of 21 auto-graded coding challenges that run inside your code editor. You start by printing `Hello World!` and finish by writing FizzBuzz, a Russian-roulette function and the full 99-bottles-of-milk song. It takes roughly 10 hours, requires no prior programming experience, and 19 of the exercises include a step-by-step video walkthrough.

<!-- hide -->
## 📋 About this tutorial

- **Difficulty**: easy (`difficulty: "easy"` in `learn.json`)
- **Duration**: about 10 hours
- **Exercises**: 22 folders — 1 welcome page plus 21 coding challenges
- **Technologies**: Python 3, variables, strings, conditionals, functions, loops
- **Grading**: automatic, 21 `test.py` files executed with pytest
- **Videos**: 19 exercise walkthroughs plus 1 intro video
- **Languages**: [English](https://github.com/4GeeksAcademy/python-beginner-programming-exercises/blob/HEAD/README.md) · [Español](https://github.com/4GeeksAcademy/python-beginner-programming-exercises/blob/HEAD/README.es.md)
<!-- endhide -->

## 🎯 What will you learn?

The 21 challenges introduce one idea at a time, and every idea is used again in a later exercise:

- **The console**: `print()` as the way a program talks back to you, and as your main debugging tool.
- **Variables**: declaring them, assigning strings and numbers, and printing several of them in a single `print()` call separated by commas.
- **Arithmetic**: multiplication with `*` and storing a result in a variable.
- **User input**: reading a value with `input()` and working with a variable whose value you don't know in advance.
- **String concatenation**: joining strings with the `+` operator, up to building a full HTML document out of 8 separate variables.
- **Conditionals**: `if...else` chains, relational operators (`>`, `<`, `==`, `!=`, `>=`, `<=`) and multi-branch price brackets.
- **The `random` module**: `randint(min, max)` and `randrange(start, stop)`, and the difference between an inclusive and an exclusive upper bound.
- **Functions**: calling a function someone else wrote, defining your own, passing parameters, and the difference between `return` and `print`.
- **Loops**: `for` with `range()`, repeating an action hundreds of times, and combining loops with conditionals.
- **Lists**: building a list item by item inside a loop.

## 👀 What will you build?

Each exercise is a real, runnable Python program. These are the 21 graded challenges, in order:

- **`01` Console** — print `Hello World!` on the terminal.
- **`02` Declare Variables** — declare a variable with the value `"Yellow"` and print it.
- **`03` Print more Variables** — declare `color = "red"` and `item = "marker"` and print both in one call.
- **`04` Multiply Two Values** — store `2345 * 7323` in a variable and print the result.
- **`05` User Inputed Values** — ask the user for their age and print it plus 10 years.
- **`06` String Concatenation** — set two variables so that `my_var1 + my_var2` prints `Hello World`.
- **`07` Create a Basic HTML** — concatenate 8 given variables into `<html><head><title></title></head><body></body></html>`.
- **`08.1` Your First If** — answer differently depending on whether the user has more than $100, more than $50, or $50 or less.
- **`08.2` How Much The Wedding Costs** — price a wedding catering job across four guest brackets, from $4,000 for up to 50 guests to $20,000 for more than 200.
- **`09` Random Numbers** — return a random whole number between 1 and 10 instead of a decimal.
- **`10` Calling Your First Function** — call the given `is_odd` function with `45345` and print what it returns.
- **`10.1` Creating Your First Function** — fill in the body of `add_numbers(a, b)` so the program prints `7`.
- **`11` Create A New Function** — write `generate_random()`, returning a random number between 0 and 9.
- **`12` Rand From One to Twelve** — use `randrange()` to produce integers from 1 to 12 inclusive.
- **`13` Your First Loop** — take a loop that counts to 9 and make it count to 11.
- **`14` Create A For Loop** — print "I will ask questions if I am stuck" exactly 300 times.
- **`15` Looping With FizzBuzz** — the classic interview exercise, printing 1 to 100 with `Fizz`, `Buzz` and `FizzBuzz`.
- **`16` Random Colors (Loop)** — assign one random color out of four to each of 10 students and return the resulting list.
- **`17` Russian Roulette** — complete `fire_gun` so it compares the bullet slot against the chamber position of a 6-slot revolver.
- **`18` The Beatles** — write `sing()` so it prints the closing chorus of "Let It Be" line by line.
- **`19` Bottles Of Milk** — write `number_of_bottles()`, printing all 100 verses of the 99-bottles song, singular included.

Exercise `00` is a welcome page with no code: it lists the concepts ahead and links to introductory reading.

## 🎓 What do you need before starting?

- **Prior programming experience**: none. The first challenge is a single `print()` call, and the tutorial explains what a console is before asking you to use one.
- **Python knowledge**: none. Every function used (`print`, `input`, `int`, `str`, `range`, `randint`, `randrange`) is introduced in the exercise that needs it.
- **Software, cloud option**: a GitHub account is enough. Codespaces builds the environment from the repository's `.devcontainer`, which installs Python 3.10, Node 22, LearnPack and pytest for you.
- **Software, local option**: Python 3 and Node.js 14 or newer, plus `pytest`, `pytest-testdox` and `mock`.
- **Time**: about 10 hours in total, so roughly 30 minutes per challenge if you watch the videos.
- **Language**: every exercise ships with `README.md` in English and `README.es.md` in Spanish.

## ✅ How does the automatic grading work?

Grading is real, not decorative: 21 of the 22 exercise folders contain a `test.py` file, and they run with pytest.

- **You write your answer in `app.py`**, the only file you are meant to edit. Comment markers such as `# ✅↓ Write your code here ↓✅` and `# ❌ ↓ DON'T CHANGE THE CODE BELOW ↓ ❌` show you the editable region.
- **You press Run** to execute the program and see its output, and the feedback button to run the tests.
- **Each test has a human-readable label** written with `@pytest.mark.it(...)`, so a failure reads like "The function `fizz_buzz` should exist" or "Your function needs to print the correct output" instead of a raw traceback.
- **Two kinds of checks are used**: output checks that capture what your program prints and compare it to the expected text, and source checks that use regular expressions to confirm you actually used the technique being taught, for example that a `for` keyword appears in your FizzBuzz solution.
- **A `solution.hide.py` file sits next to every graded exercise**, so a worked answer is always available once you have tried it yourself.

![Screenshot of the LearnPack instructions panel inside VS Code showing exercise 01 Console, with a red arrow pointing at the Run button next to the Get feedback and Reset buttons](https://raw.githubusercontent.com/4GeeksAcademy/python-beginner-programming-exercises/HEAD/.learn/assets/run-exercise.png)

## 💡 What mistakes should you avoid?

Most failed tests in this tutorial come from the same handful of causes:

- **Producing the right output the wrong way.** Exercise `12` accepts only `random.randrange(1, 13)`; `randint(1, 12)` prints identical numbers and still fails. Exercise `15` requires a `for` keyword in your file, so a `while` loop that prints perfect FizzBuzz output is rejected.
- **Confusing `return` with `print`.** Exercise `19` says explicitly to print the lyrics, while exercise `17` expects `fire_gun` to return the strings `You are dead!` and `Keep playing!`. Swapping the two breaks the test even though the behaviour looks right on screen.
- **Getting the exact text wrong.** Comparisons include capitalisation, punctuation and spacing: `"Yellow"` is not `"yellow"`, and the milk song's last verse changes to "no more bottles" and "Go to the store and buy some more".
- **Forgetting the singular case.** The 99-bottles exercise flips from "bottles" to "bottle" at 1, which is the single most common reason its last test fails.
- **Off-by-one ranges.** `randint(a, b)` includes both ends, `randrange(a, b)` excludes the last one, and the loop in exercise `13` has to reach 11, not stop at 10.
- **Not calling your own function.** Several tests check that the function is both defined and invoked, for example that `print(get_randomInt())` actually appears in `app.py`.

## ❓ Frequently asked questions

### How long does it take to learn Python basics with these exercises?

The package is estimated at 10 hours across 21 challenges. Most of them are a few lines of code; the ones that take longest are FizzBuzz, the random-colors list and the 99-bottles song, because their expected output is compared character by character.

### Do I need to know how to program before starting?

No. The tutorial is marked as `easy` difficulty and begins with printing a single line of text. Concepts arrive in order — console, variables, input, conditionals, randomness, functions, loops, lists — and each one is used again in a later exercise.

### Do I have to install Python on my computer?

Not if you use Codespaces: the `.devcontainer` in this repository provisions Python 3.10, Node 22, LearnPack and pytest automatically, and the exercises open in the browser. Installing locally is supported too and needs Python 3, Node.js 14 or newer, and the `pytest`, `pytest-testdox` and `mock` packages.

### My code works but the test still fails. Is that normal?

Yes, and it is worth knowing why. Some tests inspect your source code with regular expressions to check you used the specific construct being taught, so a correct answer written a different way can be rejected. The original authors describe the grading as rigid and suggest treating it as a suggestion rather than a verdict. When in doubt, compare your file with the `solution.hide.py` next to the exercise.

### Is it free, and can I reuse the code?

Access costs nothing and the code you write is yours. The content itself is not open source: the [LICENSE](https://github.com/4GeeksAcademy/python-beginner-programming-exercises/blob/HEAD/LICENSE.md) reserves all intellectual property rights and forbids republishing, selling, reproducing or redistributing the material. You can use it for personal learning and study, which is what 4Geeks Academy publishes it for.

### What should I do after finishing?

Move on to the packages this tutorial itself points you to: a dedicated set of [lists and loops exercises](https://4geeks.com/en/interactive-exercise/python-lists-loops-programming-exercises) and more than 20 [functions exercises](https://4geeks.com/en/interactive-exercise/python-functions-programming-exercises) that grow in difficulty. Exercises `10.1`, `13` and `15` link to them directly.

<!-- hide -->
## 📚 Related tutorials

- [Python lists and loops exercises](https://4geeks.com/en/interactive-exercise/python-lists-loops-programming-exercises) — the natural next step after exercise `13`.
- [Python functions exercises](https://4geeks.com/en/interactive-exercise/python-functions-programming-exercises) — 20+ challenges, referenced from exercises `10` and `10.1`.
- [Intro video for this course](https://www.youtube.com/watch?v=amyDNhZwGJQ) — the walkthrough linked from `learn.json`.

## 🚀 How to start

One-click installation, recommended:

[Open in GitHub Codespaces](https://codespaces.new/?repo=4GeeksAcademy/python-beginner-programming-exercises)

Once VS Code opens, the LearnPack exercises should start on their own. If they don't, type this in the terminal:

```bash
$ learnpack start
```

> 💡 You can also follow the same tutorial on the web at [4geeks.com](https://4geeks.com/en/interactive-exercise/python-beginner-programming-exercises).

## 💻 Local installation

1. Install [LearnPack](https://learnpack.co), Node.js 14+ and Python 3+:

   ```bash
   $ npm i @learnpack/learnpack -g && learnpack plugins:install @learnpack/python
   ```

2. Clone the repository and enter the folder:

   ```bash
   $ git clone https://github.com/4GeeksAcademy/python-beginner-programming-exercises.git
   $ cd python-beginner-programming-exercises
   ```

3. Install the testing dependencies and start, from the same level as `learn.json`:

   ```bash
   $ pip3 install pytest==6.2.5 pytest-testdox mock
   $ learnpack start
   ```

## 📚 How the exercises are organized

Every exercise lives in its own folder inside [`exercises/`](https://github.com/4GeeksAcademy/python-beginner-programming-exercises/tree/HEAD/exercises). The 21 graded ones contain:

- **`app.py`** — the entry file you edit and run.
- **`README.md`** — the instructions in English.
- **`README.es.md`** — the instructions in Spanish.
- **`test.py`** — the grading script; you don't need to open it.
- **`solution.hide.py`** — a worked solution, hidden by LearnPack until you ask for it.

## 🤝 Contributors

Thanks to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

1. [Alejandro Sánchez (alesanchezr)](https://github.com/alesanchezr) — (coder) 💻, (idea) 🤔, (build-tests) ⚠️, (pull-request-review) 👀, (build-tutorial) ✅, (documentation) 📖
2. [Paolo Lucano (plucodev)](https://github.com/plucodev) — (bug reports) 🐛, (coder) 💻, (translation) 🌎
3. [Marco Gómez (marcogonzalo)](https://github.com/marcogonzalo) — (translation) 🌎

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind are welcome — see the [full contributor list](https://github.com/4GeeksAcademy/python-beginner-programming-exercises/graphs/contributors).

This and many other exercises are built by students as part of the [4Geeks Academy Coding Bootcamp](https://4geeks.com/en/coding-bootcamp). Find out more about the [Full Stack Developer program](https://4geeks.com/en/career-programs/full-stack) and the [Data Science and Machine Learning program](https://4geeks.com/en/career-programs/data-science-ml).
<!-- endhide -->
