from wordcloud import WordCloud
import matplotlib.pyplot as plt
import codecs

file = codecs.open('word.txt','r', 'utf-8', 'ignore')
text = file.read()
wordcloud = WordCloud(font_path = r'C:\Users\taniguchi\OneDrive\Word_annkert\IPAfont00303\ipamp.ttf',
                      background_color="black",
                      width=1000,height=400).generate(text)
plt.figure(figsize=(15,12))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("./img/word_txt.png")