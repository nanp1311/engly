# 複数のファイルに共通する関数の定義
import wx
import json
from os.path import expanduser

# jsonファイルの読み込み
def json_open(filename):
    with open(filename, "r") as json_file:
        return json.load(json_file)

# jsonファイルに書き込み
def json_write(filename, json_data):
    with open(filename, "w") as json_file:
        json.dump(json_data, json_file, indent=2, ensure_ascii=False)

# ファイルのパスを返す
def path(filename, dir="data"):
    home = expanduser("~")
    return home + "/.engly_data/" + dir + "/" + filename # 返すのはこの関数を実行したファイルが存在するパス
# 指定したサイズのフォントを返す
def set_font(i):
    return wx.Font(i, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

# jsonファイルに単語と意味を追加する
def add_word(word, meaning, filename):
    json_data = json_open(filename)
    new_word = {
                "meaning": meaning,
                "correct": 0,
                "incorrect": 0
                }
    json_data[word] = new_word
    json_write(filename, json_data)