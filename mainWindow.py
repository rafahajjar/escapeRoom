import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.window = QWidget()
        self.window.resize(100000, 1000)
        # self.window.move(0, 0)
        self.window.setWindowTitle("Escape Room")
        # window.showFullScreen()

        self.backgroundLabel = QLabel(self.window)
        self.backgroundPixmap = QPixmap('./images/marioBackground.jpg').scaled(1500, 800)
        self.backgroundLabel.setPixmap(self.backgroundPixmap)

        # self.setStyleSheet("QLabel {font: 80pt Comic Sans MS}")
        self.textLabel = QLabel(self.window)
        self.textLabel.setText('<h1><span style="color: red; font-size: 80px">Oh, Hello there! It is me, Mario!&nbsp;</span></h1>')
        self.textLabel.setWordWrap(True)
        self.textLabel.setAlignment(Qt.AlignCenter)
        self.textLabel.move(650, 200)

        self.pictureLabel = QLabel(self.window)
        self.testPixmap = QPixmap('./images/icon.png').scaled(100, 100)
        self.pictureLabel.setPixmap(self.testPixmap)
        self.pictureLabel.move(10, 10)
        self.pictureLabel.resize(100, 100)
        
        self.window.show()
        # self.window.showFullScreen()
        # self.window.showMaximized()



