# engly
## 概要
- 英語学習支援アプリケーション
- GUI
- 単語リストやAPIキーなどの各種データは~/.engly_dataに存在している
## インストール
- pip install -U engly
## 使用法
### List
- リストに登録されている単語の表示、単語をリストに登録
### Test
- リストに登録されている単語を出題、意味を4択から回答
### Reading
- ChatGPTを使って以下の情報を提供する
> 英文に含まれる単語、熟語とその意味の表示
> 英文の翻訳と主語動詞の表示
### History
- Testで正解した回数のグラフを表示
### apikey
- apikeyの入力
## 依存関係
- openai ~= 0.28
- wxPython ~= 4.2.1
- plotly ~= 5.16.1
## ライセンス
- MITライセンス
## Version
### 0.0.4.5
- Readingの返答が保存できない不具合を修正
### 0.0.4.4
- WindowsでReadingが実行できない不具合を修正
### 0.0.4.2
- Windowsでのウィンドウサイズの調整
- 1つの単語に複数の意味を登録していれば単語が3つ以下でもTestを実行できてしまう不具合を修正
- 1つの単語に複数の意味を登録していた場合、Testでその単語が出題されたときの選択肢に出現する意味はその中の1つのみとなるように修正
- Listの単語を削除を行った後、もしくは登録されていない単語を入力してshowボタンを押し"Unregisterd word"が表示された後、すぐにその単語を登録してshowを押しても意味が表示されない不具合を修正
- 一部のMacにて文字色が変わってしまう不具合を修正
### 0.0.4.1
- Windowsとその他のosでウィンドウサイズが変わるように変更
### 0.0.4
- 各ウィンドウが画面の中心に表示されるように変更