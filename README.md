# NUMBER_GUESSING_GAME_USING_PYTHON

## Project Overview
This project is a Reverse Number Guessing Game developed using Python.  
In this program, the user thinks of a number between 1 and 100, and the computer tries to guess the number.

The computer does not guess randomly. Instead, it uses mathematical logic to find the number efficiently.  
After each guess, the user gives feedback by telling whether the guessed number is **low**, **high**, or **correct**.

Based on the user’s response, the computer adjusts its next guess until it finds the correct number.

---

## What This Program Does
- Asks the user whether to start the game or not
- Displays game rules using a tuple
- The user thinks of a number (not entered in the program)
- The computer makes a guess
- The user responds with:
  - `low` if the guess is smaller than the number
  - `high` if the guess is larger than the number
  - `correct` if the guess is right
- The computer continues guessing until the correct number is found
- Displays the total number of attempts and guesses at the end

---

## Concepts Used in This Project
- Looping statements (`while`)
- Conditional statements (`if`, `elif`, `else`)
- Mathematical expressions
- Python data structures:
  - List (to store all guesses)
  - Set (to store unique guesses)
  - Tuple (to store game rules)
  - Dictionary (to store final results)
- User input and output

---

## Purpose of the Project
The main purpose of this project is to understand:
- How logical thinking can be applied in problem solving
- How computers can make decisions based on user feedback
- How Python data structures work in real-time applications
