#!/usr/bin/env python2
"""
Minimal Example
===============
Generating a square wordcloud from some Bitbucket commits
"""

from os import path
import matplotlib.pyplot as plt
from scipy.misc import imread
import random

from wordcloud import WordCloud, STOPWORDS


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = path.dirname(__file__)

# Read the DB mask in
mask = imread(path.join(d, "db_mask.jpeg"))

# Read the whole text.
text = open(path.join(d, "oh-dba_commits_format.txt")).read()

# adding stopwords
stopwords = STOPWORDS.copy()

# Open a plot of the generated image.
wc = WordCloud(max_words=1000, mask=mask,stopwords=stopwords, margin=5,
               random_state=1).generate(text)
# store default colored image
#default_colors = wc.to_array()]
plt.title("Custom colors")
plt.axis("off")
plt.imshow(wc)
wc.to_file("db_mask2.png")
#plt.figure()
#plt.title("Default colors")
#plt.imshow(default_colors)

plt.show()


