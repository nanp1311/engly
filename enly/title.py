#!/usr/bin/python3
import os
import wx
import subprocess
from os.path import expanduser
from libs.common import json_write, set_font
from libs.newdate import HistoryWrite
import word_list
import word_test
import reading
import history

class SampleFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, title=title, pos=(0, 0), size=(400, 400))
        self.home_directory = expanduser("~")
        self.__create_widget()
        self.__do_layout()
        self.__data_setup()

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

    def __data_setup(self):
        if not os.path.exists(self.home_directory + "/.enly_data"):
            home_directory = expanduser("~")
            mk_directory = home_directory + "/.enly_data"
            data_dir = mk_directory + "/data"
            fig_dir = mk_directory + "/fig"
            res_json = data_dir + "/response.json"
            his_json = data_dir + "/history.json"
            word_json = data_dir + "/words.json"
            subprocess.call(["mkdir", mk_directory])
            subprocess.call(["mkdir", data_dir])
            subprocess.call(["mkdir", fig_dir])
            subprocess.call(["touch", res_json])
            subprocess.call(["touch", his_json])
            subprocess.call(["touch", word_json])
            json_write(res_json, {})
            json_write(his_json, {})
            init = HistoryWrite()
            init.history_init()
            json_write(word_json, {})
        else:
            pass

        # gitのエラー直す

    def list(self, event):
        #subprocess.Popen(["python3", "word_list.py"])
        word_list.main()

    def test(self, event):
        #subprocess.Popen(["python3", "word_test.py"])
        word_test.main()

    def reading(self, event):
        #subprocess.Popen(["python3", "reading.py"])
        reading.main()

    def history(self, event):
        #subprocess.Popen(["python3", "history.py"])
        history.main()

# アプリケーションクラス
class SampleApp(wx.App):
    def OnInit(self):
        frame = SampleFrame(None, -1, "Title")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

def main():
    app = SampleApp()
    app.MainLoop()

main()

# メイン
'''
if __name__ == "__main__":
    app = SampleApp()
    app.MainLoop()
'''