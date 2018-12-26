# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\James\Desktop\sec_tal_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from check import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(198, 364)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 160, 290))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # -------------- TERMS --------------
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.terms = getTerms()
        l1 = [*self.terms]
        self.comboBox.addItems(l1)

        # -------------- Subjects --------------
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        self.comboBox_4 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout.addWidget(self.comboBox_4)

        self.subjs = getSubjs()
        l2 = [*self.subjs]
        self.comboBox_4.addItems(l2)

        # -------------- Profs --------------
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout.addWidget(self.comboBox_2)

        self.profs = getProfs()
        l3 = [*self.profs]
        self.comboBox_2.addItems(l3)

        # -------------- CRN --------------
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.verticalLayout.addWidget(self.lineEdit2)

        # -------------- Email --------------
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        # -------------- Email --------------
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 198, 26))
        self.menubar.setObjectName("menubar")
        self.menuSection_Tally = QtWidgets.QMenu(self.menubar)
        self.menuSection_Tally.setObjectName("menuSection_Tally")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSection_Tally.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.submit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Term"))
        self.label_5.setText(_translate("MainWindow", "Subject"))
        self.label_2.setText(_translate("MainWindow", "Professor"))
        self.label_3.setText(_translate("MainWindow", "CRN"))
        self.label_4.setText(_translate("MainWindow", "E-Mail"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.menuSection_Tally.setTitle(_translate("MainWindow", "Tally Checker"))

    def submit(self):
        termSubmit = self.comboBox.currentText()
        term = self.terms.get(termSubmit)

        subjSubmit = self.comboBox_4.currentText()
        subj = self.subjs.get(subjSubmit)

        profSubmit = self.comboBox_2.currentText()
        prof = self.profs.get(profSubmit)

        crnSubmit = self.lineEdit2.text()

        emailSubmit = self.lineEdit.text()

        MainWindow.close()

        runScript(term,subj,prof,crnSubmit, emailSubmit)
  

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
