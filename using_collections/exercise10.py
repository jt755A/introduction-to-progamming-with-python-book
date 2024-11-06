# Consider the following nested collection:
# Write one line of code to print the activities that Cocoa enjoys.

cats = {
    'Pete': {                        # 1sdt object of 1st
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {                    # 2nd object of 2nd 
            'color': 'black',
            'enjoys': {               # 2nd object of nested
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

#print(cats[0][1][1]) # indexs

print(cats['Pete']['Cocoa']['enjoys'])