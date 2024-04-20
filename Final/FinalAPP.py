# This Python file uses the following encoding: utf-8
import sys, io

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

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
        self.ui.movieNameLabel.setText(movie_name)  # Assuming movieNameLabel is your QLabel

    def get_movie_name_from_number(self, number):
       pass



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

{
    #ifndef FINALPROJECT_H
#define FINALPROJECT_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class finalProject;
}
QT_END_NAMESPACE

class finalProject : public QMainWindow
{
    Q_OBJECT

public:
    finalProject(QWidget *parent = nullptr);
    ~finalProject();

private slots:
    void on_movieButton_clicked();

private:
    Ui::finalProject *ui;
};
#endif // FINALPROJECT_H
                
}

{
    #include "finalproject.h"
#include "ui_finalproject.h"

finalProject::finalProject(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::finalProject)
{
    ui->setupUi(this);
}

finalProject::~finalProject()
{
    delete ui;
}



QString movieName;

#include <QStack>
#include <QRandomGenerator>

QStack<QString>  evenMovies;
QStack<QString> oddMovies;
QStack<QString> tempStack;


void shuffleStack(QStack<QString> &stack) {
    QList<QString> tempList;
    while (!stack.isEmpty()) {
        tempList.append(stack.pop());
    }
    std::shuffle(tempList.begin(), tempList.end(), std::default_random_engine(std::random_device{}()));
    for (const QString &movie : tempList) {
        stack.push(movie);
    }
}


void finalProject::on_movieButton_clicked()
{
    // Initialize the stacks with movie names
    evenMovies.push("Ice Age 5: Collision Course");
    evenMovies.push("Forbidden Empire");
    evenMovies.push("X-Men: Days of Future Past");
    evenMovies.push("The Mortal Instruments: City of Bones");
    evenMovies.push("Melancholia");

    oddMovies.push("DC's Legends of Tomorrow");
    oddMovies.push("Miss Peregrine's Home for Perculiar Children");
    oddMovies.push("The Zero Theorem");
    oddMovies.push("Jupiter Ascending");
    oddMovies.push("The Age of Adaline");

    shuffleStack(oddMovies);

    shuffleStack(evenMovies);

    tempStack.push(oddMovies.pop());
    tempStack.push(evenMovies.pop());

    if((ui->movieNumber->text().toInt()) % 2 == 0)
    {
        movieName = tempStack.pop();
        oddMovies.push(tempStack.pop());
    }
    else
    {
        evenMovies.push(tempStack.pop());
        movieName = tempStack.pop();
    }

    ui->movieResult->setText(movieName);

}

}

class CFantasyMovies:
    def __init__(self,lbl):
        self._lbl = lbl
    def printMovie(self,txt):
        self._lbl.setText(txt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
