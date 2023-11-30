from .common import json_open, json_write, path
import re
import datetime

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