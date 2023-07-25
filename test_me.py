# ライブラリのインポート
import MeCab

# 分かち書き用のパーサーの設定
tagger = MeCab.Tagger("-Owakati") 

test_string = '「すもも」もももももものうち'
print(tagger.parse(test_string))

test_string1 = 'すももの木が裏庭にあり、ももの木は玄関先にある。'
print(tagger.parse(test_string1))