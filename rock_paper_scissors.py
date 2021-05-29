import sys
import random
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QPushButton, QMainWindow, QApplication, QDesktopWidget, QLabel)


class PlayGame(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Rock, Paper, Scissors!"

        self.header = QLabel("Rock, Paper, Scissor", self)
        self.header.setGeometry(20, 10, 280, 60)
        self.header.setAlignment(Qt.AlignCenter)

        self.user_choice = ''
        self.user = QLabel("You", self)
        self.user.setGeometry(50, 100, 70, 70)
        self.user.setStyleSheet("border : 2px solid black; background : white;")
        self.user.setAlignment(Qt.AlignCenter)

        self.computer_choice = ''
        self.computer = QLabel("Computer", self)
        self.computer.setGeometry(200, 100, 70, 70)
        self.computer.setStyleSheet("border : 2px solid black; background : white;")
        self.computer.setAlignment(Qt.AlignCenter)

        self.RockButton = QPushButton('Rock', self)
        self.RockButton.setGeometry(30, 270, 80, 35)

        self.PaperButton = QPushButton('Paper', self)
        self.PaperButton.setGeometry(120, 270, 80, 35)

        self.ScissorsButton = QPushButton('Scissors', self)
        self.ScissorsButton.setGeometry(210, 270, 80, 35)

        self.ResetButton = QPushButton('Reset', self)
        self.ResetButton.setGeometry(100, 320, 120, 50)

        self.result = QLabel(self)
        self.result.setText("Who will it be")
        self.result.setFont(QFont('Times', 10))
        self.result.setGeometry(25, 200, 270, 50)
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setStyleSheet("border : 1px solid black; background : white;")

        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QDesktopWidget().availableGeometry().center()

        self.qtRectangle.moveCenter(self.centerPoint)

        self.gen_computer_choice()
        self.window_launch()

    def window_launch(self):

        """Init the window and the elements within"""
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 320, 400)
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())
        self.RockButton.clicked.connect(self.rock_choice)
        self.PaperButton.clicked.connect(self.paper_choice)
        self.ScissorsButton.clicked.connect(self.scissors_choice)
        self.ResetButton.clicked.connect(self.reset_choice)
        self.show()

    @pyqtSlot()
    def rock_choice(self):
        self.user_choice = 0
        self.user.setText('Rock')
        self.determine_winner()

    @pyqtSlot()
    def paper_choice(self):
        self.user_choice = 1
        self.user.setText('Paper')
        self.determine_winner()

    @pyqtSlot()
    def scissors_choice(self):
        self.user_choice = 2
        self.user.setText('Scissors')
        self.determine_winner()

    @pyqtSlot()
    def reset_choice(self):
        self.result.setText("Who will it be")
        self.user.setText('You')
        self.computer.setText('Computer')
        self.reset_game()

    @pyqtSlot()
    def reset_game(self):
        self.user_choice = ''
        self.computer_choice = ''
        self.RockButton.setEnabled(True)
        self.PaperButton.setEnabled(True)
        self.ScissorsButton.setEnabled(True)
        self.gen_computer_choice()

    def gen_computer_choice(self):

        self.computer_choice = random.randint(0, 2)

    def populate_computer_choice(self):

        if self.computer_choice == 0:
            self.computer.setText('Rock')
        elif self.computer_choice == 1:
            self.computer.setText('Paper')
        else:
            self.computer.setText('Scissors')

    def determine_winner(self):

        self.populate_computer_choice()
        winner_value = ((self.user_choice + -self.computer_choice) % 3)
        print(winner_value)
        if winner_value == 0:
            self.result.setText("Draw!")
            self.reset_game()
        elif winner_value == 1:
            self.result.setText("You win!")
            self.reset_game()
        else:
            self.result.setText("Computer won you loser!")
            self.reset_game()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = PlayGame()
    sys.exit(app.exec_())
