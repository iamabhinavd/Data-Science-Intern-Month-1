# Week 2 Summary: Data Structures and Functions

## 1. Built-in Data Structures
Python provides four primary built-in data structures to store collections of data:
* **Lists (`[]`):** Ordered, mutable (changeable), and allow duplicate elements. Used for collections of items where order matters.
* **Tuples (`()`):** Ordered, immutable (cannot be changed after creation), and allow duplicates. Excellent for data that shouldn't be modified (e.g., coordinates, configurations).
* **Dictionaries (`{key: value}`):** Unordered (or insertion-ordered in modern Python), mutable collections of key-value pairs. Keys must be unique and immutable.
* **Sets (`{}`):** Unordered, mutable collections of unique elements. Used to eliminate duplicates and perform mathematical operations like union or intersection.

## 2. Functions & Advanced Paradigms
Functions help modularize code, making it reusable and scannable.
* **Def Functions:** Standard functions defined using the `def` keyword with optional parameters and a explicit `return` statement.
* **Lambda Functions:** Anonymous, single-line functions defined using the `lambda` keyword. They are ideal for quick, throwaway calculations or passing as arguments (e.g., inside `map()` or `filter()`).
* **Recursion:** A programming pattern where a function calls itself to solve smaller instances of the same problem. Requires a *base case* to prevent infinite loops.

## 3. List Comprehension
An elegant, concise syntax to create new lists based on existing lists or iterables. It replaces verbose `for` loops.
* **Syntax:** `[expression for item in iterable if condition]`