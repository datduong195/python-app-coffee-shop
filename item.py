# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'item.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(881, 606)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowTitle(self._translate("MainWindow", "Item List"))
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 861, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 859, 719))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.groupBoxHorList= [0,210,420,630]
        self.groupBoxVerOffset = 180
        print("Calling create group box function ...")
        self.createGroupBox("E:/Bi/CF_App/item")

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        #Ok/Cancel Button
 
    def createGroupBox(self,path):
        self.spinBoxList = []
        self.layout = QGridLayout(self.scrollAreaWidgetContents) 
        folder = os.fsencode(path)
        countItem = 0
        verOffset = 0
        for file in os.listdir(folder):   
            filename = os.fsdecode(file)
            if filename.endswith('.jpg'):
                print("File Name: "+ str(filename))
                if(countItem<4):
                    groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
                    groupBox.setEnabled(True)
                    groupBox.setFixedSize(201,171)
                    #self.groupBox.setGeometry(QtCore.QRect(self.groupBoxHorList[countItem], verOffset, 201, 171))
                    font = QtGui.QFont()
                    font.setPointSize(5)
                    groupBox.setFont(font)
                    groupBox.setFlat(False)
                    groupBox.setCheckable(False)
                    groupBox.setObjectName("groupBox")

                    image = QtWidgets.QLabel(groupBox)
                    image.setGeometry(QtCore.QRect(10, 10, 181, 111))
                    image.setText("")
                    image.setPixmap(QtGui.QPixmap("item/"+str(filename)))
                    image.setScaledContents(True)
                    image.setObjectName("image")

                    spinBox = QtWidgets.QSpinBox(groupBox)
                    spinBox.setGeometry(QtCore.QRect(130, 130, 61, 31))
                    font.setPointSize(10)
                    spinBox.setFont(font)
                    spinBox.setObjectName(filename)
                    self.spinBoxList.append(spinBox)
                    
                    label = QtWidgets.QLabel(groupBox)
                    label.setGeometry(QtCore.QRect(70, 129, 91, 31))
                    font.setPointSize(12)
                    label.setFont(font)
                    label.setObjectName("label")
                    label.setText(self._translate("MainWindow", "Qantity"))
                    self.layout.addWidget(groupBox, verOffset,self.groupBoxHorList[countItem]) 
                    countItem+=1
                else:
                    countItem = 0
                    verOffset+= self.groupBoxVerOffset

