# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now') # tuple is immutable.
stuff = list(stuff) # convert to list using constructor
stuff[2] = 'goodbye' # change 'bye' to 'goodbye'
stuff = tuple(stuff) # converting back to tuple using constructor
print(stuff) # Checking
print(type(stuff)) # Checking class type