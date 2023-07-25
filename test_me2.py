# ライブラリのインポート
import MeCab
import csv

# 形態素解析のパーサーの設定
tagger = MeCab.Tagger("-Owakati")

# 例文
test_string = '「すもも」もももももものうち'

# 形態素解析
print(tagger.parse(test_string))

f = open('an.csv')
# ファイル終端まで全て読んだデータを返す
text = f.read()  
f.close()

