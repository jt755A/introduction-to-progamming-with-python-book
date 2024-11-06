# Use slicing to write Python code to print a 6-character
# substring of 'Launch School' that begins with the first c.

text = 'Launch School'

index = text.find('c')   # returns index number of first 'c'.
print(text[index:index + 6])