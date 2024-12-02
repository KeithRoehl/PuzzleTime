# Infinite Loop from Hell

Welcome to the Infinite Loop from Hell! Your task is to hijack the alien loop and print `Game over`.

## Setup
Clone this repository and run `puzzle.py`. Warning: this will run an infinite loop if you don’t solve it!

## Goal
You can only inject **one line of code** into the program. The goal is to replace the `alien_loop` function with something that ends the madness.

## Rules
- Do not modify the `alien_loop` function beyond one line.
- You must solve it using Python's runtime flexibility.

## Example
Inject the following line to hijack the loop:
```python
alien_loop = lambda: print("Game over")
