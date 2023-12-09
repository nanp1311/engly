# nanpapp
## 概要
- 英語学習支援アプリケーション
- 単語リストやAPIキーなどの各種データは~/.ll_dataに存在している
## インストール
- pip install -U appname
## 使用法
### List
- リストに登録されている単語の表示、単語をリストに登録
### Test
- リストに登録されている単語を出題、意味を4択から回答
### Reading
- ChatGPTを使って以下の情報を提供する
- > 英文に含まれる単語、熟語とその意味の表示
- > 英文の翻訳と主語動詞の表示
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
## 連絡先
- pengin.na11@gmail.com