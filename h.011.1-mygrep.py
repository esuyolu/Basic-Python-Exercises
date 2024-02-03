# Write a function called mygrep that prints lines containing certain words in a file as follows:
# <line number>: characters in the line

def mygrep(path, text):
    i = 0
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            i += 1
            if text in line:
                print(f'<{i}>:' + line, end='')


mygrep('test.txt', 'gül')
