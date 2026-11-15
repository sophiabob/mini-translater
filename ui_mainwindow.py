# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(783, 398)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout_3 = QGridLayout(self.centralWidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(10, 5, 10, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 35, 10, 10)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_network = QPushButton(self.centralWidget)
        self.pushButton_network.setObjectName(u"pushButton_network")

        self.horizontalLayout.addWidget(self.pushButton_network)

        self.pushButton_settings = QPushButton(self.centralWidget)
        self.pushButton_settings.setObjectName(u"pushButton_settings")

        self.horizontalLayout.addWidget(self.pushButton_settings)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox_languageFrom = QComboBox(self.centralWidget)
        self.comboBox_languageFrom.setObjectName(u"comboBox_languageFrom")

        self.verticalLayout.addWidget(self.comboBox_languageFrom)

        self.textEdit_transFrom = QTextEdit(self.centralWidget)
        self.textEdit_transFrom.setObjectName(u"textEdit_transFrom")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_transFrom.sizePolicy().hasHeightForWidth())
        self.textEdit_transFrom.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.textEdit_transFrom)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.line = QFrame(self.centralWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox_languagTo = QComboBox(self.centralWidget)
        self.comboBox_languagTo.setObjectName(u"comboBox_languagTo")

        self.verticalLayout_2.addWidget(self.comboBox_languagTo)

        self.textEdit_transTo = QTextEdit(self.centralWidget)
        self.textEdit_transTo.setObjectName(u"textEdit_transTo")
        sizePolicy.setHeightForWidth(self.textEdit_transTo.sizePolicy().hasHeightForWidth())
        self.textEdit_transTo.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.textEdit_transTo)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_translation = QPushButton(self.centralWidget)
        self.pushButton_translation.setObjectName(u"pushButton_translation")

        self.horizontalLayout_2.addWidget(self.pushButton_translation)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 783, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_network.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0435\u0442\u044c", None))
        self.pushButton_settings.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.pushButton_translation.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438", None))
    # retranslateUi

