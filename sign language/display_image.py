import sys
from voice_recognition import recognition, generate_image
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.Qt import QEventLoop, QTimer

sub = recognition()

image_list = generate_image(sub)

class App(QWidget):

    def __init__(self):

        super().__init__()

        self.title = 'Signal Language'

        self.left = 650
        self.top = 100
        self.width = 700
        self.height = 700

        self.initUI()
    
    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.subtitle = QLabel(sub, self)
        self.subtitle.setFont(QFont('Times',18))
        self.subtitle.move(20,800)
        self.resize(300,50)

        label = QLabel(self)

        for image in image_list:

            loop = QEventLoop()
            QTimer.singleShot(1000, loop.quit)
            loop.exec_()

            pixmap = QPixmap('sign-language/{}'.format(image))
            label.setPixmap(pixmap)
            self.resize(pixmap.width(),pixmap.height()+100)
                    
            self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
