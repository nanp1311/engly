# engly
## 概要
- 英語学習支援アプリケーション
- jsonファイルは~/.engly_dataに存在している
- .local/binにinstallされる場合はsudo権限を使う
  - upgradeやuninstallにもsudoが必要になる
- Ubuntuだと色々めんどいからWindowsかMacを推奨
  - GUIアプリの実行環境、日本語化など
- PowerShellのコマンド
  - pip show engly: パッケージの保存場所
  - gcm engly | fl: exeファイルの保存場所
- [PyPI](https://pypi.org/)
- [TestPyPI](https://test.pypi.org/)
- [Python のプロジェクトをパッケージングする](https://packaging.python.org/ja/latest/tutorials/packaging-projects/)
- [Python でパッケージを開発して配布する標準的な方法 2023 年編](https://qiita.com/propella/items/5cd89caee6379920d889)

## TestPyPI
- python3 -m build
- python3 -m twine upload --repository testpypi dist/*
- python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps engly

## PyPI
- python3 -m build
- python3 -m twine upload dist/*
- python3 -m pip install engly

## 欲しい機能
- ChatGPTの履歴確認
- 品詞も出す
- Listの単語を順番に表示するボタン
- Listの単語をランダムに表示するボタン
- ユーザー側からのjsonファイルの指定
- ChatGPTの使い方の改良

## 疑問点
- tar.gzと.whlがなにかわからない(ソースとビルド済？)

## 1220-0110
- MacでListが動かない
- 一部のMacで文字の色がおかしい
- 言語のタブ分け
- メニューバー、終了方法の選択肢を増やす
- 英文の解説

## 1219
#### Version0.1.2
- Readingのテキストが一部表示されない不具合を修正したVersion0.1.2をリリース

#### テキストの表示が不完全
- ChatGPTの返答の最後の一行が表示されたりされなかったりする
- ウィンドウを最大化すると直る
```
You
StaticTextのサイズを調整する方法を教えてください。
ChatGPT
wx.StaticTextのサイズを調整するには、SetSizeまたはsizerを使用することが一般的です。以下に、これらの方法の例を示します。

SetSizeを使用する場合:
```
```python
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "StaticTextサイズの調整", size=(400, 200))

panel = wx.Panel(frame, wx.ID_ANY)
static_text = wx.StaticText(panel, wx.ID_ANY, "表示されなかったテキストがここに入ります。")

# StaticTextのサイズをテキストに合わせて調整
static_text.SetSize(static_text.GetBestSize())

frame.Show(True)
app.MainLoop()
```
```
Sizerを使用する場合:
```
```python
Copy code
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "StaticTextサイズの調整", size=(400, 200))

panel = wx.Panel(frame, wx.ID_ANY)
static_text = wx.StaticText(panel, wx.ID_ANY, "表示されなかったテキストがここに入ります.")

# Sizerを使用してStaticTextのサイズを調整
sizer = wx.BoxSizer(wx.HORIZONTAL)
sizer.Add(static_text, 1, wx.EXPAND)
panel.SetSizer(sizer)

frame.Show(True)
app.MainLoop()
```
```
これらの例では、SetSizeメソッドを使用するか、またはsizerを使ってStaticTextのサイズを調整しています。適切なサイズやレイアウトを見つけるために、アプリケーションの要件に応じて調整してみてください。
```
- Sizerはレイアウトに影響がでる可能性があるのでまずSetSizeの方を試す
- SetSizeでは表示に変化はなかった
- Sizerでも変化はなかった
- 別の方法を試す
```
StaticTextのサイズを調整する他の方法を教えてください。
ChatGPT
StaticTextのサイズを調整するために、以下の方法を検討できます。

SetMinSizeを使用する:
```
```python
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "StaticTextサイズの調整", size=(400, 200))

panel = wx.Panel(frame, wx.ID_ANY)
static_text = wx.StaticText(panel, wx.ID_ANY, "表示されなかったテキストがここに入ります.")

# StaticTextの最小サイズを設定
static_text.SetMinSize((200, -1))  # 幅200ピクセル、高さは自動調整

frame.Show(True)
app.MainLoop()
Wrapを有効にする:

python
Copy code
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "StaticTextサイズの調整", size=(400, 200))

panel = wx.Panel(frame, wx.ID_ANY)
static_text = wx.StaticText(panel, wx.ID_ANY, "表示されなかったテキストがここに入ります.", style=wx.ST_ELLIPSIZE_END|wx.WRAP)

frame.Show(True)
app.MainLoop()
```
```
Sizerを使用する（詳細な制御が可能）:
```
```python
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "StaticTextサイズの調整", size=(400, 200))

panel = wx.Panel(frame, wx.ID_ANY)
static_text = wx.StaticText(panel, wx.ID_ANY, "表示されなかったテキストがここに入ります.")

sizer = wx.BoxSizer(wx.HORIZONTAL)
sizer.Add(static_text, 0, wx.ALL|wx.EXPAND, 5)
panel.SetSizer(sizer)

frame.Show(True)
app.MainLoop()
```
```
これらの方法を組み合わせて試してみてください。たとえば、SetMinSizeとWrapを同時に使用することで、最小サイズを設定し、テキストがそれを超えた場合に自動的に改行されるようになります。
```
- SetMinSizeを試したところ，求めていた表示をしてくれた
- SetMinSizeで解決したためWrapは試していない

#### メニューバーの追加の検討
```Python
menuBar = wx.MenuBar()
menu = wx.Menu()
menuBar.Append(menu, '&File')
self.SetMenuBar(menuBar)
exit = menu.Append(-1, '&Exit', 'Terminate the application.')
self.Bind(wx.EVT_MENU, self.onExit)
```
- プログラム終了処理だけのバーを入れる必要はあるのか
- Listで複数のリストを選べるようにする機能を入れるならメニューバーを使いたい
- [MenuBar](https://www.python-izm.com/gui/wxpython/wxpython_menubar/)

## 1216
#### Listのcomboboxにスクロールを追加
```ChatGPT
wxPythonのcomboboxにスクロールをつけたいです。どうすればよいですか。
ChatGPT
wxPythonのComboBoxにスクロールを追加するには、以下の手順に従うことができます。

wx.EVT_COMBOBOX イベントを使用してコンボボックスの値が変更されたときに呼び出される関数を作成します。
その関数内で、SetMaxSize メソッドを使用してコンボボックスのサイズを制限します。
wx.VSCROLL スタイルを使用して、コンボボックスに垂直スクロールバーを追加します。
以下は、簡単な例です：
```
```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        choices = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
        combo_box = wx.ComboBox(panel, choices=choices, style=wx.CB_DROPDOWN | wx.VSCROLL)
        combo_box.Bind(wx.EVT_COMBOBOX, self.on_combobox_change)

        vbox.Add(combo_box, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)

        self.Centre()
        self.Show(True)

    def on_combobox_change(self, event):
        selected_value = event.GetString()
        print(f"Selected value: {selected_value}")

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame(None, "ComboBox with Scroll")
    app.MainLoop()
```
```ChatGPT
この例では、wx.CB_DROPDOWN | wx.VSCROLL スタイルを使用して、ドロップダウンスタイルのコンボボックスに垂直スクロールバーを追加しています。on_combobox_change 関数内でコンボボックスの値が変更されるたびに呼び出される処理を行うことができます。
```
- Windowsではスクロールが付いた、Ubuntuでは付かなかった、Macは不明

#### スクロール問題修正
- wx.lib.scrolledpanel.ScrolledPanelがWindowsで上手く表示されない
- 他の方法でスクロールを付ける
- ChatGPTに聞くと
```ChatGPT
You
wxPythonにて、wx.Frameのstyleにwx.VSCROLLを追加したところ、スクロールバーは表示されましたが実際の画面はスクロールされませんでした。スクロールバーと画面のスクロールを連動させる方法はありますか。
ChatGPT
wxPythonでwx.VSCROLLスタイルを使用して垂直スクロールバーを追加した場合、実際にスクロールできるようにするには、wx.ScrolledWindowを使用すると便利です。wx.ScrolledWindowは、自動的にスクロール領域を管理し、スクロールバーの操作に応じて画面をスクロールさせます。

以下は、wx.ScrolledWindowを使用して垂直スクロールバーを実現する基本的な例です：
```

```Python
import wx

class MyScrollableWindow(wx.ScrolledWindow):
    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent, style=wx.VSCROLL)

        self.SetScrollRate(0, 20)  # 垂直方向のスクロール単位を設定

        # スクロール領域に配置するコントロールなどをここで作成
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        # スクロール領域のサイズを設定（必要に応じて調整）
        self.SetVirtualSize((500, 1000))
        self.SetScrollbars(0, 20, 0, 50)  # スクロールバーのサイズを設定

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.DoPrepareDC(dc)

        # ここで描画処理などを行う

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Scrollable Window Example", size=(400, 300))
scrollable_window = MyScrollableWindow(frame)

frame.Show()
app.MainLoop()
```
```ChatGPT
この例では、wx.ScrolledWindowを継承したMyScrollableWindowクラスを作成し、その中でSetScrollRateやSetVirtualSizeなどのメソッドを使用してスクロールに関連する設定を行っています。また、wx.EVT_PAINTイベントに対するハンドラとしてOnPaintメソッドを定義し、ここでスクロール領域内の描画処理を行います。

この例を基に、スクロール領域内に配置するコントロールや描画内容を追加して、必要に応じてスクロール領域のサイズを調整してください。
```ChatGPT
You
app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Scrollable Window Example", size=(400, 300))
scrollable_window = MyScrollableWindow(frame)

frame.Show()
app.MainLoop()
この部分を
class SampleApp(wx.App):
    def OnInit(self):
        frame = SampleFrame(None, -1, "Reading")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

def main():
    app = SampleApp()
    app.MainLoop()
この形式に書き直してください。

ChatGPT
以下は、与えられたコードを新しい形式に書き直したものです。SampleApp クラスが OnInit メソッドをオーバーライドしてアプリケーションの初期化を行い、SampleFrame クラスを使用してメインウィンドウを作成します。main 関数は SampleApp をインスタンス化して MainLoop を呼び出します。
```
```Python
import wx

class MyScrollableWindow(wx.ScrolledWindow):
    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent, style=wx.VSCROLL)
        self.SetScrollRate(0, 20)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.SetVirtualSize((500, 1000))
        self.SetScrollbars(0, 20, 0, 50)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.DoPrepareDC(dc)

class SampleFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(400, 300))
        scrollable_window = MyScrollableWindow(self)

class SampleApp(wx.App):
    def OnInit(self):
        frame = SampleFrame(None, -1, "Scrollable Window Example")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

def main():
    app = SampleApp()
    app.MainLoop()

if __name__ == "__main__":
    main()
```
```ChatGPT
この形式では、SampleFrame クラスが MyScrollableWindow を使ってスクロール可能なウィンドウを作成し、SampleApp クラスが SampleFrame を使用してアプリケーションを初期化しています。main 関数は SampleApp をインスタンス化して MainLoop を呼び出し、アプリケーションを開始します。
```
- 以上の経緯からwx.ScrolledWindowを採用
- このコードを追加するだけでは画面の変更に合わせてスクロールを付けることができない
- SetScrollbarsとFitInsideを使うことで対応
```ChatGPT
You
self.SetScrollbars(1, 1, 1, 1)はどういう意味ですか。

ChatGPT
self.SetScrollbars(1, 1, 1, 1) は、wx.ScrolledWindow内で使用されるメソッドで、スクロールバーの設定を行います。このメソッドの引数は次の通りです：

最初の引数 (1): 水平方向のスクロールバーのページサイズ（スクロールバーの動き幅）を指定します。通常、横スクロールは使わないので1を指定しています。

二番目の引数 (1): 垂直方向のスクロールバーのページサイズを指定します。ここでは1を指定していますが、通常は表示領域内に収めるサイズを指定します。

三番目の引数 (1): 水平方向のスクロールバーの範囲（最小値から最大値までの範囲）を指定します。通常は使わないので1を指定しています。

四番目の引数 (1): 垂直方向のスクロールバーの範囲を指定します。通常は表示領域の高さを指定します。

このメソッドは、スクロールバーの設定を行い、スクロールバーの表示と動作を制御するために使用されます。ただし、実際にはスクロールバーの制御には SetupScrolling や手動の調整がより推奨されており、SetScrollbars を直接使用するよりも柔軟性があります。
```
```
You
FitInside()はなんですか。

ChatGPT
FitInside() メソッドは、wx.ScrolledWindow クラスに存在するメソッドで、ウィンドウ内の表示内容に基づいて、スクロール領域やスクロールバーを自動的に調整するためのメソッドです。

このメソッドを呼び出すと、wx.ScrolledWindowは内部のサブウィンドウやコントロールに合わせてスクロールバーを自動的に調整し、表示領域が最適な状態になります。特に、サブウィンドウやコントロールがサイズ変更されたり、新しいコントロールが追加されたりした場合に、FitInside()を呼び出すことでスクロールバーが正しく更新されます。

以下は FitInside() の簡単な使用例です：
```
```python
import wx

class MyScrollableWindow(wx.ScrolledWindow):
    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.text_ctrl.SetValue("ここに表示したい文章を設定してください。")

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.text_ctrl, 1, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizerAndFit(self.sizer)

        self.virtual_height = 1000

        # スクロールバーの初期化
        self.SetScrollbars(1, 1, 1, self.virtual_height)

        # スクロールイベントのバインド
        self.Bind(wx.EVT_SCROLLWIN, self.OnScroll)

    def OnScroll(self, event):
        # スクロールイベント発生時の処理
        self.Refresh()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.DoPrepareDC(dc)

        # 表示内容をスクロール位置に応じて描画
        dc.SetClippingRegion(0, self.GetScrollPos(wx.VERTICAL), self.GetClientSize().width, self.GetClientSize().height)
        self.panel.Refresh()

class SampleFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(400, 300))
        self.scrollable_window = MyScrollableWindow(self)

        # FitInside()メソッドを呼び出し、スクロールバーを調整
        self.scrollable_window.FitInside()

class SampleApp(wx.App):
    def OnInit(self):
        frame = SampleFrame(None, -1, "Scrollable Window Example")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

def main():
    app = SampleApp()
    app.MainLoop()

if __name__ == "__main__":
    main()

この例では、FitInside() メソッドが SampleFrame 内で使われています。 FitInside() メソッドの呼び出しにより、スクロール領域が適切に調整されます。
```
- wx.ScrolledWindowではSetupScrollingが使えなかった
- self.SetScrollbarsの引数は(20, 20, 1, 1)で設定

#### 一部のMacにて文字の色が変わってしまう問題を修正
- 原因不明
- コンボボックス以外の全てのコントロールに文字色を指定した
- 直ってるかどうかはわからない

## 1214
#### Listにて特定条件下で単語の意味が表示されない問題を修正
- Listの単語を削除した直後に同じ単語を登録しても意味が表示されない
- Listに登録されていない単語をshowした直後にその単語を登録しても意味が表示されない
- comboboxに入力されている単語が直前に入力した単語と違っていた場合は意味を更新する処理となっていたため、comboboxを更新しないまま単語の追加をしても反映されなかった
- flagを導入し、削除、追加を行うとflagがTrueになり、Trueの際に単語の意味を更新する条件を追加

#### Testの意味被りを修正
- 出題がkeyとなっていた
- 出題を単語にするだけだと、1つの単語に意味を複数登録していた場合、選択肢が被ってしまう
- 例えばhogeという単語にほげ1、ほげ2という意味が登録されていると、選択肢がほげ1、ほげ2、何か、何かのときにほげ1とほげ2のどちらが正解なのか判別不能となる
- 意味を複数登録していた場合、選択肢に出てくる意味はその内の1つのみとなるように修正
- 単語の判定をkeyで行うことで実装した

#### Testの実行判定の修正
- words.jsonのデータの数が4個未満なら実行しないようにしていた
- 1つの単語に複数の意味を登録した場合単語が4個未満でもデータの数が4個以上となる状況を作ることができた
- 異なる単語の数が4個未満なら実行できないように修正した

#### ウィンドウの初期位置を真ん中にする
- pos=(x, y)で位置の指定, frame.Centre()で中心に作られる
- Ubuntuでは適用されない
- [Frame - 表示位置の指定](https://www.python-izm.com/gui/wxpython/wxpython_frame/#i-3)

#### osの判定、os毎にウィンドウサイズを変更する
- platformモジュールを使用
- __init__内でosを判定しsizeの値を変更する
```ChatGPT
You
Pythonで使用中のos(windows, Mac, Linux)を判定するプログラムを書いてください。
ChatGPT
PythonでOSを判定するためには、platformモジュールを使用すると便利です。以下は、OSがWindows、Mac、またはLinuxであるかを判定するプログラムの例です。
```
```python
import platform

def detect_os():
    system = platform.system()

    if system == "Windows":
        return "Windows"
    elif system == "Darwin":
        return "Mac"
    elif system == "Linux":
        return "Linux"
    else:
        return "Unknown"

if __name__ == "__main__":
    os_name = detect_os()
    print(f"The current operating system is: {os_name}")
```
```ChatGPT
このプログラムでは、platform.system()を使用して現在のOSを取得し、それに基づいて判定を行います。これを実行すると、現在のOSが表示されます。
```

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
- ソース配布の.tar.gzとビルド配布の.whl
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

## pyproject.toml_memo
```
[tool.poetry.dependencies]
python = "^3.8"
openai = "0.28"
wxPython = "4.2.1"
plotly = "5.16.1"

numpy = { version = "1.21.2", python = "^3.8" }
```

## アプリ名考案
- word, list, reading, english, learning, study, assist, support, comprehension, analyze, language

## ChatGPT_API
### system: 役柄、役割を指定する(誰に聞くか)
- "あなたは初学者に英語を教えるアシスタントです。"
  - なんか無限？に返答しだした
- "あなたは英語が得意なアシスタントです。"
  - 一番正確に返してくれた気がする
- "あなたは英和辞典です。" 
  - 若干指定した形式と違う形だったり、無駄な文章入れたりする

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