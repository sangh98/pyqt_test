import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
FILE = 10
curType=""
curNum=""

form_class = uic.loadUiType("fiqt.ui")[0]
form_second = uic.loadUiType("seqt.ui")[0]
form_question = uic.loadUiType("question.ui")[0]

class mainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        type = ["입출력", "조건문", "반복문", "배열", "문자열"]
        for i in type:
            self.listWidget.addItem(i)
        self.listWidget.clicked.connect(self.typeClicked)

    def showMain(self):
        self.show()
    def typeClicked(self):
        global curType
        curType = str(self.listWidget.currentRow()+1).zfill(2)
        print(curType)
        self.second = secondWindow()
        self.close()
        self.second.show()#창 띄움

class secondWindow(QMainWindow, form_second):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        num =[]
        for i in range(1, FILE+1):
            num.append(str(i).zfill(2)+"번")
        for i in num:
            self.listNum.addItem(i)
        self.listNum.clicked.connect(self.numClicked)
        self.backBtn.clicked.connect(self.backClicked)

    def numClicked(self):
        global curNum
        curNum = self.listNum.currentItem().text()[0:2]
        print(f"txt/test{curType.zfill(2)}{curNum.zfill(2)}.txt")
        self.qw = questionWindow()
        self.qw.show()

    def backClicked(self):
        self.close()
        self.showMain = mainWindow.showMain()
        self.showMain

    """
    def numClicked(self):
        global txtdata
        for i in range(1, FILE+1):
            if self.listNum.currentItem().text()[0] == str(i):
                f = open(f"txt/test{str(i)}.txt", encoding="UTF8")
                txtdata = f.read()
        self.qw = questionWindow()
        self.qw.show()
    """
    """
    def numClicked(self):
        global txtdata
        match self.listNum.currentItem().text():
            case "1번":
                f = open('txt/test1.txt', encoding="UTF8")
                txtdata = f.read()
            case "2번":
                f = open('txt/test2.txt', encoding="UTF8")
                txtdata = f.read()
            case "3번":
                f = open('txt/test3.txt', encoding="UTF8")
                txtdata = f.read()               
        self.qw = questionWindow()
        self.qw.show()
    """
    """
    def numClicked(self):
        if(self.listNum.currentItem().text() == "1번"):
            f = open('txt/test1.txt', encoding="UTF8")
            txtdata = f.read()
            print(txtdata)

        elif (self.listNum.currentItem().text() == "2번"):
            f = open('txt/test2.txt', encoding="UTF8")
            txtdata = f.read()
            print(txtdata)

        elif (self.listNum.currentItem().text() == "3번"):
            f = open('txt/test3.txt', encoding="UTF8")
            txtdata = f.read()
            print(txtdata)
    """

class questionWindow(QMainWindow, form_question):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        global curNum, curType
        f = open(f"txt/test{curType.zfill(2)}{curNum.zfill(2)}.txt", "r", encoding="UTF-8")
        txtdata = f.read()
        self.label.setText(txtdata)

        self.submitBtn.clicked.connect(self.win3SubmitBtn)

    def win3SubmitBtn(self):
        answer = self.codeBox.toPlainText()
        print(answer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = mainWindow()
    mainWindow.show()
    app.exec_()