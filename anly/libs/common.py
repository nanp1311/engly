# 複数のファイルに共通する関数の定義
import os
import wx
import json
import re
import datetime

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
    return os.getcwd() + "/../" + dir + "/" + filename # 返すのはこの関数を実行したファイルが存在するパス

# 指定したサイズのフォントを返す
def set_font(i):
    return wx.Font(i, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

# history.jsonを今日までのデータに更新し、今日の日付を返す
def history_renewal():
    filename = path("history.json")
    history_data = json_open(filename)

    for key, value in history_data.items():
        pass
    
    ptn_year = '(\d+)-\d+-\d+'
    ptn_month = '\d+-(\d+)-\d+'
    ptn_day = '\d+-\d+-(\d+)'

    year = int(re.match(ptn_year, key).group(1))
    month = int(re.match(ptn_month, key).group(1))
    day = int(re.match(ptn_day, key).group(1))

    # 最終更新日と今日の日付を取得
    last_date = datetime.date(year, month, day)
    today = datetime.date.today()

    # 最終更新日と今日の日付の差を取得
    days_difference = abs((today - last_date).days)

    # 最終更新日から今日までのデータを入力
    for i in range(-days_difference+1, 1):
        record_day = today - datetime.timedelta(days=-i)
        history_data[str(record_day)] = {
            "total": value["total"]
        }

    # 更新内容をjsonファイルに書き込む
    json_write(filename, history_data)

    # 今日の日付を返す
    return str(today)