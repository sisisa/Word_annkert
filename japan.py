import MeCab  # MeCab: 日本語の形態素解析ライブラリ
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 日本語のテキストデータ（例として、日本の都道府県名を使用します）
japanese_text = """
北海道 青森 岩手 宮城 秋田 山形 福島 茨城 栃木 群馬 埼玉 千葉 東京 神奈川 新潟 富山 石川 福井 山梨 長野 岐阜 静岡 愛知 三重 滋賀 京都 大阪 兵庫 奈良 和歌山 鳥取 島根 岡山 広島 山口 徳島 香川 愛媛 高知 福岡 佐賀 長崎 熊本 大分 宮崎 鹿児島 沖縄
"""

# MeCabを使ってテキストを単語に分割する関数
def japanese_tokenizer(text):
    mecab = MeCab.Tagger("-Owakati")
    return mecab.parse(text).split()

# ワードクラウドの設定と生成
wordcloud = WordCloud(
    background_color="white",  # 背景色を白に設定
    width=800,
    height=400,
    font_path="path/to/your/font.ttf",  # 日本語フォントのパスを指定
    collocations=False,  # 連語（bigram）を考慮しないように設定
).generate(" ".join(japanese_tokenizer(japanese_text)))

# ワードクラウドの描画
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # 軸を非表示に設定
plt.show()
