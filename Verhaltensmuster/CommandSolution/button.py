from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod

class Befehl(ABC):

    def __init__(self, app:App, editor:Editor):
        self.editor = editor
        self.app = app

    @abstractmethod
    def execute(self) -> bool:
        pass

    @abstractmethod
    def undo(self):
        pass

class KopierenBefehl(Befehl):
    
    def execute(self) -> bool:
        # copy to clipboard
        txt = self.editor.get_selection()
        self.app.setze_kopierten_text(txt)
        return False

    def undo(self):
        # Nothing to undo
        pass

class EinfuegenBefehl(Befehl):
    
    def execute(self) -> bool:
        # backup cursor position
        self.backup_pos = self.editor.position
        self.backup_begin = self.editor.select_begin
        self.backup_end = self.editor.select_end
        # paste text from clipboard
        self.editor.enter(self.app.kopierter_text)
        return True
    
    def undo(self):
        # reset text
        length = len(self.app.kopierter_text)
        text = self.editor.text[0:self.editor.position - length] + self.editor.text[self.editor.position:len(self.editor.text) - length]
        self.editor.text = text
        # restore cursor position
        self.editor.select_begin = self.backup_begin
        self.editor.select_end = self.backup_end
        self.editor.position = self.backup_pos
        # remove backups
        self.backup_end = -1
        self.backup_begin = -1

class AusschneidenBefehl(Befehl):

    backup_begin:int
    backup_end:int

    def execute(self) -> bool:
        # backup cursor positions
        self.backup_begin = self.editor.select_begin
        self.backup_end = self.editor.select_end
        # cut logic
        txt = self.editor.get_selection()
        self.editor.enter("")
        # copy to clipboard
        self.app.setze_kopierten_text(txt)
        return True
    
    def undo(self):
        # re-paste text
        self.editor.enter(self.app.kopierter_text)
        # restore cursor positions
        self.editor.select_begin = self.backup_begin
        self.editor.select_end = self.backup_end
        # remove backup
        self.backup_end = -1
        self.backup_begin = -1

# Shortcuts ###############################################
class Shortcut():

    befehl:Befehl
    
    def __init__(self, befehl:Befehl):
        self.befehl = befehl

    def hit(self) -> bool:
        return self.befehl.execute()

# Buttons #################################################
class Button():

    befehl:Befehl

    def __init__(self, befehl:Befehl):
        self.befehl = befehl

    def click(self) -> bool:
        return self.befehl.execute()

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
    history:List[Befehl] = []

    def __init__(self, ed:Editor):
        self.ed = ed
        self.kopierter_text = ""
        self.cut_bt = Button(AusschneidenBefehl(self, ed))
        self.paste_bt = Button(EinfuegenBefehl(self, ed))
        self.copy_bt = Button(KopierenBefehl(self, ed))
        self.cut_sc = Shortcut(AusschneidenBefehl(self, ed))
        self.paste_sc = Shortcut(EinfuegenBefehl(self, ed))
        self.copy_sc = Shortcut(KopierenBefehl(self, ed))

    def setze_kopierten_text(self, txt:str):
        self.kopierter_text = txt

    def hit_shortcut(self, sc_text:str):

        # select correct shortcut
        sc:Shortcut = None
        if (sc_text == "Copy"):
            sc = self.copy_sc
        elif (sc_text == "Paste"):
            sc = self.paste_sc
        elif (sc_text == "Cut"):
            sc = self.cut_sc
        
        # hit shortcut. If it is an undoable shortcut, add it to the history
        if sc is not None and sc.hit():
            self.history.append(sc.befehl)

    def click_button(self, bt_text:str):

        # select correct button
        button = None
        if (bt_text == "Copy"):
            button = self.copy_bt
        elif (bt_text == "Paste"):
            button = self.paste_bt
        elif (bt_text == "Cut"):
            button = self.cut_bt
        
        # click button. If it is an undoable button, add it to the history
        if button is not None and button.click():
            self.history.append(button.befehl)
    
    def undo(self):
        # take last command and run undo
        befehl = self.history.pop()
        if befehl is not None:
            befehl.undo()


if __name__ == "__main__":
    ed = Editor()
    app = App(ed)
    
    ed.enter("Hallo Seminar")
    print(ed)
    ed.select(6, 13)
    print(ed)
    app.click_button("Cut")
    print(ed)
    app.undo()
    print(ed)
    ed.enter("Teilnehmer im ")
    print(ed)
    app.click_button("Paste")
    print(ed)
    app.undo()
    print(ed)
    app.click_button("Paste")
    print(ed)
    ed.enter(" Design Patterns")
    print(ed)