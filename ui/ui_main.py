# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit,QLabel
from PyQt5.QtCore import QMetaObject,QCoreApplication,QSize
from PyQt5.QtGui import QIcon,QPixmap,QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 188)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/title.ico"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#MainWindow{background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"border-style:none;;\n"
"background-color:#20b1ff;\n"
"border:2px;\n"
"border-radius:2px;\n"
"padding:2px 4px;\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:hover{color:lightskyblue}\n"
"QPushButton:pressed {\n"
"    /* 改变背景色 */\n"
"    /* background-color:rgb(180, 180, 180,120); */\n"
"    /* 改变边框风格 */\n"
"    /* border-style:inset; */\n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:6px;\n"
"    padding-top:4px;\n"
"}\n"
"#pushButton_run{\n"
"text-align: center;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #20b1ff;\n"
"border-radius:2px;\n"
"background-color:#f0f0f0;\n"
"}\n"
"\n"
"#lineEdit_domain,#lineEdit_random{\n"
"background-color:#ffffff;\n"
"}\n"
"\n"
"QComboBox{\n"
"border: 1px solid #20b1ff;\n"
"border-radius:2px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol- position :  top  right ;\n"
"     width :  20px ;\n"
"     border-left-width :  1px ;\n"
"     border-left-color : darkgray;\n"
"     border-left-style :  solid ; \n"
"     border-top-right-radius:  3px ;\n"
"     border-bottom-right-radius:  3px ;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_old = QPushButton(self.widget)
        self.pushButton_old.setMinimumSize(QSize(120, 25))
        self.pushButton_old.setMaximumSize(QSize(120, 25))
        font = QFont()
        font.setPointSize(10)
        self.pushButton_old.setFont(font)
        self.pushButton_old.setObjectName("pushButton_old")
        self.horizontalLayout.addWidget(self.pushButton_old)
        self.lineEdit_old = QLineEdit(self.widget)
        self.lineEdit_old.setMinimumSize(QSize(0, 25))
        self.lineEdit_old.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_old.setFont(font)
        self.lineEdit_old.setText("")
        self.lineEdit_old.setReadOnly(True)
        self.lineEdit_old.setObjectName("lineEdit_old")
        self.horizontalLayout.addWidget(self.lineEdit_old)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_new = QPushButton(self.widget_2)
        self.pushButton_new.setMinimumSize(QSize(120, 25))
        self.pushButton_new.setMaximumSize(QSize(120, 25))
        font = QFont()
        font.setPointSize(10)
        self.pushButton_new.setFont(font)
        self.pushButton_new.setObjectName("pushButton_new")
        self.horizontalLayout_2.addWidget(self.pushButton_new)
        self.lineEdit_new = QLineEdit(self.widget_2)
        self.lineEdit_new.setMinimumSize(QSize(0, 25))
        self.lineEdit_new.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_new.setFont(font)
        self.lineEdit_new.setReadOnly(True)
        self.lineEdit_new.setObjectName("lineEdit_new")
        self.horizontalLayout_2.addWidget(self.lineEdit_new)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QLabel(self.widget_4)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.pushButton_run = QPushButton(self.widget_4)
        self.pushButton_run.setMinimumSize(QSize(100, 25))
        self.pushButton_run.setMaximumSize(QSize(100, 25))
        font = QFont()
        font.setPointSize(10)
        self.pushButton_run.setFont(font)
        self.pushButton_run.setObjectName("pushButton_run")
        self.horizontalLayout_4.addWidget(self.pushButton_run)
        self.verticalLayout.addWidget(self.widget_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片去重"))
        self.pushButton_old.setText(_translate("MainWindow", "选择原图文件夹"))
        self.pushButton_new.setText(_translate("MainWindow", "选择新图文件夹"))
        self.pushButton_run.setText(_translate("MainWindow", "运行"))
import img_rc
