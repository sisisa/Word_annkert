import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random
import codecs

words = [['観念的',50],['ポジティブ',150],['ロジカル',150],['素直',150],['達観',150],['冷静',150],['安定',50],['ミステリアス',50],['強火ポジティブ',150],['納得感',150],['戦略的',150],['本質的自分ファースト',150],['こだわり',150],['仕事人間',150],['ストイック',150],['年末年始長くとって',150],['休んで',150],['楽しければ良いけどね！',150],['落着いている',50],['温か',50],['分析家',150],['肌ラボ！',150],['趣味も仕事も全力！',150],['落ち着いてる',150],['アルゴリズム',150],['ワーカホリック',150],['ストイック',150],['真面目',150],['完璧主義',150],['アルゴリズム',150],['真面目',50],['物好き',50],['MacbookPro',150],['シンプル',150],['こだわり派',150],['深める',150],['へこたれない',150],['ドリーマー',50],['フリーダム',50],['滑るギャグ',150],['同じ土俵には立ちません',150],['変化を求める',150],['こだわり',150],['バルス！',550]]

fpath = r'C:\Users\taniguchi\OneDrive\Word_annkert\IPAfont00303\ipamp.ttf'

def show_word_cloud(ws):
    # 前処理
    # 単語をスペースで区切った１文にする。
    # 出現回数分、appendしている。
    ws_show = []
    for i in range(len(ws)):
        word_times = ws[i][1]
        if word_times>0:
            for j in range(word_times):
                ws_show.append(ws[i][0])
    # 綺麗に整列してると、「あああ あああ」という単語と判断されるので、シャッフル
    random.shuffle(ws_show)
    # スペース区切りにする
    texts = ' '.join(ws_show)
    #print(texts)
    
    # 描画
    wc = WordCloud(background_color="black", font_path=fpath, 
                   width=820, height=312, regexp=r"[\w']+").generate(texts)
    plt.figure(figsize=(15,12))
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

show_word_cloud(words)