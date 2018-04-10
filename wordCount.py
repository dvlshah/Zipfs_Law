"""""""""""""""""""""""""""""""""""""""""""""

**** WORD COUNTING PROGRAM IN TXT FILE****

Author - Deval Shah
Date - 15/04/2017
Language - Python 3.5.2

"""""""""""""""""""""""""""""""""""""""""""""

#Reading text file
filename = 'A Cruising Voyage Round The World'
file = open(r"C:\Users\Deval\Documents\Zipf'sLaw\Images\A Cruising Voyage Round The World.txt", "r", encoding="utf-8-sig")

from collections import Counter
import operator
import numpy as np
import pandas as pd

#Storing each and every word of file in list
file_list = file.read().split()

#Counter objects creates dictionary of (unique word,frequency) tuples
wordcount = Counter([file_list[word].lower() for word in range(len(file_list))])

#Sort the dictionary tuples and store in list
sorted_x = list(zip(*sorted(wordcount.items(), key=operator.itemgetter(1),reverse=True)))

#Choosing first 100 words with highest frequency
x = list(sorted_x[0][0:20])
y = np.array(sorted_x[1][0:20])

df = pd.DataFrame()
df['words'] = x
df['frequency'] = y

results = [float("{0:.3f}".format(y[i]/y[0])) for i in range(int(y.shape[0]))]

import matplotlib.pyplot as plt
ax = df.plot(kind='bar',title=filename)
ax.set_xticklabels(df['words'], rotation=90)

#ax2 = df.plot(ax=ax)
#ax2.set_xticklabels(df['words'], rotation=90,)
plt.show()
