# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8 - index numbers refer to positions within the slice
print(text.rfind('f', 21, 35))    # 29 - index numbers are for whole string betweeen the start: stop indices