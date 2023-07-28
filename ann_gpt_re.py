from janome.tokenizer import Tokenizer
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import argparse

def wordcloud_make(file_path):
    t = Tokenizer()
    try:
        with open(file_path, encoding="shift-jis") as file:
            text = file.read()

        token = t.tokenize(text)
        word_list = []
        for line in token:
            tmp = re.split('\t|,', str(line))
            if tmp[1] == "名詞" and tmp[2] in ["一般", "固有名詞", "代名詞"]:
                word_list.append(tmp[0])

        return " ".join(word_list)

    except FileNotFoundError:
        print(f"エラー: ファイル '{file_path}' が見つかりませんでした。")
        return None
    except Exception as e:
        print(f"ファイル処理中にエラーが発生しました: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="CSVファイル内の日本語テキストからワードクラウドを生成します。")
    parser.add_argument("input_file", type=str, help="入力CSVファイルのパス。")
    args = parser.parse_args()

    word_txt = wordcloud_make(args.input_file)

    if word_txt:
        wordcloud = WordCloud(width=1200, height=800, background_color='black',
                              font_path=r"C:\Users\taniguchi\OneDrive\Word_annkert\IPAfont00303\ipamp.ttf").generate(word_txt)

        plt.figure(figsize=(8, 6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.savefig("jap1.png")
        print("ワードクラウド画像が 'jap1.png' として保存されました。")
    else:
        print("ワードクラウドの生成に失敗しました。")

if __name__ == "__main__":
    main()
