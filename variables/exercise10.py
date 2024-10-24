obj = 'ABcd' #reassigns variable
obj.upper() #Neither: runs a upper method on obj. But does not reassign or mutate
obj = obj.lower() #mutates value of object # False: text strings are immutable. It reassigns to new string
print(len(obj)) # no change, just prints
obj = list(obj) # reassigns: Becomes a list of ['a', 'b', 'c', 'd']
obj.pop() # mutates: removes the last element of the list.
obj[2] = 'X' # mutates collection to ['a', 'b', 'X']
obj.sort() # mutates: sorts collection to ['X', 'a', 'b']
set(obj) # neither: creates a set from obj, but does not reassign. Do not capture return value.
obj = tuple(obj) #reassigns collection   initializes elements into a tupe: ('X', 'a', 'b')
print(obj) 
print(type(obj))