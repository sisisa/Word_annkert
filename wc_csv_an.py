from janome.tokenizer import Tokenizer
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import csv

def wordcloud_make(text):
#1---オブジェクト作成
    t = Tokenizer()
#2---メソッドに文字列を渡す
    token = t.tokenize(text)
    word_list = []
#3---品詞の指定
    for line in token:
        tmp = re.split('\t|,', str(line))
        if tmp[1] in ["名詞"]:
            if tmp[2] in ["一般", "固有名詞","代名詞"]:
                word_list.append(tmp[0])

    return " " . join(word_list)

#4---ファイル読み込み
text = open("an.csv", encoding="shift-jis").read()
#5---文字列取得
word_txt = wordcloud_make(text)
#6---wordcloudにテキストを代入
wordcloud = WordCloud(width=1200, height=800, background_color='black',font_path= r"C:\Users\taniguchi\OneDrive\Word_annkert\IPAfont00303\ipamp.ttf").generate(word_txt)
# wordcloud = WordCloud(background_color="black", ).generate(text)

#7---matplotlibで画像生成
plt.figure(figsize=(8, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("jap1.png")