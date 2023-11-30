#!/usr/bin/python3
import wx
import openai
from libs.apikey import APIKEY
import json
from libs.common import json_open, json_write, path

openai.api_key = APIKEY

class SampleFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, title=title, pos=(0, 0), size=(1200, 1000))
        # 返答文のフォント
        self.font = wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        # テキストボックスのフォント
        self.font_Ctrl = wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        # ChatGPTの返答を入れる変数
        self.text_m = ""
        self.text_t = ""
        # テキストボックスの内容を入れる変数
        self.val_m = "///"
        self.val_t = "///"
        # ファイルパスの指定
        self.file_words = path("words.json")
        self.file_response = path("response.json")
        # カウントのための変数
        self.i = 0
        self.c = 0
        # 必要なやつ
        self.__create_widget()
        self.__do_layout()

    # Widgetを作成するメソッド
    def __create_widget(self):
        # テキストボックス
        self.txtCtrl = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE, size=(500, 80))
        self.txtCtrl.SetFont(self.font_Ctrl)
        
        # wordボタン
        self.button_m = wx.Button(self, label="word")
        self.button_m.Bind(wx.EVT_BUTTON, self.OnButton_m)

        # transボタン
        self.button_t = wx.Button(self, label="trans")
        self.button_t.Bind(wx.EVT_BUTTON, self.OnButton_t)

        # 返答文表示
        self.txt = wx.StaticText(self, -1, "", style=wx.TE_LEFT)
        self.txt.SetFont(self.font)

    # レイアウトを設定するメソッド
    def __do_layout(self):
        # 各sizer定義
        self.sizer_all = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_btn = wx.BoxSizer(wx.VERTICAL)
        self.sizer_txt = wx.BoxSizer(wx.VERTICAL)
        self.sizer_word = wx.BoxSizer(wx.VERTICAL)
        
        # テキストボックス
        self.sizer.Add(self.txtCtrl, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        # word, transボタン
        self.sizer_btn.Add(self.button_m, flag=wx.ALIGN_CENTER | wx.TOP, border=5)
        self.sizer_btn.Add(self.button_t, flag=wx.ALIGN_CENTER | wx.TOP, border=5)
        # テキストボックスとボタンを結合
        self.sizer.Add(self.sizer_btn, flag=wx.ALIGN_CENTER | wx.ALL, border=0)
        self.sizer_all.Add(self.sizer, flag=wx.ALIGN_CENTER | wx.ALL, border=30)

        # 単語保存用ボタン、返答表示用テキストを結合
        self.sizer_txt.Add(self.sizer_word, flag=wx.ALIGN_LEFT | wx.TOP, border=0)
        self.sizer_txt.Add(self.txt, flag=wx.ALIGN_LEFT | wx.TOP, border=20)

        # 全てを合体しセット
        self.sizer_all.Add(self.sizer_txt, flag=wx.ALIGN_LEFT | wx.LEFT, border=100)
        self.SetSizer(self.sizer_all)

    # ボタン押したときの処理
    def OnButton_m(self, event):
        # テキストボックスが更新されていれば返答をリセット
        if self.txtCtrl.GetValue() != self.val_m:
            self.text_m = ""
            self.c = 0
            # 新たな返答を受けとる前に古い返答のボタンを削除
            if self.i != 0:
                count = self.i
                for i in range(0, count):
                    exec("self.btn_{}.Destroy()".format(i))
        # テキストボックスの内容を受け取りChatGPTに質問
        if self.text_m == "":# & self.txtCtrl.GetValue() != "":
            self.val_m = self.txtCtrl.GetValue()
            ques = self.val_m + "この英文に出てくる単語や熟語の意味をword: meaningという形で表示してください。"
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは英語が得意なアシスタントです。" }, 
                {"role": "assistant", "content": "英単語の意味を日本語で簡潔に回答します。"}, 
                {"role": "user", "content": ques} 
            ],
            temperature=0,
            top_p = 0
            )
            self.text_m = response['choices'][0]['message']['content'].strip()
            # ChatGPTの返答をjsonファイルに保存
            if self.c == 0:
                with open(self.file_response, "r") as json_file:
                    json_data = json.load(json_file)
                new_word = {
                    "tag": "Word",
                    "sentence": self.val_m,
                    "response": self.text_m
                }
                json_data["ChatGPT"].append(new_word)
                with open(self.file_response, "w") as json_file:
                    json.dump(json_data, json_file, indent=4, ensure_ascii=False)
                self.c += 1
            # 返答に含まれる単語と意味をボタン化 -> 機能はdef add
            print(self.text_m)
            self.text_word = self.text_m.replace("- ", "").split('\n') #前に書かれてる方から処理する
            #.replace(" - ", ": ")
            self.i = 0
            for word in self.text_word:
                if ": " in word:
                    exec("self.btn_{} = wx.Button(self, label=word)".format(self.i))
                    exec("self.btn_{}.Bind(wx.EVT_BUTTON, self.add)".format(self.i))
                    exec("self.sizer_word.Add(self.btn_{}, flag=wx.ALIGN_LEFT | wx.TOP, border=10)".format(self.i))
                    self.i += 1
        self.Layout()
    
    def add(self, event):
        # 押したボタンの情報を取得
        btn = event.GetEventObject()
        # ボタンのラベルを取得し分解
        content = btn.GetLabel().split(': ')
        # 単語と意味の保存
        with open(self.file_words, "r") as json_file:
            json_data = json.load(json_file)
        new_word = {
            "meaning": content[1].strip(),
            "correct": 0,
            "incorrect": 0
        }
        json_data[content[0].strip()] = new_word
        with open(self.file_words, "w") as json_file:
            json.dump(json_data, json_file, indent=2, ensure_ascii=False)
        # ボタンを押せるのは一度だけ
        btn.Disable()

    def OnButton_t(self, event):
        # テキストボックスが更新されていれば返答をリセット
        if self.txtCtrl.GetValue() != self.val_t:
            self.text_t = ""
            self.c = 0
        # テキストボックスの内容を受け取りChatGPTに質問
        if self.text_t == "":# & self.txtCtrl.GetValue() != "":
            self.val_t = self.txtCtrl.GetValue()
            ques = self.val_t + "この英文の日本語訳を表示してください。それに加え、この英文の主語と動詞を英語で表示してください。"
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "あなたは英語が得意なアシスタントです。"},
                    #{"role": "assistant", "content": "この英文の日本語訳を表示します。それに加え、この英文の主語と動詞を英語で表示します。"},
                    {"role": "user", "content": ques}
            ],
            temperature=0,
            top_p = 0
            )
            print(response['choices'][0]['message']['content'])
            self.text_t = response['choices'][0]['message']['content'].strip()
            # ChatGPTの返答をjsonファイルに保存
            if self.c == 0:
                with open(self.file_response, "r") as json_file:
                    json_data = json.load(json_file)
                new_word = {
                    "tag": "Translation",
                    "sentence": self.val_t,
                    "response": self.text_t
                }
                json_data["ChatGPT"].append(new_word)
                with open(self.file_response, "w") as json_file:
                    json.dump(json_data, json_file, indent=4, ensure_ascii=False)
                self.c += 1
        # ChatGPTの返答を表示
        self.txt.SetLabel(self.text_t)
        self.Layout()

