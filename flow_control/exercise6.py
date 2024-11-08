# Write a function that takes a string as an argument and returns an
# all-caps version of the string when the string is longer
# than 10 characters. Otherwise, it should return the original string.
#  Example: change 'hello world' to 'HELLO WORLD',
# but don't change 'goodbye'.

def conditional_caps(text):
    if len(text) > 10:
        return text.upper()
    else:
        return text
    
# print(conditional_caps('hello world'))    