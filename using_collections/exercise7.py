# Write Python code to replace all the : characters
# in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info = info.split(':')

print('+'.join(info))

# method 2

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info = info.replace(':', '+')
print(info)