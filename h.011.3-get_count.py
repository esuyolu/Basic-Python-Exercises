# Write the function called get_count,
# which returns the values of how many lines,
# how many words and how many characters are in a file as a triple tuple:

def get_count(path):
    with open(path, 'r') as f:
        size_of_lines = 0
        size_of_words = 0
        size_of_characters = 0

        for line in f:
            size_of_lines += 1
            for word in line.split(' '):
                size_of_words += 1
                size_of_characters += len(word)

        print(f'size_of_lines: {size_of_lines}')
        print(f'size_of_words: {size_of_words}')
        print(f'size_of_characters: {size_of_characters}')


get_count('test.txt')
