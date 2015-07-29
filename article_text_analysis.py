#!/usr/bin/env python2
"""
Minimal Example
===============
Generating a square wordcloud from some shit
"""

from os import path
import matplotlib.pyplot as plt
from scipy.misc import imread
import random

from wordcloud import WordCloud, STOPWORDS


#def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    #return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = path.dirname(__file__)

# Read the DB mask in
mask = imread(path.join(d, "3DBox.png"))

# Read the whole text.
text = open(path.join(d, "article_texts.txt")).read()

# adding stopwords
stopwords = STOPWORDS.copy()
stopwords.add("P")
stopwords.add("p")
stopwords.add("b")
stopwords.add("br")
stopwords.add("quot")
stopwords.add("nbsp")
stopwords.add("em")
stopwords.add("strong")
stopwords.add("href")
stopwords.add("said")
stopwords.add("also")


# Open a plot of the generated image.

wc = WordCloud(max_words=100,000,000, stopwords=stopwords, margin=4,
               random_state=1).generate(text)
# store default colored image
#default_colors = wc.to_array()]


plt.title("Custom colors")
plt.axis("off")
plt.imshow(wc)
#plt.figure(figsize=(50,40))
wc.to_file("article_text_3.png")

#plt.figure()
#plt.title("Default colors")
#plt.imshow(default_colors)


plt.show()


