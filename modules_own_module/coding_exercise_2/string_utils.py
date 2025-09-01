from math import ceil

def halve_string(input_string):
    length = ceil(len(input_string)/2)
    tuple = (input_string[:length], input_string[length:])
    return tuple

if __name__ == '__main__':
    print(halve_string('tetst'))

