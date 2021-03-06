from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.painter = QtGui.QPainter(self)
        self.painter.setPen(QtCore.Qt.white)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.update()

    def createAndDrawCircle(self, xPos, yPos, x, y, text, colorR, colorG, colorB):
        color = QtGui.QColor(colorR, colorG, colorB)
        qRect = QtCore.QRect(xPos, yPos, x ,y)
        qCorcleRect = QtCore.QRect(xPos, yPos, x , y)
        circleSize = 50
        center = QtCore.QPoint(xPos + circleSize/2, yPos + circleSize/2)
        self.painter.setBrush(color)
        self.painter.drawEllipse(qRect)
        self.painter.setBrush(QtCore.Qt.white)
        self.painter.drawText(center, text)
    
    def createAndDrawLine(self, xPos, yPos):
        pen = QtGui.QPen(QtCore.Qt.black)
        self.painter.setPen(pen)
        self.painter.drawLine(xPos, yPos, 10, 200)

    def paintEvent(self, event):
        self.painter = QtGui.QPainter(self)
        self.painter.setPen(QtCore.Qt.black)
        self.painter.begin(self)
        self.createAndDrawLine(10, 100)
        self.createAndDrawCircle(10, 50, 30, 40, "A", 255, 0 , 0)
        self.painter.end()

if __name__ == "__main__":
    app = QtWidgets.QApplication(["app"])
    mainScreen = MainWindow()
    mainScreen.show()
    app.exec()

