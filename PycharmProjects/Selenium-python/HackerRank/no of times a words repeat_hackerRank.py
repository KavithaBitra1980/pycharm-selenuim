#!/usr/bin/env python


__author__ = 'Kavitha Bitra'
__copyright__ = 'Copyright 2018.'
__version__ = '0.0.1'

# no of times a word repeats ina string

s = 'kavitha is a good girl, kavitha loves food and is good at food preparation'

words = s.split()
print(words)
print('no of words are',len(words))
for i in words:
    word_count = words.count(i)
    if word_count >= 2:
       print(i,word_count)





