from PyQt5 import QtCore, QtGui, QtWidgets

ik_text = """<h2>Ishani Kathuria</h2>
             <h3><a href=\"https://www.linkedin.com/in/ishani-kathuria/\">LinkedIn</a></h3>
             <h3><a href=\"https://github.com/ikathuria\">GitHub</a></h3>"""

ks_text = """<h2>Kamad Saxena</h2>
             <h3><a href=\"https://www.linkedin.com/in/kamad-saxena/\">LinkedIn</a></h3>
             <h3><a href=\"https://github.com/kamad11\">GitHub</a></h3>"""


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(700, 700)
        About.setMinimumSize(QtCore.QSize(700, 700))
        About.setStyleSheet("""background-color: rgb(255, 255, 255);
                               font: 12pt \"Consolas\";""")
        self.main_layout = QtWidgets.QGridLayout(About)
        self.main_layout.setObjectName("main_layout")
        
        self.logo = QtWidgets.QLabel(About)
        self.logo.setMinimumSize(QtCore.QSize(300, 300))
        self.logo.setPixmap(QtGui.QPixmap("Resources\logo_transparent.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.main_layout.addWidget(self.logo, 0, 0, 1, 3)

        self.authors = QtWidgets.QLabel(About)
        self.authors.setAlignment(QtCore.Qt.AlignCenter)
        self.authors.setObjectName("authors")
        self.main_layout.addWidget(self.authors, 1, 1, 1, 1)
        
        self.IK = QtWidgets.QLabel(About)
        self.IK.setMinimumSize(QtCore.QSize(210, 210))
        self.IK.setAlignment(QtCore.Qt.AlignCenter)
        self.IK.setObjectName("IK")
        self.main_layout.addWidget(self.IK, 1, 0, 1, 1)

        self.KS = QtWidgets.QLabel(About)
        self.KS.setMinimumSize(QtCore.QSize(210, 210))
        self.KS.setAlignment(QtCore.Qt.AlignCenter)
        self.KS.setObjectName("KS")
        self.main_layout.addWidget(self.KS, 1, 2, 1, 1)

        self.repo = QtWidgets.QLabel(About)
        self.repo.setAlignment(QtCore.Qt.AlignCenter)
        self.repo.setObjectName("repo")
        self.main_layout.addWidget(self.repo, 2, 0, 1, 3)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))

        self.authors.setText(_translate("About", "<h1>Authors</h1>"))

        self.IK.setText(_translate("About", ik_text))

        self.KS.setText(_translate("About", ks_text))

        self.repo.setText(_translate(
            "About", "<h4>The Project: <a href=\"https://github.com/Kamad11/Smart_Sudoku\">https://github.com/Kamad11/Smart_Sudoku</a><h4>"))
