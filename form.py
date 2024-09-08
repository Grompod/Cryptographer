# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(663, 545)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(225, 251, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(255, 246, 208, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(127, 118, 81, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(170, 158, 108, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(255, 237, 162, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        icon = QIcon(QIcon.fromTheme(u"czd"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(225, 251, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Niagara Solid"])
        font.setPointSize(48)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/newPrefix/132-1325883_transparent-typewriter-png-transparent-background-typewriter-icon-png.png"))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(308, 68, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Text_In = QLineEdit(self.centralwidget)
        self.Text_In.setObjectName(u"Text_In")
        self.Text_In.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.Text_In)

        self.Button_Code = QPushButton(self.centralwidget)
        self.Button_Code.setObjectName(u"Button_Code")
        palette1 = QPalette()
        brush8 = QBrush(QColor(98, 255, 216, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.Button_Code.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.Button_Code.setFont(font1)
        self.Button_Code.setCursor(QCursor(Qt.OpenHandCursor))
        self.Button_Code.setStyleSheet(u"background-color: rgb(98, 255, 216)\n"
"")
        self.Button_Code.setAutoRepeat(False)

        self.verticalLayout.addWidget(self.Button_Code)

        self.Code_Out = QTextEdit(self.centralwidget)
        self.Code_Out.setObjectName(u"Code_Out")
        self.Code_Out.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.Code_Out)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Code_In = QLineEdit(self.centralwidget)
        self.Code_In.setObjectName(u"Code_In")
        self.Code_In.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.verticalLayout_2.addWidget(self.Code_In)

        self.Button_Text = QPushButton(self.centralwidget)
        self.Button_Text.setObjectName(u"Button_Text")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush8)
        brush9 = QBrush(QColor(225, 250, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush9)
        brush10 = QBrush(QColor(161, 238, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush10)
        brush11 = QBrush(QColor(48, 113, 127, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush11)
        brush12 = QBrush(QColor(64, 151, 170, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush13 = QBrush(QColor(176, 240, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush14 = QBrush(QColor(97, 226, 255, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.Button_Text.setPalette(palette2)
        self.Button_Text.setFont(font1)
        self.Button_Text.setCursor(QCursor(Qt.OpenHandCursor))
        self.Button_Text.setStyleSheet(u"background-color: rgb(98, 255, 216)")

        self.verticalLayout_2.addWidget(self.Button_Text)

        self.Text_Out = QTextEdit(self.centralwidget)
        self.Text_Out.setObjectName(u"Text_Out")
        self.Text_Out.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.verticalLayout_2.addWidget(self.Text_Out)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 663, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cryptographer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cryptographer", None))
        self.label_2.setText("")
        self.Text_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435...", None))
        self.Button_Code.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.Code_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0448\u0438\u0444\u0440...", None))
        self.Button_Text.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

