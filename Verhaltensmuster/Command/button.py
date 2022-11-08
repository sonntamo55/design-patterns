from __future__ import annotations
from abc import ABC, abstractmethod

# Shortcuts ###############################################
class Shortcut(ABC):

    editor:Editor
    app:App
    
    def __init__(self, app:App, editor:Editor):
        self.editor = editor
        self.app = app

    @abstractmethod
    def hit(self):
        pass

class KopierenShortcut(Shortcut):

    def hit(self):
        self.app.setze_kopierten_text(self.editor.get_selection())

class EinfuegenShortcut(Shortcut):

    def hit(self):
        self.editor.enter(self.app.kopierter_text)

class AusschneidenShortcut(Shortcut):

    def hit(self):
        txt = self.editor.get_selection()
        self.editor.enter("")
        self.app.setze_kopierten_text(txt)

# Buttons #################################################
class Button(ABC):

    editor:Editor
    app:App

    def __init__(self, app:App, editor:Editor):
        self.editor = editor
        self.app = app

    @abstractmethod
    def click(self):
        pass

class KopierenButton(Button):

    def click(self):
        self.app.setze_kopierten_text(self.editor.get_selection())

class EinfuegenButton(Button):

    def click(self):
        self.editor.enter(self.app.kopierter_text)

class AusschneidenButton(Button):
    def click(self):
        txt = self.editor.get_selection()
        self.editor.enter("")
        self.app.setze_kopierten_text(txt)

# Editor ##################################################
class Editor():

    text:str

    select_begin:int
    select_end:int

    position:int

    def __init__(self):
        self.select_begin = -1
        self.select_end = -1
        self.position = 0
        self.text = ""

    def select(self, a:int, b:int):
        if a < 0 or b < 0:
            print("Eine negative Position kann nicht selektiert werden")
        if a > len(self.text) or b > len(self.text):
            print("Die Selektion darf nicht größer als der Text sein")
        if a > b:
            m = b
            b = a
            a = m
        self.select_begin = a
        self.select_end = b

    def get_selection(self) -> str:
        return self.text[self.select_begin: self.select_end]

    def place_cursor(self, a:int):
        if a < 0:
            print("Der Cursor kann nicht an einer negativen Position sein")
        if a > len(self.text):
            print("Die Cursor-Position kann nicht größer als der Text sein")
        self.position = a
        self.select_begin = -1
        self.select_end = -1

    def enter(self, txt:str) -> str:
        if self.select_begin < 0:
            # Einfügen an Position
            t1 = self.text[0:self.position]
            t2 = self.text[self.position:len(self.text)]
            self.position += len(txt)
            self.text = t1 + txt + t2
        else:
            # Einfügen in Markierung
            t1 = self.text[0:self.select_begin]
            t2 = self.text[self.select_end:len(self.text)]
            self.text = t1 + txt + t2
            self.position = self.select_begin + len(txt)
            self.select_begin = -1
            self.select_end = -1
        return self.text

    def __str__(self) -> str:
        
        if (self.select_begin < 0):
            erg = self.text[0:self.position] + "|" + self.text[self.position:len(self.text)]
        else:
            erg = self.text[0:self.select_begin] + "|" + self.text[self.select_begin:self.select_end] + "|" + self.text[self.select_end:len(self.text)]
        return erg

# App #####################################################
class App():

    kopierter_text:str
    ed:Editor

    def __init__(self, ed:Editor):
        self.ed = ed
        self.kopierter_text = ""
        self.cut_bt = AusschneidenButton(self, ed)
        self.paste = EinfuegenButton(self, ed)
        self.copy = KopierenButton(self, ed)
        self.cut_sc = AusschneidenShortcut(self, ed)
        self.paste_sc = EinfuegenShortcut(self, ed)
        self.copy_sc = KopierenShortcut(self, ed)

    def setze_kopierten_text(self, txt:str):
        self.kopierter_text = txt

    def hit_shortcut(self, sc_text:str):
        sc:Shortcut = None
        if (sc_text == "Copy"):
            sc = self.copy_sc
        elif (sc_text == "Paste"):
            sc = self.paste_sc
        elif (sc_text == "Cut"):
            sc = self.cut_sc
        sc.hit()

    def click_button(self, bt_text:str):
        button:Button = None
        if (bt_text == "Copy"):
            button = self.copy_bt
        elif (bt_text == "Paste"):
            button = self.paste_bt
        elif (bt_text == "Cut"):
            button = self.cut_bt
        
        button.click()

# Main ####################################################
if __name__ == "__main__":
    ed = Editor()
    app = App(ed)
    
    ed.enter("Hallo Seminar")
    print(ed)
    ed.select(6, 13)
    print(ed)
    app.click_button("Cut")
    print(ed)
    ed.enter("Teilnehmer im ")
    print(ed)
    app.hit_shortcut("Paste")
    print(ed)
    ed.enter(" Design Patterns")
    print(ed)