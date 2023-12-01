#!/usr/bin/python3
import wx
import subprocess
from libs.common import set_font

class SampleFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, title=title, pos=(0, 0), size=(400, 400))
        self.__create_widget()
        self.__do_layout()

    def __create_widget(self):
        self.txt = wx.StaticText(self, label = "Menu")
        self.txt.SetFont(set_font(40))

        self.btn_list = wx.Button(self, label="List")
        self.btn_list.Bind(wx.EVT_BUTTON, self.list)

        self.btn_test = wx.Button(self, label="Test")
        self.btn_test.Bind(wx.EVT_BUTTON, self.test)

        self.btn_reading = wx.Button(self, label="Reading")
        self.btn_reading.Bind(wx.EVT_BUTTON, self.reading)

        self.btn_history = wx.Button(self, label="History")
        self.btn_history.Bind(wx.EVT_BUTTON, self.history)

    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.txt, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        sizer.Add(self.btn_list, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        sizer.Add(self.btn_test, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        sizer.Add(self.btn_reading, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        sizer.Add(self.btn_history, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        self.SetSizer(sizer)

    def list(self, event):
        subprocess.Popen(["python3", "word_list.py"])

    def test(self, event):
        subprocess.Popen(["python3", "word_test.py"])

    def reading(self, event):
        subprocess.Popen(["python3", "reading.py"])

    def history(self, event):
        subprocess.Popen(["python3", "history.py"])

# アプリケーションクラス
class SampleApp(wx.App):
    def OnInit(self):
        frame = SampleFrame(None, -1, "Test")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

# メイン
if __name__ == "__main__":
    app = SampleApp()
    app.MainLoop()
