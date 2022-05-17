from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 101, 16)) 
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 90, 191, 16))
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 71, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 180, 71, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 310, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 310, 101, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 320, 101, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(0, 20, 82, 17))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(0, 40, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 60, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 71, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 171, 16))
        self.label_5.setObjectName("label_5")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 151, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 40, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 120, 91, 22))
        self.comboBox.setObjectName("comboBox")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 220, 401, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 350, 211, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 450, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 450, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 430, 71, 16))
        self.label_6.setObjectName("label_6")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Какой-то тест PyQt5"))
        self.label.setText(_translate("MainWindow", "Введите число"))
        self.label_2.setText(_translate("MainWindow", "Введите ваше имя"))
        self.label_3.setText(_translate("MainWindow", "Хотите узнать, запомнил ли я число?"))
        self.pushButton.setText(_translate("MainWindow", "Ответ"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_3.setText(_translate("MainWindow", "Ответ"))
        self.pushButton_4.setText(_translate("MainWindow", "Записать в файл"))
        self.radioButton.setText(_translate("MainWindow", "В квадрат"))
        self.radioButton_2.setText(_translate("MainWindow", "В куб"))
        self.radioButton_3.setText(_translate("MainWindow", "Не надо"))
        self.label_4.setText(_translate("MainWindow", "Возведение"))
        self.label_5.setText(_translate("MainWindow", "Какая степень вас интересует?"))
        self.pushButton_5.setText(_translate("MainWindow", "Нет"))
        self.pushButton_6.setText(_translate("MainWindow", "Да"))
        self.label_6.setText(_translate("MainWindow", "Прощаемся?"))
