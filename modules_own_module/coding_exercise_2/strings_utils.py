import string_utils

def halve_strings(string_list):
    strings_output = []
    for strings in string_list:
        strings_output += [string_utils.halve_string(strings)]

    return strings_output

if __name__ == '__main__':
    print(halve_strings(['test', '1234']))
