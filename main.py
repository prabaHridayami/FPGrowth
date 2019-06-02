# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import time
import matplotlib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pyfpgrowth import pyfpgrowth

import fp


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 91, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 140, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 0, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 210, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 100, 61, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(520, 100, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 91, 16))
        self.label_5.setObjectName("label_5")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 210, 421, 141))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 419, 139))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_6 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 419, 139))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 960, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 370, 91, 16))
        self.label_9.setObjectName("label_9")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(30, 400, 421, 141))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 419, 139))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_8 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 419, 139))
        self.label_8.setObjectName("label_8")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 140, 421, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "File Input Name"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "FP-GROWTH"))
        self.pushButton_2.setText(_translate("MainWindow", "Process"))
        self.label_4.setText(_translate("MainWindow", "Min.Support"))
        self.label_5.setText(_translate("MainWindow", "Frequent Itemset"))
        # self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "Frequent Itemset"))
        self.label_9.setText(_translate("MainWindow", "Confidence"))
        self.label_8.setText(_translate("MainWindow", ""))
        self.FINAL_RESULT = ''
        self.pushButton.clicked.connect(self.loadPath)
        self.pushButton_2.clicked.connect(self.fpgrowth)

    def loadPath(self):
        file_path = QFileDialog.getOpenFileName()
        self.filename = str(file_path[0])
        self.textEdit_2.setText(str(file_path[0]))

    def fpgrowth(self):
        self.label_6.setText("")
        min_Support = self.spinBox.value()
        initSet = ''
        initSet = fp.create_initialset(fp.Load_data(self.filename))
        start = time.time()
        FPtree, HeaderTable = fp.create_FPTree(initSet, min_Support)

        frequent_itemset = []
        # call function to mine all ferquent itemsets
        # print(fp.Mine_Tree(FPtree, HeaderTable, min_Support, set([]), frequent_itemset))
        end = time.time()

        FPtree.disp()

        patterns = pyfpgrowth.find_frequent_patterns(fp.Load_data(self.filename), min_Support)
        all_pattern = pyfpgrowth.find_frequent_patterns(fp.Load_data(self.filename), 0)


        for the_key, the_value in patterns.items():
            self.label_6.append(str(the_key)+ ' corresponds to '+ str(the_value))

        self.label_8.setText(str(len(patterns)/len(all_pattern)))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

