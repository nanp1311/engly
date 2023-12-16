import wx
import platform
from libs.common import json_open, json_write, path, set_font, add_word

class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        system = platform.system()
        if system == "Windows":
            self.x = 600
            self.y = 300
        else:
            self.x = 800
            self.y = 400
        wx.Frame.__init__(self, parent, title=title, pos=(100, 100), size=(self.x, self.y))

        self.filename = path("words.json")
        self.select_word = ""
        self.tmpword = " "
        self.flag = False

        self.__create_widget()
        self.__do_layout()
        self.__set_word()

        self.Show()

    def __create_widget(self):
        self.SetBackgroundColour((224, 224, 224))

        # リストボックスの作成
        self.list_box = wx.ListBox(self, choices=[""], style=wx.LB_SINGLE)
        self.list_box.Bind(wx.EVT_LISTBOX, self.on_listbox_selected)

        # 意味を表示するテキスト
        self.txt_meaning = wx.StaticText(self, -1, "", style=wx.TE_CENTER)
        self.txt_meaning.SetFont(set_font(25))

        # 単語入力用のテキストボックス
        self.word = wx.StaticText(self, -1, "word", style=wx.TE_CENTER)
        self.txtCtrl_word = wx.TextCtrl(self, -1, size=(430, 25))

        # 意味入力用のテキストボックス
        self.meaning = wx.StaticText(self, -1, "meaning", style=wx.TE_CENTER)
        self.txtCtrl_meaning = wx.TextCtrl(self, -1, size=(430, 25))

        # 単語追加成功報告テキスト
        self.btn_add = wx.Button(self, -1, "add")
        self.btn_add.Bind(wx.EVT_BUTTON, self.push_add)

        self.txt_success = wx.StaticText(self, -1, "", style=wx.TE_CENTER)
        self.txt_success.SetForegroundColour('#0000FF')
        self.txt_success.SetFont(set_font(15))

    def __do_layout(self):
        sizer_all = wx.BoxSizer(wx.VERTICAL)

        # リストボックスの配置
        sizer_all.Add(self.list_box, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

        # 意味を表示するテキストの配置
        sizer_all.Add(self.txt_meaning, flag=wx.ALIGN_CENTER)

        # 単語入力用のテキストボックスの配置
        sizer_wd = wx.BoxSizer(wx.HORIZONTAL)
        sizer_wd.Add(self.word, flag=wx.ALIGN_CENTER)
        sizer_wd.Add(self.txtCtrl_word, flag=wx.ALIGN_CENTER | wx.LEFT, border=35)
        sizer_all.Add(sizer_wd, flag=wx.ALIGN_CENTER | wx.ALL, border=5)

        # 意味入力用のテキストボックスの配置
        sizer_mn = wx.BoxSizer(wx.HORIZONTAL)
        sizer_mn.Add(self.meaning, flag=wx.ALIGN_CENTER)
        sizer_mn.Add(self.txtCtrl_meaning, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)
        sizer_all.Add(sizer_mn, flag=wx.ALIGN_CENTER | wx.ALL, border=5)

        # 単語追加成功報告テキストの配置
        sizer_all.Add(self.btn_add, flag=wx.ALIGN_CENTER)
        sizer_all.Add(self.txt_success, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)

        self.SetSizer(sizer_all)

    def __set_word(self):
        self.wordlist = [""]
        self.keylist ={"":""}
        self.meaninglist = {"": "Please enter a word"}
        json_data = json_open(self.filename)
        for key, value in json_data.items():
            self.wordlist.append(value["word"])
            self.keylist[key] = value["word"]
            self.meaninglist[key] = value["meaning"]
        self.wordlist = list(set(self.wordlist))
        self.list_box.Set(self.wordlist)

    def on_listbox_selected(self, event):
        selected_index = self.list_box.GetSelection()
        selected_word = self.list_box.GetString(selected_index)
        self.select_word = selected_word.strip()

        try:
            if len(self.meaninglist[self.select_word]) > 30:
                self.txt_meaning.SetFont(set_font(20))
            else:
                self.txt_meaning.SetFont(set_font(25))

            self.txt_meaning.SetLabel(self.meaninglist[self.select_word])
            self.txt_meaning.SetForegroundColour('#000000')
            self.show_key = self.select_word
            if self.show_key != "":
                self.btn_delete.Enable()
            else:
                self.btn_delete.Disable()
        except:
            self.txt_meaning.SetLabel("Unregistered word")
            self.txt_meaning.SetForegroundColour('#FF0000')

        self.Layout()

    def push_add(self, event):
        word = self.txtCtrl_word.GetValue().strip()
        meaning = self.txtCtrl_meaning.GetValue().strip()
        key = word
        self.flag = True
        i = 2

        if word != "" and meaning != "":
            while key in self.keylist:
                key = word + str(i)
                i += 1

            add_word(word, meaning, key, self.filename)
            self.wordlist.append(word)
            self.keylist[key] = word
            self.meaninglist[key] = meaning

            if not word in self.list_box.GetItems():
                self.list_box.Append(word)

            self.txt_success.SetForegroundColour('#0000FF')
            self.txt_success.SetLabel("\"" + word + "\" " + "added.")

            self.txtCtrl_word.Clear()
            self.txtCtrl_meaning.Clear()
        else:
            self.txt_success.SetForegroundColour('#FF0000')
            self.txt_success.SetLabel("Enter a word and meaning.")

        self.Layout()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "Wordlist")
        frame.Centre()
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
