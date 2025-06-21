spam = ['apples', 'bananas', 'tofu', 'cats']

def list_to_str(items):
    if items == 0:
        return ''
    elif items == 1:
        return items[0]
    elif items == 2:
        return items[0] + ' and ' + items[1]
    else:
        return ', '.join(items[:-1]) + ' and ' + items[-1]
    
print("\n", list_to_str(spam))