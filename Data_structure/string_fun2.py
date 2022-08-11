from itertools import count
from operator import le

# from sympy import PoleError
from story import story_
# # print(story_)
# leng = len(story_)
# print(leng)
# a_ = story_.count('a')
# print(a_)

# # unstory = story_.replace(' of ', 'on')
# # print(unstory)

# my_vowel_story = story_.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
# print(my_vowel_story)

# only_vowel = ''
# for char in 'aeiouAEIOU':
#     only_vowel += char
    
# print(only_vowel)

# words = story_.split()
# print("Total number of words",len(words))
# print('Total unique words: {}'.format(set(words)))

# sentence = story_.split('.')
# print(len(sentence))

# lines = story_.split('\n')
# print(len(lines))

poem = [
    'twinkle, twincle, little star',  
    'How i wonder what you are!'
]
Poem_story = '\n'.join(poem)
print(Poem_story)