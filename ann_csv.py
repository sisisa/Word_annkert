import csv
import collections
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud

list = []
with open('an.csv', 'r',encoding="utf-8") as f:

    '''
    UnicodeDecodeError:2023年7月24日解決(参考情報=https://qiita.com/Yuu94/items/9ffdfcb2c26d6b33792e)
    '''
    # カラムの値を抽出
    for row in csv.reader(f):
        list.append(row[1])

    # 先頭文字を削除
    del list[0]

    # 文字列をつなげる
    b = ""
    for a in reversed(list):
        b += a

    # 文字の整形（改行削除）
    text = "".join(b.splitlines())

    # 単語ごとに抽出
    docs=[]
    t = Tokenizer()
    tokens = t.tokenize(text)
    for token in tokens:
        if len(token.base_form) > 2:
            docs.append(token.surface)

    ## wordcloud の実行
    ## 日本語フォントを指定
    c_word = ' '.join(docs)
    wordcloud = WordCloud(background_color='white',font_path="C:\\Users\\taniguchi\\OneDrive\\Word_annkert\\IPAfont00303\\ipamp.ttf",width=800, height=400).generate(c_word)

    ## 結果を画像に保存
    wordcloud.to_file('./suda/an.png')

    # 単語を多い順に並べる
    c = collections.Counter(docs)
    print(c)

