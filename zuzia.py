#!/usr/bin/python
# -*- coding: utf-8 -*-
# FridgeApp.py

import wx


class F(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(F, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&Fridge')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    F(None, -1, 'FridgeApp.py')
    app.MainLoop()


if __name__ == '__main__':
    main()