from wordcloud import WordCloud

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

word = open('output.txt', 'r',encoding='utf-8').read()

out = WordCloud(
    background_color='white',
    max_words=2000
)

out.generate(word)

mask = np.array(Image.open('alice_mask.png'))    

out = WordCloud(background_color='white', max_words=2000, mask=mask)

# generate the word cloud
out.generate(word)

# display the word cloud
fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height

plt.imshow(out, interpolation='bilinear')
plt.axis('off')
plt.show()