# アプリケーションクラス
class SampleApp(wx.App):
    def OnInit(self):
        frame = SampleFrame(None, -1, "Reading")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

# メイン
if __name__ == '__main__':
    app = SampleApp()
    app.MainLoop()

"""例文
So, even though it feels a little speculative we'll work forward.
Perhaps later we'll optimize the special case of adding two identical currencies, but that's later.
Did you know that the first argument to addition is called the augend?
I didn't until I was writing this. Geek joy.
It is deeply con cerned with the implementation of our operation, rather than its externally vis ible behavior.
This code should work with any Expression.
"""

#役柄、役割を指定する(誰に聞くか)
    # "あなたは初学者に英語を教えるアシスタントです。"
    # -> なんか無限？に返答しだした
    # "あなたは英語が得意なアシスタントです。"
    # -> 一番正確に返してくれた気がする
    # "あなたは英和辞典です。" 
    # -> 若干指定した形式と違う形だったり、無駄な文章入れたりする

# ChatGPTの返答を入れる？
    # "英単語の意味を日本語で簡潔に回答します。"
    # "英文を単語や熟語に分解し、それらの簡潔な意味を日本語を使ってword: meaningという形で表示します。"
    #  返答しているのがassistant
    # ChatGPTにさせたいことをassistantに入力する？「私はこういうことができます。」と言わせることでChatGPT側の能力や立場をより明確にしている？
    # assistantにやって欲しいこと(単語を指定の形式で表示)を入力したが、エラーコードの際に上手く動作しなかった(英文全体の日本語訳のみが表示された)
    # 「翻訳などの場合はassistantに英文を入れる」という記事もあったが、上手くいかなかった(英文が存在しない、という返答があるなど)

#質問内容(何を聞くか)
    # 明確、具体的に
    # 英語に翻訳しやすい日本語(?)
    # 追加質問、指定 -> そういう枠も作る？(質問コーナー的な)
    # ここに入力したものが優先されている？一番効力がある感じがする