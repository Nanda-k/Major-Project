# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Sentiment2019\adminhome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from RFTrain import RFTrain
from SVMTrain import SVMTrain
from NBTrain import NBTrain

import time
import pandas as pd
import sys
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from RandomForest import RandomForest
from NB import NB
from SVM import SVM
from AccuracyStore import AccuracyStore
from F1Store import F1Store
from Graphs import view
from Graphs2 import f1view


class AdminHome(object):

    def browsefile(self):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File",
                                                                "D://",
                                                                "*.csv")
            print(fileName)
            self.trainfile.setText(fileName)
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)
    def browsefile2(self):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File",
                                                                "D://",
                                                                "*.csv")
            print(fileName)
            self.trainfile_2.setText(fileName)
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)



    def model_assessment(y_test, predicted_class):
        # Accuracy = (TP + TN) / ALL
        accuracy = accuracy_score(y_test, predicted_class)
        f1=f1_score(y_test, predicted_class,average='weighted')
        #f1=0
        print('F1_Score',f1)
        return [accuracy,f1]


    def deftesting(self):
        setacc = []
        setf1 = []
        self.showAlertBox("Classification", "Implementing Random Forest")
        self.testname.setText("Random Forest")
        self.testingtime.setText("")
        self.accuracy.setText("")
        self.f1score.setText("")

        testfile = self.trainfile_2.text()
        start = time.time()
        l = RandomForest.detecting(testfile)
        end = time.time()
        t = (end - start)

        self.testingtime.setText(str(round(t)) + " (sec)")
        test_file = pd.read_csv(testfile)
        res = AdminHome.model_assessment(test_file['sentiment'], l)
        print('accuracy', res[0])
        print('f1', res[1])
        setacc.append(res[0])
        setf1.append(res[1])
        self.accuracy.setText(str(res[0]))
        self.f1score.setText(str(res[1]))

        self.progressBar.setProperty("value", 33)

        time.sleep(6.0)

        self.showAlertBox("Classification", "Implementing Naive Bayes")

        self.testname.setText("Naive Bayes")
        self.testingtime.setText("")
        self.accuracy.setText("")
        self.f1score.setText("")

        testfile = self.trainfile_2.text()
        start = time.time()
        l = NB.detecting(testfile)
        end = time.time()
        t = (end - start)
        self.testingtime.setText(str(round(t)) + " (sec)")
        res = AdminHome.model_assessment(test_file['sentiment'], l)
        print('accuracy', res[0])
        print('f1', res[1])

        setacc.append(res[0])
        setf1.append(res[1])
        self.accuracy.setText(str(res[0]))
        self.f1score.setText(str(res[1]))
        self.progressBar.setProperty("value", 67)
        time.sleep(6.0)
        self.showAlertBox("Classification", "Implementing Support Vector Machine")
        self.testname.setText("SVM")
        self.testingtime.setText("")
        self.accuracy.setText("")
        self.f1score.setText("")

        testfile = self.trainfile_2.text()
        start = time.time()
        l = SVM.detecting(testfile)
        end = time.time()
        t = (end - start)

        self.testingtime.setText(str(round(t)) + " (sec)")

        res = AdminHome.model_assessment(test_file['sentiment'], l)
        print('accuracy', res[0])
        print('f1', res[1])
        setacc.append(res[0])
        setf1.append(res[1])

        self.accuracy.setText(str(res[0]))
        self.f1score.setText(str(res[1]))

        self.progressBar.setProperty("value", 100)
        self.showAlertBox("Classification", "Completed !!")
        print(setacc)
        print(setf1)
        AccuracyStore.store(setacc[0], setacc[1], setacc[2])
        F1Store.store(setf1[0], setf1[1], setf1[2])




    def rftrain(self):
        try:
            self.trainname.setText("Random Forest")
            self.traintime.setText("")
            self.trainstatus.setText("")

        
            file=self.trainfile.text()
            start = time.time()
            rf=RFTrain()
            rf.detecting(file)
            end = time.time()
            t=(end - start)
            self.traintime.setText(str(round(t))+" (sec)")
            self.trainstatus.setText("Model Saved")


        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def nbtrain(self):
        try:
            self.trainname.setText("Naive Bayes")
            self.traintime.setText("")
            self.trainstatus.setText("")

        
            file=self.trainfile.text()
            start = time.time()
            rf=NBTrain()
            rf.detecting(file)
            end = time.time()
            t=(end - start)
            self.traintime.setText(str(round(t))+" (sec)")
            self.trainstatus.setText("Model Saved")


        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def svmtrain(self):
        try:
            self.trainname.setText("Support Vector Machine")
            self.traintime.setText("")
            self.trainstatus.setText("")

        
            file=self.trainfile.text()
            start = time.time()
            rf=SVMTrain()
            rf.detecting(file)
            end = time.time()
            t=(end - start)
            self.traintime.setText(str(round(t))+" (sec)")
            self.trainstatus.setText("Model Saved")


        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def accuracyview(self):
        view()
    def f1view(self):
        f1view()

    def showAlertBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, box):
        box.setObjectName("box")
        box.resize(899, 610)
        box.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(box)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 891, 640))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.frame = QtWidgets.QFrame(self.Home)
        self.frame.setGeometry(QtCore.QRect(0, 0, 901, 591))
        self.frame.setStyleSheet("background-image: url(wall.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.Home, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 891, 581))
        self.tableView.setStyleSheet("background-image: url(bg.jpg);")
        self.tableView.setObjectName("tableView")
        self.trainrf = QtWidgets.QPushButton(self.tab_2)
        self.trainrf.setGeometry(QtCore.QRect(40, 250, 380, 30))
        self.trainrf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.trainrf.setObjectName("trainrf")

        #-----------------------------------
        self.trainrf.clicked.connect(self.rftrain)
        #-----------------------------------



        self.trainsvm = QtWidgets.QPushButton(self.tab_2)
        self.trainsvm.setGeometry(QtCore.QRect(40, 330, 380, 30))
        self.trainsvm.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.trainsvm.setObjectName("trainsvm")

        #--------------------------------   
        self.trainsvm.clicked.connect(self.svmtrain)
        #--------------------------------   

        self.browse = QtWidgets.QToolButton(self.tab_2)
        self.browse.setGeometry(QtCore.QRect(380, 200, 40, 30))
        self.browse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browse.setObjectName("browse")

        #------------------------
        self.browse.clicked.connect(self.browsefile)
        #------------------------




        self.trainnb = QtWidgets.QPushButton(self.tab_2)
        self.trainnb.setGeometry(QtCore.QRect(40, 290, 380, 30))
        self.trainnb.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.trainnb.setObjectName("trainnb")

        #---------------------
        self.trainnb.clicked.connect(self.nbtrain)
        #---------------------

        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(40, 150, 261, 30))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS PGothic\";")
        self.label.setObjectName("label")
        self.trainfile = QtWidgets.QLineEdit(self.tab_2)
        self.trainfile.setGeometry(QtCore.QRect(40, 200, 330, 30))
        self.trainfile.setObjectName("trainfile")





        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(500, 220, 140, 40))
        self.label_2.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(500, 260, 140, 40))
        self.label_3.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(500, 300, 140, 40))
        self.label_4.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.label_4.setObjectName("label_4")
        self.trainname = QtWidgets.QLabel(self.tab_2)
        self.trainname.setGeometry(QtCore.QRect(660, 220, 210, 40))
        self.trainname.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.trainname.setObjectName("trainname")
        self.traintime = QtWidgets.QLabel(self.tab_2)
        self.traintime.setGeometry(QtCore.QRect(660, 260, 210, 40))
        self.traintime.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.traintime.setObjectName("traintime")
        self.trainstatus = QtWidgets.QLabel(self.tab_2)
        self.trainstatus.setGeometry(QtCore.QRect(660, 300, 210, 40))
        self.trainstatus.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.trainstatus.setObjectName("trainstatus")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView_2 = QtWidgets.QTableView(self.tab)
        self.tableView_2.setGeometry(QtCore.QRect(0, 0, 891, 571))
        self.tableView_2.setStyleSheet("background-image: url(bg.jpg);")
        self.tableView_2.setObjectName("tableView_2")
        self.accuracy = QtWidgets.QLabel(self.tab)
        self.accuracy.setGeometry(QtCore.QRect(660, 300, 210, 40))
        self.accuracy.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.accuracy.setObjectName("accuracy")
        self.testing = QtWidgets.QPushButton(self.tab)
        self.testing.setGeometry(QtCore.QRect(40, 250, 380, 30))
        self.testing.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.testing.setObjectName("testing")

        #------------------------   
        self.testing.clicked.connect(self.deftesting)
        #------------------------

        self.trainfile_2 = QtWidgets.QLineEdit(self.tab)
        self.trainfile_2.setGeometry(QtCore.QRect(40, 200, 330, 30))
        self.trainfile_2.setObjectName("trainfile_2")
        self.browse_2 = QtWidgets.QToolButton(self.tab)
        self.browse_2.setGeometry(QtCore.QRect(380, 200, 40, 30))
        self.browse_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browse_2.setObjectName("browse_2")
        
        #-----------------------------
        self.browse_2.clicked.connect(self.browsefile2)
        #-----------------------------

        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(500, 260, 140, 40))
        self.label_5.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.label_5.setObjectName("label_5")
        self.testingtime = QtWidgets.QLabel(self.tab)
        self.testingtime.setGeometry(QtCore.QRect(660, 260, 210, 40))
        self.testingtime.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.testingtime.setObjectName("testingtime")
        self.testname = QtWidgets.QLabel(self.tab)
        self.testname.setGeometry(QtCore.QRect(660, 220, 210, 40))
        self.testname.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.testname.setObjectName("testname")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(500, 220, 140, 40))
        self.label_6.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(500, 300, 140, 40))
        self.label_7.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(40, 150, 261, 30))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS PGothic\";")
        self.label_8.setObjectName("label_8")
        self.f1score = QtWidgets.QLabel(self.tab)
        self.f1score.setGeometry(QtCore.QRect(660, 340, 210, 40))
        self.f1score.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.f1score.setObjectName("f1score")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(500, 340, 140, 40))
        self.label_9.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.label_9.setObjectName("label_9")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(40, 310, 420, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.buttonaccuracy = QtWidgets.QPushButton(self.tab)
        self.buttonaccuracy.setGeometry(QtCore.QRect(40, 420, 180, 30))
        self.buttonaccuracy.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"FangSong\";")
        self.buttonaccuracy.setObjectName("buttonaccuracy")


        self.buttonaccuracy.clicked.connect(self.accuracyview)

        self.buttonf1 = QtWidgets.QPushButton(self.tab)
        self.buttonf1.setGeometry(QtCore.QRect(240, 420, 180, 30))
        self.buttonf1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"FangSong\";")
        self.buttonf1.setObjectName("buttonf1")
        self.buttonf1.clicked.connect(self.f1view)
        self.tabWidget.addTab(self.tab, "")
        box.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(box)
        self.statusbar.setObjectName("statusbar")
        box.setStatusBar(self.statusbar)

        self.retranslateUi(box)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(box)

    def retranslateUi(self, box):
        _translate = QtCore.QCoreApplication.translate
        box.setWindowTitle(_translate("box", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("box", "Home"))
        self.trainrf.setText(_translate("box", "Random Forest"))
        self.trainsvm.setText(_translate("box", "Support Vector Machine"))
        self.browse.setText(_translate("box", "..."))
        self.trainnb.setText(_translate("box", "Naive Bayes"))
        self.label.setText(_translate("box", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Training Dataset </span></p></body></html>"))
        self.trainfile.setPlaceholderText(_translate("box", "Upload Training File"))
        self.label_2.setText(_translate("box", "Algorithm:"))
        self.label_3.setText(_translate("box", "Process Time:"))
        self.label_4.setText(_translate("box", "Status:"))
        self.trainname.setText(_translate("box", "non"))
        self.traintime.setText(_translate("box", "non"))
        self.trainstatus.setText(_translate("box", "non"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("box", "Training Classifications"))
        self.accuracy.setText(_translate("box", "non"))
        self.testing.setText(_translate("box", "Testing with Classifications"))
        self.trainfile_2.setPlaceholderText(_translate("box", "Upload Training File"))
        self.browse_2.setText(_translate("box", "..."))
        self.label_5.setText(_translate("box", "Process Time:"))
        self.testingtime.setText(_translate("box", "non"))
        self.testname.setText(_translate("box", "non"))
        self.label_6.setText(_translate("box", "Algorithm:"))
        self.label_7.setText(_translate("box", "Accuracy:"))
        self.label_8.setText(_translate("box", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Testing</span></p></body></html>"))
        self.f1score.setText(_translate("box", "non"))
        self.label_9.setText(_translate("box", "F1 Score"))
        self.buttonaccuracy.setText(_translate("box", "Accuracy Graph"))
        self.buttonf1.setText(_translate("box", "F1-Score Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("box", "Testing"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    box = QtWidgets.QMainWindow()
    ui = AdminHome()
    ui.setupUi(box)
    box.show()
    sys.exit(app.exec_())
