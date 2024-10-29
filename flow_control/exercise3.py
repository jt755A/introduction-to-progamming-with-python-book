def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113') # prints 'Product2' - matches case '113' condition
bar_code_scanner(142) # prints 'Product not found!' - 142 is int, not str