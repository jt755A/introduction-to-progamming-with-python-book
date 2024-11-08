# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)


# There is no code advancing the value of counter, which would
# allow the code to finish.
# EDIT i.e. counter < 5 always remains truthy