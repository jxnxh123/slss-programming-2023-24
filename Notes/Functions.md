A function is a block of code that can be re used over and over again.

we can input data to the function. We refer to the data parameters. 

We describe the parameters in the docstring. A docstring (is short for documentation string) tells a human what the purpose of the function is.

We use the term arguments to describe the actual data that we put into the function.

```python
def area_of_a_sqaure(sidelength: float):
	"""calculate and print the area of a square.
	results are in units squared.

	  params:

	sidelength - length of one side of the square
	"""

	are = sidelength ** 2

	print(f:the area of a square with the side lenght {sidelength} is:
	{area} quare units."")

are_of_a_square(12.2)


```

## functions with Return Values

if a function has a return keyword in the body, we can call it a fruitful function.

```python
def adder(x: int, y: int) -> int:
	"""Returns the sum of the given numbers"""
	sum = x + y

	return sum

12 # 12
```

the return keyword does two things in a function.

1. Stops the functions
2. if theres a value after the return keyword, it sends the value back to the function call.

```python
def search(l: list, item: Any) -> int:
	"""searches through a list and returns the index.

	

```

## recursion

recursion is an elegant way to repeat a pattern.

Fractals are examples of patterns that can be described recursively. 

A recursive function must have three parts:

1. A function
2. A call to itself inside of the body code block.
3. A base case. The base case is where the function stops calling itself.

# Fibonacci Sequence and recursion

```python
fibonacci sequence
1, ,1, 2, 5, 8, 13, 21, 34, 55, ...
	x

fib(1) = 1
fib(2) = 1
	   
fib(3) = fib(2) + fib(2)
	   = 

	   =

```

# 2 dimensional list

so far, all the lists we've used in the class are one - dimensional.

we can create two- dimensional lists, which are lists inside a list.

```python
some_2d_list = [
				
]
```