# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Sentiment2019\userhome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,tweepy,re
from NBTest import NB
from Graphs3 import viewg
from Freq import CountFrequency

class UserHome(object):

    def __init__(self):
        self.tweetset = []
        self.pclasses=[]


    def get(self):

        try:
            kwd = self.keywords.text()

            nts = 20
            consumerKey = '7zN6WvASiB5jZV2cFKQU5oR0F'
            consumerSecret = 'bKxoxxhEUMx6bk3HPcBf5sXvUf7zJfnisj2V9ObY2aDRIr6be9'
            accessToken = '1100727463011864577-vys9YeHGpK6GK2ihT5ITAC4fe5vShI'
            accessTokenSecret = '3ZJ5qF02SKG1dUL1G2M6uy7dbRIWfkd4QbLLwQ38Y4RMU'
            auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
            auth.set_access_token(accessToken, accessTokenSecret)
            api = tweepy.API(auth)
            # input for term to be searched and how many tweets to search
            searchTerm =kwd
            NoOfTerms =int(nts)

            # searching for tweets
            self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang="en").items(NoOfTerms)
            #print(self.tweets)

            self.tweetset=[]

            for tweet in self.tweets:
                self.tweetset.append(tweet.text)




            item = QtWidgets.QListWidgetItem()
            self.listWidget.clear()
            for i in self.tweetset:
                self.listWidget.addItem(i)
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def sentiprediction(self):
        try:
            tweets=self.tweetset
            self.pclasses=NB.detecting(tweets)
            print(self.pclasses)
            item = QtWidgets.QListWidgetItem()
            self.listWidget.clear()
            s=len(tweets)
            for i in range(s):
                st=""+str(self.pclasses[i])+"   |   "+str(tweets[i]);
                self.listWidget.addItem(st)





        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def view(self):
        try:
            g1=CountFrequency(self.pclasses)
            viewg(g1)







        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)







    def setupUi(self, box):
        box.setObjectName("box")
        box.resize(888, 530)
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
        self.frame.setStyleSheet("background-image: url(twitter-analytics-fade-ss-1920.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.Home, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 891, 581))
        self.tableView.setStyleSheet("background-image: url(wall2.jpg);")
        self.tableView.setObjectName("tableView")
        self.gettweets = QtWidgets.QPushButton(self.tab_2)
        self.gettweets.setGeometry(QtCore.QRect(80, 260, 310, 30))
        self.gettweets.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.gettweets.setObjectName("gettweets")

        #-----------------------
        self.gettweets.clicked.connect(self.get)
        #-----------------------




        self.graph = QtWidgets.QPushButton(self.tab_2)
        self.graph.setGeometry(QtCore.QRect(110, 360, 260, 30))
        self.graph.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.graph.setObjectName("graph")
        #-----------------------
        self.graph.clicked.connect(self.view)
        #-----------------------

        self.prediction = QtWidgets.QPushButton(self.tab_2)
        self.prediction.setGeometry(QtCore.QRect(80, 300, 310, 30))
        self.prediction.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.prediction.setObjectName("prediction")

        #-----------------------
        self.prediction.clicked.connect(self.sentiprediction)
        #-----------------------

        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(50, 147, 370, 30))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS PGothic\";")
        self.label.setObjectName("label")
        self.keywords = QtWidgets.QLineEdit(self.tab_2)
        self.keywords.setGeometry(QtCore.QRect(40, 210, 380, 30))
        self.keywords.setObjectName("keywords")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(50, 177, 350, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(70, 187, 310, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setGeometry(QtCore.QRect(50, 140, 350, 10))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.tab_2)
        self.line_4.setGeometry(QtCore.QRect(490, 560, 350, 10))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.tab_2)
        self.line_5.setGeometry(QtCore.QRect(70, 130, 310, 10))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(460, 130, 380, 300))
        self.listWidget.setStyleSheet("font: 12pt \"MV Boli\";\n"
"color: rgb(40, 103, 170);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.tabWidget.addTab(self.tab_2, "")
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
        self.gettweets.setText(_translate("box", "Get Tweets"))
        self.graph.setText(_translate("box", "View Graph"))
        self.prediction.setText(_translate("box", "Sentiment Analysis"))
        self.label.setText(_translate("box", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Search Tweets and Sentiment Analysis</span></p></body></html>"))
        self.keywords.setPlaceholderText(_translate("box", "Enter Topic words or HashTags"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        #item = self.listWidget.item(0)
        #item.setText(_translate("box", "sajid"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("box", "Training Classifications"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    box = QtWidgets.QMainWindow()
    ui = UserHome()
    ui.setupUi(box)
    box.show()
    sys.exit(app.exec_())
