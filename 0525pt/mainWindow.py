from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import sys
import openai
openai.api_key = "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"
chap = ""
level = ""
index = 1
parts = []

firstForm = uic.loadUiType("ui/firstWindow.ui")[0]
secondForm = uic.loadUiType("ui/secondWindow.ui")[0]
testForm = uic.loadUiType("ui/testWindow.ui")[0]
codingForm = uic.loadUiType("ui/codingWindow.ui")[0]

class firstWindow(QMainWindow, firstForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for i in range(1, 8):
            self.listFirst.addItem(f"chap{i}")

        self.listFirst.clicked.connect(self.chapClicked)
        self.startBtn.clicked.connect(self.startClicked)

    def chapClicked(self):
        global chap
        self.listSecond.clear()
        chap = self.listFirst.currentRow()+1
        for i in range(1,8):
            if chap == i:
                for j in range(1, 9):
                    self.listSecond.addItem(f"{i}-{j}")

    def startClicked(self):
        global level
        level = self.listSecond.currentRow()+1
        if level != 0:
            self.second = secondWindow()
            self.close()
            self.second.show()

        #listWidget에 이미지 넣기 #실패
        #chap1 = QListWidgetItem(QIcon("img/chap1.png"), '')
        #self.listFirst.addItem(chap1)

class secondWindow(QWidget, secondForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.nextBtn.clicked.connect(self.nextClicked)

    def nextClicked(self):
        #global chap, level
        #if 마지막 장일때 nextBtn ==> 시험보기로 바꿈 or 시험보기 버튼 생김
        self.test = testWindow()
        self.hide()
        self.test.show()

class testWindow(QWidget, testForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        global chap, level, index, parts
        self.submitBtn.clicked.connect(self.submitClicked)
        self.doCodingBtn.clicked.connect(self.codingClicked)

        self.testTitle.setText(f"{chap} - {level}")
        ##test0101.txt부분 test{chap}{level}로 변경해서 선택한 챕터의 문제 나올 수 있도록 변경하기
        with open("test/test0101.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()

        parts = [line.strip().split(',') for line in lines]#line(str)을 parts(list)로 변경
        question = parts[0][0]
        options = '\n'.join(parts[0][1:5])
        self.testQuestion.setText(question)
        self.testOption.setText(options)

    def submitClicked(self):
        global index, parts
        userAnswer = self.answerText.text()
        self.answerText.clear()
        if index == 3:#len(parts):
            print("end")
            self.doCodingBtn.setEnabled(True)
        else:
            if userAnswer == parts[index-1][5]:
                question = parts[index][0]
                options = '\n'.join(parts[index][1:5])
                self.testQuestion.setText(question)
                self.testOption.setText(options)
                self.statusLabel.setText("정답입니다")
                index += 1
            else:
                self.statusLabel.setText("다시 확인해주세요")

    def codingClicked(self):
        self.coding = codingWindow()
        self.hide()
        self.coding.show()

class codingWindow(QWidget, codingForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.codeSubmit.clicked.connect(self.submitClicked)
        self.codingQuestion.setText("1부터 100까지의 합을 구하는 코드를 작성하시오")

    def submitClicked(self):
        answer = self.codeBox.toPlainText().splitlines()
        escapedAnswer = [i.replace("\\", "\\\\") for i in answer]
        escapedAnswer = [i.replace("\n", "\\n") for i in escapedAnswer]
        escapedAnswer = [i.replace('"', '\\"') for i in escapedAnswer]
        escapedAnswer = [i.replace("'", "\\'") for i in escapedAnswer]
        escapedAnswer = [item + '\n' for item in escapedAnswer]
        #print(escapedAnswer)
        self.gptAnswer(escapedAnswer)

    def gptAnswer(self, escapedAnswer):
        escapedAnswer.insert(0, "#####다음 문제의 파이썬 코딩\n")
        escapedAnswer.insert(1, "#####오류가 있는 부분 알려줘")
        #escapedAnswer.insert(0, "#####다음 파이썬 코드의 예상 출력 값")
        escapedAnswer.insert(2, f"문제 : {self.codingQuestion.text()}")
        escapedAnswer.append("###")
        prompt = str(escapedAnswer).strip('[]')
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,  # 다양성
            max_tokens=2000,  # 문장 길이
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["###"]
        )
        print(response.choices[0].text)
        #print([codecs.decode(i, 'unicode_escape') for i in response.choices[0].text])#escape 문자 제거

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = firstWindow()

    """
    stackedWidget = QStackedWidget(mainWindow)

    firstWidget = uic.loadUi("ui/firstWindow.ui")
    secondWidget = uic.loadUi("ui/secondWindow.ui")

    stackedWidget.addWidget(firstWidget)
    stackedWidget.addWidget(secondWidget)

    mainWindow.setCentralWidget(stackedWidget)
    """

    mainWindow.show()
    app.exec_()
