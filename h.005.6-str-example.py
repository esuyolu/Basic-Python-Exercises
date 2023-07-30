# Read a text from the keyboard. Let the text consist of words separated by space characters.
# Put the words in a list by discarding the same words.
# For example, the text entered is:
# bugün hava evet bugün çok hava güzel güzel
# The result should be a list like this:
# ['bugün', 'hava', 'evet', 'çok', 'güzel']

s = input('Enter a text: ')
s = s.split()[::]
result = []

for i in s:
    if i not in result:
        result.append(i)


print(result)

