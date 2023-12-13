# engly
## 概要
- 英語学習支援アプリケーション
- jsonファイルは~/.engly_dataに存在している
- testPyPIに公開
- windowsでも動いた
- 必要なパッケージの処理をどうするのかがわからない、自動で追加
- tar.gzと.whlがなにかわからない(ソースとビルド済？)
- LICENSE合ってるかわからない
- .local/binにinstallされる場合はsudo権限を使う -> uninstallにもsudoが必要になる
- アプリ名考える -> dataディレクトリの名前変える
- 複数単語の処理 -> comboboxの内部データに意味を格納する？
- gcm notepad | fl
- windowsだとreadingのレイアウトがおかしい -> スクロール関連の影響？
- win: 0.0.3.6, linux: 0.0.3.7 (12/12現在)

## TestPyPI
- python3 -m build
- python3 -m twine upload --repository testpypi dist/*
- python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps engly

## PyPI
- python3 -m build
- python3 -m twine upload dist/*
- python3 -m pip install engly

```
[tool.poetry.dependencies]
python = "^3.8"
openai = "0.28"
wxPython = "4.2.1"
plotly = "5.16.1"

numpy = { version = "1.21.2", python = "^3.8" }
```

## 正式リリースまでの課題
- ChatGPTの履歴確認
- 品詞も出す
- ウインドウの大きさの自動調節、初期位置指定

## アプリ名
- word, list, reading, english, learning, study, assist, support, comprehension, analyze, language

## 1213
- 各ウィンドウの色を変更

## 1212
- Reading, testのエラー判定をtitleで行うように変更
- ReadingのAPIキーが間違っていた時にエラーメッセージを表示するように変更
- Readingのウィンドウにスクロールを追加
- Readnigのテキストボックスが空の際はChatGPTにアクセスしないように変更

## 1211
- listに単語の意味を複数登録、表示できる機能を追加

## 1209
- README.md整理、アプリ仕様やインストール方法などを記述
- MANIFEST.inにREADME.md, LICENSEを追加、MEMO.mdを除外する記述を追加

## 1207
- 単語リストに単語削除機能追加
- APIキー未入力の場合readingが使用できないように変更
- PyPIにアップロード

## 1206
- 英語のテキストを来週までに -> TOEIC公式問題集
- 来週までに人がアプリを使えるように
- 12/13から一ヶ月間を使ってアプリの効果を計る
- まず適当なテキストを選ぶ
- 何もせずに問題を解く
- 1ヶ月間アプリを使って勉強する
- 1ヶ月後もう一度テストを解いて結果を記録する

## 1205
- titleで作成した各種ファイルを初期化するプログラムを実装
- newdateにhistory_init()とreturn_today()を実装
- newdateにHistoryWriteクラスを実装
- クラスを使用する際は必ずインスタンスを生成する(init = HistoryWrite()みたいな感じ)
- titleの__setup_dataにディレクトリ存在判定を追加
- api/apikeyを.ll_dataに作成
- apiキーはapikeyファイルから読みだすように変更
- apiキーを保存する機能をtitleに追加
- tomlファイルを作成
- ソース配布の.tar.gzとビルド配布の.whl -> 要検索
- ディレクトリ作成をmkdirからos.makedirsに変更
- ファイル作成をwith openで行うように変更
- fig.htmlをtry文を用いてwebbrowserかsubprocessで開くように変更

## 1204
- 各種プログラムの呼び出しをdef main()に変更
- jsonファイルの管理を.ll_data(仮)に変更
- pathで返すパスをホーム直下.ll_dataに変更
- ホーム直下に.ll_data(仮)を作成するプログラムを実装
```ファイル構造
├── data
│   ├── history.json
│   ├── response.json
│   └── words.json
└── fig
    └── fig.html
```

## 1201
- モジュールapikey.pyを作成
- reading.pyのコードを整理

## 1130
- モジュールcommon.py, newdate.pyを作成
- word_list.py, word_test.py, history.pyのコードを整理

## ChatGPT_API
### system: 役柄、役割を指定する(誰に聞くか)
- "あなたは初学者に英語を教えるアシスタントです。"
- > なんか無限？に返答しだした
- "あなたは英語が得意なアシスタントです。"
- > 一番正確に返してくれた気がする
- "あなたは英和辞典です。" 
- > 若干指定した形式と違う形だったり、無駄な文章入れたりする

### assistant: ChatGPTの返答を入れる？
- "英単語の意味を日本語で簡潔に回答します。"
- "英文を単語や熟語に分解し、それらの簡潔な意味を日本語を使ってword: meaningという形で表示します。"
- 返答しているのがassistant
- ChatGPTにさせたいことをassistantに入力する？「私はこういうことができます。」と言わせることでChatGPT側の能力や立場をより明確にしている？
- assistantにやって欲しいこと(単語を指定の形式で表示)を入力したが、エラーコードの際に上手く動作しなかった(英文全体の日本語訳のみが表示された)
- 「翻訳などの場合はassistantに英文を入れる」という記事もあったが、上手くいかなかった(英文が存在しない、という返答があるなど)

### user: 質問内容(何を聞くか)
- 明確、具体的に
- 英語に翻訳しやすい日本語(?)
- 追加質問、指定 -> そういう枠も作る？(質問コーナー的な)
- ここに入力したものが優先されている？一番効力がある感じがする

## 例文
Before when we've had a fake implementation, it has been obvious how to work backward to the real implementation.