import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Pepe Dame: The Game!'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel(self)
        pixmap = QPixmap('interface.jpg')
        label.setPixmap(pixmap)
            

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        startMenu = mainMenu.addMenu('Start')
        helpMenu = mainMenu.addMenu('Help')

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        NewGameButton = QAction(QIcon('NewGame24.png'), 'New Game', self)
        NewGameButton.setShortcut('Ctrl+N')
        NewGameButton.setStatusTip('Open a New Game')
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        AboutButton = QAction(QIcon('AboutButton24.png'), 'About Game', self)
        HelpButton = QAction(QIcon('HelpButton24, png'), 'Help', self)
        HelpButton.setShortcut('F1')
        fileMenu.addAction(exitButton)
        startMenu.addAction(NewGameButton)
        helpMenu.addAction(AboutButton)
        helpMenu.addAction(HelpButton)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
sys.exit(app.exec_())
