# This Python file uses the following encoding: utf-8
import sys
import rc_main_resources
from PySide6.QtCore import Qt


from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file     #done!
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
