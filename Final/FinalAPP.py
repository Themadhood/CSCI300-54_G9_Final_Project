# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)



class CReadFile:
    def GetLists(self):
        #read input.txt file alow for speshal chars
        #split read in to two stacks with first line =ing 1
        #return the 2 stacks
        pass
        
            
class CRandom:
    def __init__(self,oddlst:list,evenlst:list):
        self.stack_odd = oddlst
        self.stack_even = evenlst

        self.stack_temp = []

    def SetLsts(self,oddlst:list=None,evenlst:list=None):
        """
sets a or both lst to a new lst
"""
        if oddlst != None:
            self.stack_odd = oddlst
        elif evenlst != None:
            self.stack_even = evenlst

    def Selection(self,number:int): #Matthew M#
        #randomly select a movie from bolth stacks
        #add bolth to self.stack_temp
        #determin if number is odd or even
        #take corisponding movie from self.stack_temp
        #return remaing movie to its lst
        #delete the selected movie from its lst
        #return selected movie
        pass

    def UpdateLbl(self):
        #update lable with a movie title
        pass


class CFantasyMovies:
    def __init__(self):
        #get textbox input
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
