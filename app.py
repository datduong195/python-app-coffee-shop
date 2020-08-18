# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QFileDialog,QAction
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,json,time,os
from item import Ui_MainWindow
from escpos.printer import Usb
priceList ={
    "bac_siu_da":22000,
    "ca_cao_sua_da":30000,
    "cafe_den_da":15000,
    "cafe_sua_da":20000,
    "sinh_to_bo":35000,
    "sinh_to_dau":35000,
    "sinh_to_dau_chuoi":35000,
    "sinh_to_sau_rieng":40000,
    "soda_bac_ha":20000,
    "soda_blue":25000,
    "soda_chanh":25000,
    "soda_kiwi":25000,
    "soda_nho_den":25000,
    "soda_sua_hot_ga":38000,
    "sua_tuoi_cafe":22000,
    "tra_bong_cuc":30000,
    "tra_chanh_gung_mat_ong":30000,
    "tra_dao_cam_sa":30000,
    "tra_lipton":25000,
    "yogurt_cam_tuoi":30000,
    "yogurt_dau_tuoi":30000,
    "yogurt_hat_chia":25000
}
class mainWindow(object):


    def setupUi(self, Dialog):
        self.loginDatabase = {}
        self.loginDatabase["datduong_1995"] = "38697071"
        self.loginDatabase["nguyenvy_1995"] = "09010902"
        self.adminRight = False
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(400, 385)
        self.itemDataBase = {}
        self.itemBox = QtWidgets.QGroupBox(Dialog)
        self.itemBox.setGeometry(QtCore.QRect(10, 90, 381, 291))
        self.itemBox.setObjectName("itemBox")

        self.checkOutBtn = QtWidgets.QPushButton(self.itemBox)
        self.checkOutBtn.setGeometry(QtCore.QRect(290, 110, 75, 23))
        self.checkOutBtn.setObjectName("checkOutBtn")
        self.checkOutBtn.clicked.connect(self.checkOutFunction)

        self.noteBtn = QtWidgets.QPushButton(self.itemBox)
        self.noteBtn.setGeometry(QtCore.QRect(290, 80, 75, 23))
        self.noteBtn.setObjectName("noteBtn")
        self.noteBtn.setEnabled(False)

        self.addItemBtn = QtWidgets.QPushButton(self.itemBox)
        self.addItemBtn.setGeometry(QtCore.QRect(290, 50, 75, 23))
        self.addItemBtn.setObjectName("addItemBtn")
        self.addItemBtn.clicked.connect(self.addItemFunction)

        self.tableList = [i for i in range(21)]
        self.tableDrop = QtWidgets.QComboBox(self.itemBox)
        self.tableDrop.setGeometry(QtCore.QRect(200, 20, 69, 22))
        self.tableDrop.setObjectName("tableDrop")
        
        for table in self.tableList:
            self.tableDrop.addItem(str(table))
            self.itemDataBase[str(table)] = ["Table Number "+str(table)]
        self.tableDrop.activated.connect(self.loadTableItem) 

        self.tableNoLbl = QtWidgets.QLabel(self.itemBox)
        self.tableNoLbl.setGeometry(QtCore.QRect(120, 10, 131, 41))
        self.tableNoLbl.setObjectName("tableNoLbl")
        

        self.addTable = QtWidgets.QPushButton(self.itemBox)
        self.addTable.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.addTable.setObjectName("AddTable")
        self.addTable.clicked.connect(self.addTableFunction)
        self.addTable.setEnabled(False)

        self.showItem = QtWidgets.QTextEdit(self.itemBox)
        self.showItem.setGeometry(QtCore.QRect(10, 50, 261, 231))
        self.showItem.setObjectName("showItem")
        self.showItem.setReadOnly(True)

        self.loadBackupFile = QtWidgets.QPushButton(self.itemBox)
        self.loadBackupFile.setGeometry(QtCore.QRect(290, 20, 75, 23))
        self.loadBackupFile.setObjectName("loadBackupFile")
        self.loadBackupFile.clicked.connect(self.loadBackupFunction)
        self.loadBackupFile.setEnabled(False)

        self.loginBox = QtWidgets.QGroupBox(Dialog)
        self.loginBox.setGeometry(QtCore.QRect(10, 10, 381, 81))
        self.loginBox.setObjectName("loginBox")

        self.userLbl = QtWidgets.QLabel(self.loginBox)
        self.userLbl.setGeometry(QtCore.QRect(10, 20, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userLbl.setFont(font)
        self.userLbl.setObjectName("userLbl")

        self.inputUser = QtWidgets.QLineEdit(self.loginBox)
        self.inputUser.setGeometry(QtCore.QRect(70, 20, 201, 21))
        self.inputUser.setObjectName("inputUser")

        self.loginBtn = QtWidgets.QPushButton(self.loginBox)
        self.loginBtn.setGeometry(QtCore.QRect(290, 20, 75, 23))
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.clicked.connect(self.loginFunction)

        self.inputPwd = QtWidgets.QLineEdit(self.loginBox)
        self.inputPwd.setGeometry(QtCore.QRect(70, 50, 201, 21))
        self.inputPwd.setObjectName("inputPwd")
        self.inputPwd.setEchoMode(QtWidgets.QLineEdit.Password)

        self.passLbl = QtWidgets.QLabel(self.loginBox)
        self.passLbl.setGeometry(QtCore.QRect(10, 50, 47, 21))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.passLbl.setFont(font)
        self.passLbl.setObjectName("passLbl")

        self.msgWrong = QMessageBox()
        self.msgWrong.setWindowTitle("Login Check")
        self.msgWrong.setText("Wrong user/password!")
        self.msgWrong.setIcon(QMessageBox.Critical)

        self.msgCorrect = QMessageBox()
        self.msgCorrect.setWindowTitle("Login Check")
        self.msgCorrect.setText(" Login Successful!")
        self.msgCorrect.setIcon(QMessageBox.Information)
  
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.removeOldBackupFile()
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.itemBox.setTitle(_translate("Dialog", "GroupBox"))
        self.checkOutBtn.setText(_translate("Dialog", "Check out"))
        self.noteBtn.setText(_translate("Dialog", "Note"))
        self.addItemBtn.setText(_translate("Dialog", "Add Items"))
        self.tableDrop.setItemText(0, _translate("Dialog", "1"))
        self.tableDrop.setItemText(1, _translate("Dialog", "2"))
        self.tableDrop.setItemText(2, _translate("Dialog", "3"))
        self.tableNoLbl.setText(_translate("Dialog", "Table Number"))
        self.showItem.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.addTable.setText(_translate("Dialog", "Add Table"))
        self.loginBox.setTitle(_translate("Dialog", "GroupBox"))
        self.userLbl.setText(_translate("Dialog", "User:"))
        self.loginBtn.setText(_translate("Dialog", "Login"))
        self.passLbl.setText(_translate("Dialog", "Pass:"))
        self.loadBackupFile.setText(_translate("Dialog", "Load Backup"))

    def addItemFunction(self):
        self.addItemWindow = Ui_MainWindow()
        self.itemWindow = QtWidgets.QMainWindow()
        self.addItemWindow.setupUi(self.itemWindow)
        self.itemWindow.setWindowIcon(QtGui.QIcon('sushi.jpg'))
        self.buttonBox = QtWidgets.QDialogButtonBox(self.addItemWindow.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(620, 560, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setToolTipDuration(4)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.okButtonClick)
        self.buttonBox.rejected.connect(self.cancelButtonClick)
        self.buttonBox.setObjectName("buttonBox")
        self.itemWindow.show()
    def okButtonClick(self):
        for item in self.addItemWindow.spinBoxList:
            if(str(item.value())!= "0"):
                printOut = str(item.value())+" x "+item.objectName()
                self.itemDataBase[self.tableDrop.currentText()].append(printOut)
                #self.showItem.append(printOut)
        self.itemWindow.close()
        self.showItem.clear()
        for item in self.itemDataBase[self.tableDrop.currentText()]:
            self.showItem.append(item.split(".")[0])
        self.writeBackupFile()
    def cancelButtonClick(self):
        self.itemWindow.close()

    def addTableFunction(self):
        currentKeyNumber = len(self.itemDataBase.keys())
        self.tableDrop.addItem(str(currentKeyNumber))
        self.itemDataBase[str(currentKeyNumber)] = ["Table Number "+str(currentKeyNumber)]

    def loadTableItem(self):
        self.showItem.clear()
        for item in self.itemDataBase[self.tableDrop.currentText()]:
            self.showItem.append(item)
    def loginFunction(self):
        try:
            user = self.inputUser.text()
            print("user : " + user)
            pwd  = self.inputPwd.text()
            print("pwd : " + pwd)
        except:
            print("Missing Input!")
            self.msgWrong.exec_()
            pass
        try:
            if(self.loginDatabase[user] == pwd):
                print("Login Successful!")
                self.msgCorrect.exec_()
                self.adminRight = True
                self.loadBackupFile.setEnabled(True)
                self.addTable.setEnabled(True)
            else:
                self.msgWrong.exec_()

        except:
            print("Wrong password! ")
            self.msgWrong.exec_()

    def writeBackupFile(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        with open("backup/"+timestr+'.json', 'w') as backupFile:
            json.dump(self.itemDataBase,backupFile)
    def loadBackupFunction(self):
        try:
            filename = QFileDialog.getOpenFileName()
            path = filename[0]
            with open(path, "r") as f:
                self.itemDataBase.clear()
                self.itemDataBase = json.load(f)
            self.loadTableItem()
        except:
            pass
    def removeOldBackupFile(self):
        currentMonthStr = time.strftime("%m")
        folder = os.fsencode("backup")
        for file in os.listdir(folder):
            filename = os.fsdecode(file)
            if filename.endswith('.json') and filename[4:6] != currentMonthStr: 
                os.remove("backup/"+filename)
                
    def showNotAuthorize(self):
        notAdmin = QMessageBox()
        notAdmin.setWindowTitle("Login Check")
        notAdmin.setText("Not Authorized! Please Login!")
        notAdmin.setIcon(QMessageBox.Critical)
        notAdmin.exec_()
    def checkOutFunction(self):

        stringToPrint = self.getPriceFromItem()
        print(stringToPrint)
        self.showItem.clear()
        self.itemDataBase[self.tableDrop.currentText()].clear()
        self.itemDataBase[self.tableDrop.currentText()] = ["Table Number "+ self.tableDrop.currentText()]
        self.showItem.append("Table Number "+ self.tableDrop.currentText())
        
    def getPriceFromItem(self):
        temp = self.itemDataBase[self.tableDrop.currentText()].pop(0)
        totalPrice = 0
        tempString = ""
        for item in self.itemDataBase[self.tableDrop.currentText()]:
            quantity = item.split(" x ")[0]
            name = item.split(" x ")[1].split(".")[0]
            priceOfOne = priceList[name]
            priceActual = priceOfOne*int(quantity)
            totalPrice += priceActual
            ##print(item.split(".")[0] + " = " + str(price))
            tempString += item.split(".")[0] + " : " + str("{:0,.2f}".format(float(priceOfOne))) + " = " + str("{:0,.2f}".format(float(priceActual))) + "vnd\n"
        tempString += """==============================
                    Total: """ + str("{:0,.2f}".format(float(totalPrice)))+"vnd"
        return tempString


    # def closeEvent(self, event):
    #     close = QtWidgets.QMessageBox.question(self,
    #                                  "QUIT",
    #                                  "Are you sure want to stop process?",
    #                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    #     if close == QtWidgets.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

def main():
    app = QApplication(sys.argv)
    ui = mainWindow()
    window = QDialog()
    window.setWindowIcon(QtGui.QIcon('sushi.jpg'))
    ui.setupUi(window)
    window.keyPressEvent =keyPressEvent
    window.show()
    app.exec_()

def keyPressEvent(event):
    event.ignore()
if __name__ == '__main__':
    main()