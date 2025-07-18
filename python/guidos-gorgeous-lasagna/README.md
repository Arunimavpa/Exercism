# Guido's Gorgeous Lasagna

Welcome to Guido's Gorgeous Lasagna on Exercism's Python Track.
If you need help running the tests or submitting your code, check out `HELP.md`.
If you get stuck on the exercise, check out `HINTS.md`, but try and solve it without using those first :)

## Introduction

Python is a [dynamic and strongly][dynamic typing in python] typed programming language.
It employs both [duck typing][duck typing] and [gradual typing][gradual typing] via [type hints][type hints].

While Python supports many different programming _styles_, internally **everything in Python is an [object][everythings an object]**.
This includes numbers, strings, lists, and even functions.

We'll dig more into what all of that means as we continue through the track.

This first exercise introduces 4 major Python language features:
1.  Name Assignment (_variables and constants_),
2.  Functions (_the `def` keyword and the `return` keyword_),
3.  Comments, and
4.  Docstrings.

<br>

~~~~exercism/note

In general, content, tests, and analyzer tooling for the Python track follow the style conventions outlined in [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [PEP 257](https://www.python.org/dev/peps/pep-0257/) for Python code style, with the additional (strong) suggestion that there be no single letter variable names.

On the Python track, [variables][variables] are always written in [`snake_case`][snake case], and constants in `SCREAMING_SNAKE_CASE`.

[variables]: https://realpython.com/python-variables/
[snake case]: https://en.wikipedia.org/wiki/Snake_case
~~~~

<br>

## Name Assignment (Variables & Constants)

Programmers can bind [_names_][facts-and-myths-about-python-names] (also called _variables_) to any type of object using the assignment `=` operator: `<name> = <value>`.
A name can be reassigned (or re-bound) to different values (different object types) over its lifetime.


```python
>>> my_first_variable = 1  #<-- my_first_variable bound to an integer object of value one.
>>> my_first_variable = 2  #<-- my_first_variable re-assigned to integer value 2.

>>> print(type(my_first_variable))
<class 'int'>

>>> print(my_first_variable)
2

>>> my_first_variable = "Now, I'm a string." #<-- You may re-bind a name to a different object type and value.
>>> print(type(my_first_variable))
<class 'str'>

>>> print(my_first_variable)
"Now, I'm a string."  #<-- Strings can be declared using single or double quote marks.
```


### Constants

Constants are names meant to be assigned only once in a program.
They should be defined at a [module][module] (file) level, and are typically visible to all functions and classes in the program.
Using `SCREAMING_SNAKE_CASE` signals that the name should not be re-assigned, or its value mutated.


## Functions

The `def` keyword begins a [function definition][function definition].
Each function can have zero or more formal [parameters][parameters] in `()` parenthesis, followed by a `:` colon.
Statements for the _body_ of the function begin on the line following `def` and must be _indented in a block_.


```python
# The body of a function is indented by 2 spaces, & prints the sum of the numbers.
def add_two_numbers(number_one, number_two):
  total = number_one + number_two
  print(total)  

>>> add_two_numbers(3, 4)
7


# Inconsistent indentation in your code blocks will raise an error.
>>> def add_three_numbers_misformatted(number_one, number_two, number_three):
...     result = number_one + number_two + number_three   # This was indented by 4 spaces.
...    print(result)     #this was only indented by 3 spaces
...
...
  File "<stdin>", line 3
    print(result)
    ^
IndentationError: unindent does not match any outer indentation level
```


Functions _explicitly_ return a value or object via the [`return`][return] keyword:


```python
# Function definition on first line, explicit return used on final line.
>>> def add_two_numbers(number_one, number_two):
        return number_one + number_two   


# Calling the function in the Python terminal returns the sum of the numbers.
>>> add_two_numbers(3, 4)
7

# Assigning the function call to a variable and printing it 
# will also return the value.
>>> sum_with_return = add_two_numbers(5, 6)
>>> print(sum_with_return)
11
```


Functions that do not have an _explicit_ `return` expression will _implicitly_ return the [`None`][none] object.
This means that if you do not use `return` in a function, Python will return the `None` object for you.
The details of `None` will be covered in a later exercise.
For the purposes of this exercise and explanation, `None` is a placeholder that represents nothing, or null:


```python
# This function does not have an explicit return.
def add_two_numbers(number_one, number_two):
  result = number_one + number_two


# Calling the function in the Python terminal appears 
# to not return anything at all.
>>> add_two_numbers(5, 7)
>>>


# Using print() with the function call shows that 
# the function is actually returning the **None** object.
>>> print(add_two_numbers(5, 7))
None


# Assigning the function call to a variable and printing 
# the variable will also show None.
>>> sum_without_return = add_two_numbers(5, 6)
>>> print(sum_without_return)
None
```


### Calling Functions

Functions are [_called_][calls] or invoked using their name followed by `()`.
Dot (`.`) notation is used for calling functions defined inside a class or module.

```python
>>> def number_to_the_power_of(number_one, number_two):
        return number_one ** number_two
...

>>> number_to_the_power_of(3,3) # Invoking the function with the arguments 3 and 3.
27


# A mismatch between the number of parameters and the number of arguments will raise an error.
>>> number_to_the_power_of(4,)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: number_to_the_power_of() missing 1 required positional argument: 'number_two'


# Calling methods or functions in classes and modules.
>>> start_text = "my silly sentence for examples."
>>> str.upper(start_text)  # Calling the upper() method for the built-in str class.
"MY SILLY SENTENCE FOR EXAMPLES."

# Importing the math module
import math

>>> math.pow(2,4)  # Calling the pow() function from the math module
>>> 16.0
```


## Comments

[Comments][comments] in Python start with a `#` that is not part of a string, and end at line termination.
Unlike many other programming languages, Python **does not support** multi-line comment marks.
Each line of a comment block must start with the `#` character.


## Docstrings

The first statement of a function body can optionally be a [_docstring_][docstring], which concisely summarizes the function or object's purpose.
Docstrings are declared using triple double quotes (""") indented at the same level as the code block:


```python

# An example from PEP257 of a multi-line docstring.
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """

    if imag == 0.0 and real == 0.0:
        return complex_zero

```


Docstrings are read by automated documentation tools and are returned by calling the special attribute `.__doc__` on the function, method, or class name.
Docstring conventions are laid out in [PEP257][pep257].

Docstrings can also function as [lightweight unit tests][doctests], which will be covered in a later exercise.


```python
# An example on a user-defined function.
>>> def number_to_the_power_of(number_one, number_two):
        """Raise a number to an arbitrary power.

        :param number_one: int the base number.
        :param number_two: int the power to raise the base number to.
        :return: int - number raised to power of second number

        Takes number_one and raises it to the power of number_two, returning the result.
        """

        return number_one ** number_two
...

# Calling the .__doc__ attribute of the function and printing the result.
>>> print(number_to_the_power_of.__doc__)
Raise a number to an arbitrary power.

    :param number_one: int the base number.
    :param number_two: int the power to raise the base number to.
    :return: int - number raised to power of second number

    Takes number_one and raises it to the power of number_two, returning the result.
```

[calls]: https://docs.python.org/3/reference/expressions.html#calls
[comments]: https://realpython.com/python-comments-guide/#python-commenting-basics
[docstring]: https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings
[doctests]: https://docs.python.org/3/library/doctest.html
[duck typing]: https://en.wikipedia.org/wiki/Duck_typing
[dynamic typing in python]: https://stackoverflow.com/questions/11328920/is-python-strongly-typed
[everythings an object]: https://docs.python.org/3/reference/datamodel.html
[facts-and-myths-about-python-names]: https://nedbatchelder.com/text/names.html
[function definition]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[gradual typing]: https://en.wikipedia.org/wiki/Gradual_typing
[module]: https://docs.python.org/3/tutorial/modules.html
[none]: https://docs.python.org/3/library/constants.html
[parameters]: https://docs.python.org/3/glossary.html#term-parameter
[pep257]: https://www.python.org/dev/peps/pep-0257/
[return]: https://docs.python.org/3/reference/simple_stmts.html#return
[type hints]: https://docs.python.org/3/library/typing.html

## Instructions

You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook.

You have five tasks, all related to cooking your recipe.

<br>

~~~~exercism/note
We have started the first function definition for you in the stub file, but you will need to write the remaining function definitions yourself.
You will also need to define any constants yourself.
Read the #TODO comment lines in the stub file carefully.
Once you are done with a task, remove the TODO comment.
~~~~

<br>

## 1. Define expected bake time in minutes as a constant

Define the `EXPECTED_BAKE_TIME` [constant][constants] that represents how many minutes the lasagna should bake in the oven.
According to your cookbook, the Lasagna should be in the oven for 40 minutes:

```python
>>> print(EXPECTED_BAKE_TIME)
40
```

## 2. Calculate remaining bake time in minutes

Complete the `bake_time_remaining()` function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the `EXPECTED_BAKE_TIME` constant.

```python
>>> bake_time_remaining(30)
10
```


## 3. Calculate preparation time in minutes

Define the `preparation_time_in_minutes()` [function][functions] that takes the `number_of_layers` you want to add to the lasagna as an argument and returns how many minutes you would spend making them.
Assume each layer takes 2 minutes to prepare.

```python
>>> def preparation_time_in_minutes(number_of_layers):
        ...
        ...
        
>>> preparation_time_in_minutes(2)
4
```


## 4. Calculate total elapsed time (prepping + baking) in minutes

Define the `elapsed_time_in_minutes()` function that takes two parameters as arguments:

- `number_of_layers` (_the number of layers added to the lasagna_)
- `elapsed_bake_time` (_the number of minutes the lasagna has spent baking in the oven already_).

This function should return the total minutes you have been in the kitchen cooking — your preparation time layering +
the time the lasagna has spent baking in the oven.


```python
>>> def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
        ...
        ...
        
>>> elapsed_time_in_minutes(3, 20)
26
```


## 5. Update the recipe with notes

Go back through the recipe, adding "notes" in the form of [function docstrings][function-docstrings].

```python
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
```

[constants]: https://stackoverflow.com/a/2682752
[functions]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[function-docstrings]: https://docs.python.org/3/tutorial/controlflow.html#documentation-strings

## Source

### Created by

- @BethanyG