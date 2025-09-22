def count_occurences(file_name, word):
    try:
        stream = open(file_name)
        count = 0
        cleaned_strings = ' '.join(stream.readlines()).replace(
            '.', ' ').replace(',', ' ').split()
        for i in cleaned_strings:
            if i.lower() == word.lower():
                count += 1

        return count
    except Exception as e:
        print(f'An error occured: {e}')
    finally:
        stream.close()


if __name__ == '__main__':
    count1 = count_occurences('first_text_file.txt', 'bit')
    count2 = count_occurences('second_text_file.txt', 'the')

    print(
        f'The number of word \'bit\' in the first_text_file.txt is {count1}')
    print(
        f'The number of word \'the\' in the second_text_file.txt is {count2}')
