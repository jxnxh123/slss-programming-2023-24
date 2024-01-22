

# format strings
if we want to evaluate inside of a string, we use f-strings.
To create an f-string, we put an f before the open quote
```python
fave_food = input ("whats your favourite food? ")

print (f"oooooo, {fave_food})
	   
```
# [[Design]]

# [[Lists]]

# [[Modules]]

# String Methods
[[Methods]] are something we can use on [[objects]]

String methods allow us to modify strings.

say for example we want to make all the characters of a sting lowercase.

```python
mr_ubial_yelling = "YOU SHOULD PUSH YOUR CHAIRS IN! "

print(mr_ubial_yelling.lower())
```


We can use string methods to help solve [[Errors#Semantic Errors|semantic errors]]. 

## `. lower`


The .lower method takes a string and converts all uppercase
characters to lowercase. 


## `. upper`


The .upper () method uppercases all letters.


## `.strip (chars)`

The .srtrip() method removes characters from both the beginning and 
the end of the string.


```python
user_feeling = input("how are you feeling today? ")
# "good!" "good." "Good." "good!!!!!!!!"
if user_feeling.lower().strip == "good":
	print("thats great!")
```


## `.spli(str)`

The `.split` method splits a string into a [[list]], separating the string
based on the characters you give it.

```python
grocery_str = "eggs milk cheese hotwheels"

grocery_list = grocery_str.splt(" ")
```