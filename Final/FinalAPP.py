# This Python file uses the following encoding: utf-8
import sys, io
import rc_main_resources
import random
random.seed()


from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class CFantasyMovies:
    def __init__(self,lbl):
        self._lbl = lbl
    def printMovie(self,txt):
        self._lbl.setText(txt)




class CReadFile:
    def _Read(self):
        retar = ""
        with io.open('input.txt', 'r', encoding='utf-8') as movies:
            retar = movies.read()
            movies.close()
        retar = retar.split("\n")
        return retar

    def _Split(self,movies:list):
        for i in range(0,len(movies)):
            if (i+1)%2 == 1:
                self.stack_odd.append(movies[i])
            else:
                self.stack_even.append(movies[i])

    def GetLists(self):
        self.stack_odd = []
        self.stack_even = []

        movies = self._Read()
        self._Split(movies)
        
        return self.stack_odd,self.stack_even




class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        # Set window flags to remove the title bar and frame
        self.setWindowFlags(Qt.FramelessWindowHint)


        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Connect the clicked signal to the slot
        self.ui.exit_button.clicked.connect(self.close_application)

        # Connect the 'clicked' signal of the ok_button to the slot
        self.ui.ok_button.clicked.connect(self.on_ok_button_clicked)

        self.Print = CFantasyMovies(lbl = self.ui.movieNameLabel)
        self.ClassReed = CReadFile()
        self.RandSelect = CRandom()

        self.Read()

    def close_application(self):
         # This slot will be called when the button is clicked
        self.close()  # This will close the application window

    def on_ok_button_clicked(self):
        # This method will be called every time the OK button is clicked
        # Insert the functionality you want here
        user_input = self.ui.userNum.text()  # Assuming userNum is your QLineEdit

        # You can now use the input to do something, like showing a movie name
        # For example, if you have a method that gets a movie name based on a number
        movie_name = self.get_movie_name_from_number(user_input)
        self.Print.printMovie(txt = movie_name)  # Assuming movieNameLabel is your QLabel

    def get_movie_name_from_number(self, number):
        try:
            number = int(number)
            return self.RandSelect.Selection(number = number)
        except:
            return "please enter a number"

    def Read(self):
        odd,even = self.ClassReed.GetLists()
        self.RandSelect.SetLsts(oddlst=odd, evenlst=even)

        
            
class CRandom:
    def __init__(self):
        self.stack_odd = []
        self.stack_even = []

        self.stack_temp = []

    def SetLsts(self,oddlst:list=None,evenlst:list=None):
        """
sets a or both lst to a new lst
"""
        if oddlst != None:
            self.stack_odd = oddlst
        if evenlst != None:
            self.stack_even = evenlst

    def _PickRandom(self):
        if self.stack_odd > []:
            odd = random.choice(self.stack_odd)
            self.stack_temp.append(odd)
            self.stack_odd.remove(odd)
        if self.stack_even > []:
            even = random.choice(self.stack_even)
            self.stack_temp.append(even)
            self.stack_even.remove(even)

    def Selection(self,number:int):
        self._PickRandom()

        if len(self.stack_temp) > 1: #if mor than one movie in lst
            if number%2 == 1: #odd number
                retar = self.stack_temp.pop(0)
                self.stack_even.append(self.stack_temp.pop())
            else: #even
                retar = self.stack_temp.pop()
                self.stack_odd.append(self.stack_temp.pop())

        elif len(self.stack_temp) == 1:
            retar = self.stack_temp.pop()
        else:
            retar = "no other available films"

        return retar


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
