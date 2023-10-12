# Almost a Circle - Python OOP

Here is another project I did as part of my ALX-SE training. It solidifies my understanding of classes in Python. It covers concepts like Object Oriented Programming, Inheritance, JSON, etcetera.

## Project Overview

This Python Object-Oriented Programming (OOP) project is designed to strengthen your understanding of OOP concepts by creating classes and objects to model shapes and implementing unit testing. The primary goal of the project is to develop two main classes: `Rectangle` and `Square`, which enable the creation of instances of rectangles and squares with specific attributes. The project also involves writing unit tests to validate the behavior of these classes and methods.

## Project Files

The project consists of several Python files:

1. **base.py**:

   - The `Base` class serves as the base class for both `Rectangle` and `Square`.
   - It contains class attributes and methods that are common to all shapes, such as `from_json_string` (to create instances from JSON strings) and `to_json_string` (to convert instances to JSON strings).
   - The class method `create(cls, **dictionary)` allows the creation of an instance with attributes from a dictionary.
   - The `__init__` method initializes instances of `Base`.

2. **rectangle.py**:

   - The `Rectangle` class inherits from the `Base` class.
   - It contains methods and attributes specific to rectangles, including `width`, `height`, `x`, and `y`.
   - Methods include `area()` (to calculate the area of the rectangle), `display()` (to show the rectangle on the console), and `__str__` (to create a string representation of the rectangle).
   - The `update` method is used to set attributes with non-keyworded arguments.
   - The `to_dictionary` method returns a dictionary representation of a `Rectangle` instance.
   - The class is thoroughly unit-tested.

3. **square.py**:

   - The `Square` class inherits from the `Rectangle` class.
   - It shares attributes and methods with `Rectangle` but includes a single attribute, `size`, which represents the side length of a square.
   - Additional methods specific to squares include `update`, `to_dictionary`, and a custom getter and setter for the `size` attribute.
   - The class is also extensively unit-tested.

4. **tests** (directory):

   - This directory contains unit tests for the project.
   - Tests are organized into different files, such as `test_rectangle.py` and `test_square.py`.
   - They cover various aspects of the `Rectangle` and `Square` classes, including attribute validation, method behavior, and JSON serialization.

5. **README.md**:

   - This README file provides an overview of the project, instructions for running the tests, and other essential information for users and collaborators.

6. **Main Python Files**:
   - Several main Python files (e.g., `0-main.py`, `1-main.py`, etc.) are used for testing the classes and methods.
   - They create instances of `Rectangle` and `Square`, call methods, and print the results.

In summary, this project focuses on creating classes for modeling geometric shapes (rectangles and squares) using Python OOP principles. The project also emphasizes comprehensive unit testing to ensure the correctness of the classes and their methods.

## Author

- Aishah Ayomide Mabayoje (maishah2540@gmail.com)

Please feel free to reach out if you have any questions.
