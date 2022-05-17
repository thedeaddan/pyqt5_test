from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit,QComboBox,QButtonGroup
from window import Ui_MainWindow
import sys

global choice,button_choice
global result
global integer
choice = "Да"
button_choice = "В квадрат"
result = ""


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.quote)
        self.ui.pushButton_2.clicked.connect(self.clear)
        result = self.ui.pushButton_3.clicked.connect(self.degree)
        self.ui.pushButton_4.clicked.connect(self.save)
        self.ui.pushButton_5.clicked.connect(self.returns)
        self.ui.pushButton_6.clicked.connect(self.exit)
        self.ui.comboBox.addItems(["Да","Нет"])
        self.ui.comboBox.activated[str].connect(self.onActivated)

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.ui.radioButton)
        self.button_group.addButton(self.ui.radioButton_2)
        self.button_group.addButton(self.ui.radioButton_3)
        self.ui.radioButton.setChecked(True)
        self.button_group.buttonClicked.connect(self.radioButton_edit)

    def exit(self):
        sys.exit(0)

    def radioButton_edit(self,button):
        text = button.text()
        global button_choice
        if text == "В куб":
            button_choice = text
        elif text == "Не надо":
            button_choice = text
        elif text == "В квадрат":
            button_choice = text


    def onActivated(self,text):
        global choice
        if text == "Да":
            choice = text
        elif text == "Нет":
            choice = text
            

    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
    def returns(self):
        self.ui.radioButton.setChecked(True)
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        QMessageBox.critical(self, "Подтверждение", "Введите данные заново..", QMessageBox.Ok)

    def quote(self):
        global integer
        quote_max = self.ui.lineEdit_3
        integer = str(self.ui.lineEdit.text())
        name = str(self.ui.lineEdit_2.text())
        if integer == "":
            if name == "":
                quote_max.setText("Вы ничего не ввели")
            else:
                quote_max.setText(f"{name}, вы не ввели число")
        else:
            try:
                if "," in integer:
                    integer = integer.replace(",",".")
                    self.ui.lineEdit.setText(integer)
                integer = float(integer)
                integer = str(integer)[:-2]
                if choice == "Нет":
                    if name == "":
                        quote_max.setText(f"Ладно Безымянный, не запомню число, но там {integer}")
                    else:
                        quote_max.setText(f"Ладно {name}, не запомню число, но там {integer}")
                else:
                    if name == "":
                        quote_max.setText(f"Ладно Безымянный, запомню число, там {integer}")
                    else:
                        quote_max.setText(f"Ладно {name}, запомню число, там {integer}")
            except:
                quote_max.setText(f"Ошибка! {integer} - не число")

    def degree(self):
        integer = str(self.ui.lineEdit.text())
        if "," in integer:
            integer = integer.replace(",",".")
            self.ui.lineEdit.setText(integer)
        try:
            global result
            if integer != "":
                integer = float(integer)
                if button_choice == "В квадрат":
                    self.ui.lineEdit_4.setText(str(round(integer**2,3)))
                    result = round(integer**2,3)
                elif button_choice == "В куб":
                    self.ui.lineEdit_4.setText(str(round(integer**3,3)))
                    result = round(integer**3,3)
                elif button_choice == "Не надо":
                    self.ui.lineEdit_4.setText(str(integer))
                    result = integer
            else:
                self.ui.lineEdit_4.setText("Вы ещё не ввели число")
        except:
            self.ui.lineEdit_4.setText(f"Ошибка! {integer} - не число")


    def save(self):
        f = open('result.txt','a')
        if result != "":
            integer = str(self.ui.lineEdit.text())
            if integer != "":
                    if button_choice != "Не надо":
                        line = f"При возведении {integer} {button_choice} получилось {result}\n"
                    else:
                        line = f"Программа ничего не сделала и получила {result}\n"
                    f.write(line)
                    f.close()
            else:
                self.ui.lineEdit_4.setText("Введите исходное число")
        else:
            self.ui.lineEdit_4.setText("Нажмите кнопку ответ")



app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
