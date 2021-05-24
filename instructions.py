"""Instructions for the game."""
from PyQt5 import QtCore, QtWidgets

html_instructions = """<html>
<head/>
<body>

<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">Basic Instructions</span></h1>
<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">
<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Every square has to contain a single number.</li>
<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Only the numbers from 1 through to 9 can be used.</li>
<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Each 3×3 box can only contain each number from 1 to 9 once.</li>
<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Each vertical column can only contain each number from 1 to 9 once.</li>
<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Each horizontal row can only contain each number from 1 to 9 once.</li>
</ul>

<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">Real-Time Mode</span></h1>
<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">
<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Keep your camera stable for the recognition of the sudoku board.</li>
<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Avoid blurred sudoku board images.</li>
<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Perform in front of a static background.</li>
</ul>

<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">Upload Mode</span></h1>
<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">
<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Avoid blurred sudoku board images.</li>
<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Image processing may take some time.</li>
</ul>

<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">Random Generator Mode</span></h1>
<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">
<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is an interactive mode.</li>
<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Random sudoku will be created that a user can try solving on their own.</li>
<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">There is no time limit for solving sudoku.</li>
<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you think you can\'t solve it, the solution is a click away.</li>
</ul>

</body>
</html>"""


class Ui_Instructions(object):
    def setupUi(self, Instructions):
        Instructions.setObjectName("Instructions")
        Instructions.resize(700, 701)
        Instructions.setMinimumSize(QtCore.QSize(700, 700))
        self.main_layout = QtWidgets.QGridLayout(Instructions)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName("main_layout")

        self.scrollArea = QtWidgets.QScrollArea(Instructions)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 677, 746))
        self.scrollAreaWidgetContents.setStyleSheet("""background-color: rgb(255, 255, 255);
                                                       font: 12pt \"Consolas\";""")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.text_layout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.text_layout.setContentsMargins(10, 10, 10, 10)
        self.text_layout.setSpacing(5)
        self.text_layout.setObjectName("text_layout")

        self.text = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.text.setAlignment(QtCore.Qt.AlignLeading |
                               QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.text.setWordWrap(True)
        self.text.setObjectName("text")
        self.text_layout.addWidget(self.text, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.main_layout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Instructions)
        QtCore.QMetaObject.connectSlotsByName(Instructions)

    def retranslateUi(self, Instructions):
        _translate = QtCore.QCoreApplication.translate
        Instructions.setWindowTitle(_translate("Instructions", "Instructions"))
        self.text.setText(_translate("Instructions", html_instructions))
