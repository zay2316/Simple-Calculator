Simple Python Calculator

A simple desktop calculator application built with Python and Tkinter. The application provides a graphical user interface (GUI) that allows users to perform basic arithmetic operations with input validation and error handling.

Features

* Addition (+)
* Subtraction (-)
* Multiplication (*)
* Division (/)
* Input validation for numeric values
* Division-by-zero protection
* Error messages for invalid input
* Clear button to reset the calculator
* End button to close the application
* Simple graphical user interface using Tkinter

Technologies Used

* Python 3
* Tkinter — Python’s standard GUI library

How It Works

The calculator accepts two numbers from the user and an arithmetic operator.

1. Enter the first number.
2. Select an operator (+, -, *, /).
3. Enter the second number.
4. Click Calculate.
5. The result is displayed below the buttons.

The application validates both numeric inputs before performing the calculation and prevents division by zero.

Input Validation

The calculator uses a validation function to determine whether the user’s input can be converted into a floating-point number.

Invalid input produces an error message instead of allowing the application to crash.

The application also checks for division by zero before performing a division operation.

Installation

1. Clone the repository

git clone <your-repository-url>

2. Navigate to the project directory

cd SimpleCalculator

3. Run the application

python calculator.py

On some systems, you may need to use:

python3 calculator.py

Example

Enter first number: 10
Operator: *
Enter second number: 5
Result: 10.0 * 5.0 = 50.0

Purpose

This project was created as a beginner Python GUI application to demonstrate:

* Python functions
* Conditional statements
* Exception handling
* User input validation
* GUI development with Tkinter
* Event-driven programming
* Basic arithmetic operations

Future Improvements

Possible improvements include:

* Adding keyboard input support
* Adding more mathematical operations
* Improving the GUI design
* Adding a calculation history
* Adding a scientific calculator mode
* Adding keyboard shortcuts
* Improving number formatting

License

This project is available for educational and personal use.
