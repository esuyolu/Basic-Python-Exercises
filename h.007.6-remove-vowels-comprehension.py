# Write a list comprehension such that vowels are eliminated from the words in the text.
# For example: s = 'bugün hava çok güzel'
# text to be obtained: bgn hv çk gzl

vowels = 'aeıiuüoö'

s = 'bugün hava çok güzel'
result = ''

result = result.join([j for j in [i for i in s if i not in vowels]])

print('result: ', result)
