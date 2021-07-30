# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1276, 864)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1291, 781))
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_itriLogoBig = QtWidgets.QLabel(self.tab)
        self.label_itriLogoBig.setGeometry(QtCore.QRect(0, 70, 723, 168))
        self.label_itriLogoBig.setText("")
        self.label_itriLogoBig.setPixmap(QtGui.QPixmap("../../Downloads/itri.png"))
        self.label_itriLogoBig.setObjectName("label_itriLogoBig")
        self.textBrowser_mainName = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_mainName.setGeometry(QtCore.QRect(730, 90, 411, 131))
        self.textBrowser_mainName.setObjectName("textBrowser_mainName")
        self.pushButton_reset = QtWidgets.QPushButton(self.tab)
        self.pushButton_reset.setGeometry(QtCore.QRect(1050, 600, 91, 71))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_btConnect = QtWidgets.QPushButton(self.tab)
        self.pushButton_btConnect.setGeometry(QtCore.QRect(160, 350, 171, 71))
        self.pushButton_btConnect.setObjectName("pushButton_btConnect")
        self.label_BTConnected = QtWidgets.QLabel(self.tab)
        self.label_BTConnected.setGeometry(QtCore.QRect(160, 570, 131, 20))
        self.label_BTConnected.setObjectName("label_BTConnected")
        self.label_BTConnected_Item = QtWidgets.QLabel(self.tab)
        self.label_BTConnected_Item.setGeometry(QtCore.QRect(260, 580, 101, 16))
        self.label_BTConnected_Item.setObjectName("label_BTConnected_Item")
        self.textEdit_btResult = QtWidgets.QTextEdit(self.tab)
        self.textEdit_btResult.setGeometry(QtCore.QRect(500, 330, 471, 341))
        self.textEdit_btResult.setObjectName("textEdit_btResult")
        self.label_btDevice = QtWidgets.QLabel(self.tab)
        self.label_btDevice.setGeometry(QtCore.QRect(160, 460, 101, 31))
        self.label_btDevice.setObjectName("label_btDevice")
        self.comboBox_selectCom = QtWidgets.QComboBox(self.tab)
        self.comboBox_selectCom.setGeometry(QtCore.QRect(160, 491, 121, 31))
        self.comboBox_selectCom.setObjectName("comboBox_selectCom")
        self.pushButton_connectBT = QtWidgets.QPushButton(self.tab)
        self.pushButton_connectBT.setGeometry(QtCore.QRect(330, 460, 93, 71))
        self.pushButton_connectBT.setObjectName("pushButton_connectBT")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 1121, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_itriLogo = QtWidgets.QLabel(self.tab_2)
        self.label_itriLogo.setGeometry(QtCore.QRect(1100, -10, 191, 121))
        self.label_itriLogo.setText("")
        self.label_itriLogo.setPixmap(QtGui.QPixmap("../../Downloads/itri2.png"))
        self.label_itriLogo.setObjectName("label_itriLogo")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(1150, 720, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_CH1SNR = QtWidgets.QLabel(self.tab_2)
        self.label_CH1SNR.setGeometry(QtCore.QRect(1130, 120, 141, 16))
        self.label_CH1SNR.setObjectName("label_CH1SNR")
        self.label_CH1SNR_val = QtWidgets.QLabel(self.tab_2)
        self.label_CH1SNR_val.setGeometry(QtCore.QRect(1150, 140, 111, 41))
        self.label_CH1SNR_val.setObjectName("label_CH1SNR_val")
        self.label_CH2SNR = QtWidgets.QLabel(self.tab_2)
        self.label_CH2SNR.setGeometry(QtCore.QRect(1130, 220, 141, 16))
        self.label_CH2SNR.setObjectName("label_CH2SNR")
        self.label_CH2SNR_val = QtWidgets.QLabel(self.tab_2)
        self.label_CH2SNR_val.setGeometry(QtCore.QRect(1150, 240, 111, 41))
        self.label_CH2SNR_val.setObjectName("label_CH2SNR_val")
        self.label_acc = QtWidgets.QLabel(self.tab_2)
        self.label_acc.setGeometry(QtCore.QRect(1130, 330, 161, 16))
        self.label_acc.setObjectName("label_acc")
        self.label_acc_val = QtWidgets.QLabel(self.tab_2)
        self.label_acc_val.setGeometry(QtCore.QRect(1150, 350, 111, 31))
        self.label_acc_val.setObjectName("label_acc_val")
        self.label_capaci = QtWidgets.QLabel(self.tab_2)
        self.label_capaci.setGeometry(QtCore.QRect(1130, 460, 161, 16))
        self.label_capaci.setObjectName("label_capaci")
        self.label_capaci_val = QtWidgets.QLabel(self.tab_2)
        self.label_capaci_val.setGeometry(QtCore.QRect(1150, 480, 111, 41))
        self.label_capaci_val.setObjectName("label_capaci_val")
        self.label_pressure = QtWidgets.QLabel(self.tab_2)
        self.label_pressure.setGeometry(QtCore.QRect(1130, 620, 161, 16))
        self.label_pressure.setObjectName("label_pressure")
        self.label_pressure_val = QtWidgets.QLabel(self.tab_2)
        self.label_pressure_val.setGeometry(QtCore.QRect(1150, 640, 111, 41))
        self.label_pressure_val.setObjectName("label_pressure_val")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1050, 790, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1160, 790, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(40, 790, 121, 28))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(170, 790, 121, 28))
        self.pushButton_stop.setObjectName("pushButton_stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1276, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_mainName.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:28pt; font-weight:600; color:#00007f;\">耦合低壓迫</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:28pt; font-weight:600; color:#00007f;\">感測袖帶系統</span><span style=\" font-size:28pt; font-weight:600; color:#00007f;\"> </span></p></body></html>"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_btConnect.setText(_translate("MainWindow", "Searching BT Device"))
        self.label_BTConnected.setText(_translate("MainWindow", "BT Connected:"))
        self.label_BTConnected_Item.setText(_translate("MainWindow", "0"))
        self.label_btDevice.setText(_translate("MainWindow", "BT Device:"))
        self.pushButton_connectBT.setText(_translate("MainWindow", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Setting"))
        self.pushButton.setText(_translate("MainWindow", "Save data"))
        self.label_CH1SNR.setText(_translate("MainWindow", "CH1 SNR(dB):"))
        self.label_CH1SNR_val.setText(_translate("MainWindow", "0.0"))
        self.label_CH2SNR.setText(_translate("MainWindow", "CH2 SNR(dB):"))
        self.label_CH2SNR_val.setText(_translate("MainWindow", "0.0"))
        self.label_acc.setText(_translate("MainWindow", "Accuracy(%):"))
        self.label_acc_val.setText(_translate("MainWindow", "0.0"))
        self.label_capaci.setText(_translate("MainWindow", "Capacitance(nF):"))
        self.label_capaci_val.setText(_translate("MainWindow", "0.0"))
        self.label_pressure.setText(_translate("MainWindow", "Pressure value(mmHg):"))
        self.label_pressure_val.setText(_translate("MainWindow", "0.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Processing"))
        self.pushButton_2.setText(_translate("MainWindow", "最小化視窗"))
        self.pushButton_3.setText(_translate("MainWindow", "關閉視窗"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
