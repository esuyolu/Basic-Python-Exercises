# Write the set comprehension that gives the vowels in a text.
# For example, let the text be "bugün hava çok güzel".
# The set obtained here will contain the strings 'u', 'ü', 'a', 'o', 'e'.

text = input('enter a text: ')

vowels = 'aeıiuüoö'

vowels_in_text = {t for t in text if t in vowels}

print(vowels_in_text)
