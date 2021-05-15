from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap

import cv2
import numpy as np


class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                # p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(convertToQtFormat)


class Ui_RealTime(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        [...]
        self.initUI()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.feed.setPixmap(QPixmap.fromImage(image))

    def initUI(self):
        self.resize(700, 700)
        self.setMinimumSize(QtCore.QSize(700, 700))
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.feed = QtWidgets.QLabel(self)
        self.feed.setMinimumSize(QtCore.QSize(680, 680))
        self.feed.setScaledContents(True)
        self.feed.setObjectName("feed")
        self.gridLayout.addWidget(self.feed, 0, 0, 1, 1)

        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        self.show()
