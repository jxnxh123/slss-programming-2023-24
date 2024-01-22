---
tags: []
---


# Syntax Errors

These types of errors are when you run your code and something breaks.

syntax errors are relatively easy to fix.

Syntax errors happen when we don't follow the rules completely.

some examples are when we forget a closing ". or if we're missing a closing parenthesis.

# Semantic Errors

Semantic errors are much more challenging to squash.

Semantic errors are what your code doesn't "mean" what you 
actually mean. 



```python
user_response = input ("do you like to eat food? ")

if user_response == "yes":
	print("You passed the human test.")
else:
	print("you must be some sort of robot.")
```

The problem with the above code is subtle. What Mr. Ubial means 
is that if the user answers with anything AFFIRMATIVE the code should 
go back into the "yes" block. 

One way to solve this problem is to use [[#string methods]]. We can use .lower() to catch all permutations of capital letters.

```python
user_response = input ("do you like to eat food? ")

if user_response == "yes":
	print("You passed the human test.")
else:
	print("you must be some sort of robot.")



