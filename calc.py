from abstra.forms import *

calc = Page().read_number("Enter a number:") \
            .read_number("Enter another number:") \
            .read_multiple_choice("Pick an operation:",
            ["Add", "Subtract", "Multiply","Divide"]) \
            .run(None)
x, y, operation = [x for x in calc.values()]

if operation == "add":
  display(f"{x} + {y} = {x+y}",button_text = "Right on")

if operation == "subtract":
  display(f"{x} - {y} = {x-y}", button_text = "That's it")

if operation == "multiply":
  display(f"{x} * {y} = {x*y}", button_text = "Great work")

if operation == "divide":
  display(f"{x} / {y} = {x/y}", button_text = "Oh yeah")