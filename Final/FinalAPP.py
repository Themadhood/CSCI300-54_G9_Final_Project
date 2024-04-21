# This Python file uses the following encoding: utf-8
import sys, io
import rc_main_resources
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
       return self.RandSelect.Selection(number = number)

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
        {
            from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_finalProject import Ui_finalProject
import sys

class finalProject(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_finalProject()
        self.ui.setupUi(self)
        
        self.ui.movieButton.clicked.connect(self.on_movieButton_clicked)
        
    def on_movieButton_clicked(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = finalProject()
    window.show()
    sys.exit(app.exec_())


}

{
    from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.uic import loadUi
import random

class finalProject(QMainWindow):
    def __init__(self, parent=None):
        super(finalProject, self).__init__(parent)
        self.ui = loadUi("finalproject.ui", self)

        self.even_movies = []
        self.odd_movies = []
        self.temp_stack = []

    def __del__(self):
        del self.ui

    def shuffle_stack(self, stack):
        temp_list = stack.copy()
        random.shuffle(temp_list)
        stack.clear()
        stack.extend(temp_list)

    def on_movieButton_clicked(self):
        # Initialize the lists with movie names
        self.even_movies = ["Ice Age 5: Collision Course", "Forbidden Empire", "X-Men: Days of Future Past", "The Mortal Instruments: City of Bones", "Melancholia"]
        self.odd_movies = ["DC's Legends of Tomorrow", "Miss Peregrine's Home for Perculiar Children", "The Zero Theorem", "Jupiter Ascending", "The Age of Adaline"]

        self.shuffle_stack(self.odd_movies)
        self.shuffle_stack(self.even_movies)

        self.temp_stack.append(self.odd_movies.pop())
        self.temp_stack.append(self.even_movies.pop())

        if int(self.ui.movieNumber.text()) % 2 == 0:
            self.ui.movieResult.setText(self.temp_stack.pop())
            self.odd_movies.append(self.temp_stack.pop())
        else:
            self.even_movies.append(self.temp_stack.pop())
            self.ui.movieResult.setText(self.temp_stack.pop())

}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
