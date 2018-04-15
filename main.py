#!/usr/bin/python
# -*- coding: utf-8 -*-
# FridgeApp.py

import wx, math, sqlite3, webbrowser
from operator import itemgetter


con = sqlite3.connect('baza.db')

c = con.cursor()

c.execute('SELECT * FROM posts')

all_rows = c.fetchall()


class F(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(F, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        self.recipeMenu = wx.Menu()
        textMenu = wx.Menu()
        self.resetMenu = wx.Menu()

        fitem = textMenu.Append(wx.ID_ANY, 'Autorzy')
        fitem = textMenu.Append(wx.ID_ANY, 'Jak działa kod')
        menubar.Append(self.recipeMenu, '&Znajdź przepis')
        menubar.Append(self.resetMenu, '&Wyczyść')
        menubar.Append(textMenu, '&O nas')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU_OPEN, self.tf)

        vbox = wx.BoxSizer()
        skladniki = open('Składniki.txt', 'r')
        l = skladniki.readlines()
        ncol = 7
        nrow = math.ceil(len(l)*1.0/ncol)
        self.gs = wx.GridSizer(nrow, ncol, 3, 3)
        for elem in l:
            btn = wx.ToggleButton(self, label=elem.capitalize())
            def OnButton(event, button_label=elem):
                print("In OnButton:", button_label)

            btn.Bind(wx.EVT_BUTTON, OnButton)
            self.gs.Add(btn, 0, wx.EXPAND, 10)

        vbox.Add(self.gs, proportion=1, flag=wx.EXPAND)

        self.SetSizer(vbox)
        self.SetSize((1200, 700))
        self.SetTitle('FridgeApp')
        self.Centre()
        self.Show(True)

    def tf(self, event): #funkcja true/false,
        if event.GetMenu() == self.recipeMenu:
            lodowka=[]
            children=self.gs.GetChildren()
            for child in children:
                widget = child.GetWindow()
                if widget.GetValue() == True:
                    lodowka.append(widget.GetLabel()[:len(widget.GetLabel())-1])

            lista = []
            listaproc = []

            for i in all_rows:
                k = i[1].lower()
                n = []
                m = k.split(', ')
                for elem in m:
                    n.append(elem.capitalize())
                l = set(lodowka).intersection(n)
                if len(l) != 0:
                    lista.append(i[0])
                    listaproc.append(int((len(l) / len(m)) * 100))

            slownik = dict(zip(lista, listaproc))
            koniec = sorted(slownik.items(), key=itemgetter(1), reverse=True)

            count = 1

            es = ""  # empty string

            if len(koniec) != 0:
                for elem in koniec[0:5]:
                    if elem[1] != 0:
                        es += "{0}. {1} - {2}%\n".format(count, elem[0], elem[1])
                    count += 1

                dial = wx.MessageDialog(None, es + '\nWyszukać najlepszy wynik w Google?', 'Propozycje dań', wx.YES_NO)
                dial.SetYesNoLabels('&Tak', '&Nie')

                if dial.ShowModal() == wx.ID_YES:
                    przepis = koniec[0][0].split(' ')
                    query = '+'.join(przepis)
                    webbrowser.open('http://www.google.com/search?q={0}+przepis'.format(query))


            else:
                es+="Nie znalazłem pasujących dań! \n"
                dial = wx.MessageDialog(None, es, 'Ups!', wx.OK)
                dial.ShowModal()





        elif event.GetMenu() == self.resetMenu:
            children = self.gs.GetChildren()
            for child in children:
                widget=child.GetWindow()
                widget.SetValue(False)





    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    F(None, -1, 'FridgeApp.py')
    app.MainLoop()

if __name__ == '__main__':
    main()
