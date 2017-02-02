# -*- coding: utf-8 -*-

'''
Created on 2017/01/25

@author: Brian
'''

import sys, re
import database
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QApplication, QPushButton, QLineEdit)

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
    
        self.initUI()
        
        
    def initUI(self):
        self.newList = storeList()
        
        self.addBtn = QPushButton('Add', self)
        self.removeBtn = QPushButton('Remove Spaces', self)
        self.showListBtn = QPushButton('Show List', self)
        self.clearListBtn = QPushButton('Clear List', self)
        self.inputText = QLineEdit(self)
        self.outputText = QLineEdit(self)
        self.setWindowTitle('Text Tools')
        
        editWindowLayout = QVBoxLayout()
        editWindowLayout.addWidget(self.addBtn)
        editWindowLayout.addWidget(self.removeBtn)
        editWindowLayout.addWidget(self.showListBtn)
        editWindowLayout.addWidget(self.clearListBtn)
        editWindowLayout.addWidget(self.inputText)
        editWindowLayout.addWidget(self.outputText)
        
        self.setLayout(editWindowLayout)
        self.addBtn.clicked.connect(self.titleText)
        self.removeBtn.clicked.connect(self.removeSpaces)
        self.showListBtn.clicked.connect(self.newList.showItems)
        self.clearListBtn.clicked.connect(self.newList.clearList)
        
        self.setGeometry(300, 300, 250, 150)
        self.show()
        
    def titleText(self):
        inputText = self.inputText.text()
        self.outputText.setText(inputText)
        self.newList.addItem(inputText)
    
    def removeSpaces(self):
        inputText = self.inputText.text()
        
        newString = inputText.replace(' ', '')
        
        regExpTestCode  = re.compile('[#\$].*?#')
        
        originalCode = regExpTestCode.findall(inputText)
        formattedCode = regExpTestCode.findall(newString)
        
        i = 0
        while i < len(originalCode):
            newString = newString.replace(formattedCode[i], originalCode[i])
            i += 1
            
        self.outputText.setText(newString)
        
class storeList(list):
    
    def addItem(self, item):
        self.append(item)
        database.data_entry(item)        
    
    def showItems(self):
        for items in self:
            print(items)
    
    def clearList(self):
        del self[:]
    

            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    GUI = MainWindow()
    database.create_table()
    sys.exit(app.exec_())