# Week 1 Summary: Introduction to Python Programming

## 1. Variables and Data Types
Variables act as containers for storing data values. Python is dynamically typed, meaning you don't need to explicitly declare the data type.
* `int`: Whole numbers (e.g., `age = 25`)
* `float`: Decimal numbers (e.g., `temperature = 36.6`)
* `str`: Text/Strings wrapped in quotes (e.g., `name = "Alice"`)
* `bool`: Logical values (`True` or `False`)

## 2. Operators
Operators are symbols used to perform operations on variables and values.
* **Arithmetic:** `+` (Addition), `-` (Subtraction), `*` (Multiplication), `/` (Division), `//` (Floor Division), `%` (Modulus), `**` (Exponentiation)
* **Comparison:** `==` (Equal), `!=` (Not equal), `>`, `<`, `>=`, `<=`
* **Logical:** `and` (Returns True if both statements are true), `or` (Returns True if one statement is true), `not` (Reverses the result)

## 3. Input and Output
* `input()`: Captures user input as a string. It must be explicitly cast (e.g., `int()` or `float()`) if numerical operations are needed.
* `print()`: Displays output to the console. f-strings (`f"Text {variable}"`) are used for clean string formatting.

## 4. Conditional Statements
Used to make decisions and execute specific blocks of code based on conditions.
* `if`: Executes code if the condition is True.
* `elif`: Short for "else if", checks another condition if the previous ones were False.
* `else`: Executes if none of the above conditions are met.

## 5. Loops
Used to repeat a block of code multiple times.
* `for` loop: Iterates over a sequence (like a list, range, or string). Ideal when the number of iterations is known.
* `while` loop: Repeats as long as a specified condition remains `True`. Ideal when the stopping condition depends on dynamic changes.