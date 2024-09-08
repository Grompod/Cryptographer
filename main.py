from email import message
from math import sqrt
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from random import randint
from form import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow
        self.setupUi(self)


        a1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        a2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        a3 = "1234567890., "
        self.alphabet = a1 + a2 + a3 + a1 + a2 + a3
        self.Button_Code.clicked.connect(self.TextToCode)
        self.Button_Text.clicked.connect(self.CodeToText)



    def TextToCode(self):
      self.Code_Out.clear()
      if self.Text_In.text() != '':
        step = randint(10, 128)
        message = self.Text_In.text()
        res = ''    

        for i in message:
          if i in self.alphabet:
            plaсe = self.alphabet.find(i)
            new_plaсe = plaсe + step
            res += self.alphabet[new_plaсe]  
          else:
            res += i
        
        resault_Code = res + str(self.alphabet[step])
        self.Code_Out.setText(resault_Code)
      else:
        self.Code_Out.setText("ВНИМАНИЕ! Ошибка: отсутствует сообщение.")
      self.Text_In.clear()




    def CodeToText(self):
      self.Text_Out.clear()
      if self.Code_In.text() != '':
        step =  int(self.alphabet.find(self.Code_In.text()[len(self.Code_In.text()) - 1]))
        message = str(self.Code_In.text())[:-1]
        res = ''    

        for i in message:
          if i in self.alphabet:
            plaсe = self.alphabet.find(i)
            new_plaсe = plaсe - step
            res += self.alphabet[new_plaсe]  
          else:
            res += i

        resault_Text = res
        self.Text_Out.setText(resault_Text)
      else:
        self.Text_Out.setText("ВНИМАНИЕ! Ошибка: отсутствует шифр.")      
      
      self.Code_In.clear()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())