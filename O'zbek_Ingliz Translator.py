# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 17:58:36 2025

@author: HP
"""

# wxPython
import wx
from googletrans import Translator

tarjimon = Translator()

class MyFrame(wx.Frame):  # <-- to‘g‘risi Frame
    def __init__(self):
        super().__init__(parent=None, title="O'zbek-Ingliz lug'at")  # <-- / belgisi olib tashlandi
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        
        my_btn = wx.Button(panel, label='TARJIMA')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)  # <-- | wx.CENTER to‘g‘rilandi
        
        self.text_out = wx.TextCtrl(panel, style=wx.TE_READONLY)
        my_sizer.Add(self.text_out, 0, wx.ALL | wx.EXPAND, 5)
        
        panel.SetSizer(my_sizer)  # <-- SetSizer to‘g‘ri yozildi
        self.Show()
        
    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            self.text_out.SetValue("So'z kiritmadingiz")
        else:
            tarjima = tarjimon.translate(value, src='uz', dest='en')  # <-- valur -> value
            self.text_out.SetValue(tarjima.text.capitalize())  # <-- SetValue

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
