from wordcloud import WordCloud
from matplotlib import pyplot as plt

text = 'apple orange banana grape cherry pineapple watermelon'

wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud)