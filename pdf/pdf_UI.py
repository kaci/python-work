#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This file add a Qt5 UI for the pdf_rotate_merge.py file.
"""

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QTextEdit, QAction, \
                            QFileDialog, QApplication, QPushButton, QLabel, \
                            QLineEdit, QGridLayout, QWidget, QCheckBox
from PyQt5.QtCore    import Qt
from PyQt5.QtGui     import QIcon
import sys, os

class Example(QWidget):
    
    def __init__(self):
        super().__init__() 
        self.initUI()
        
    def initUI(self):
        ''' initialize main window '''
        self.initLayout()        
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.initGrid()
        self.showFileList()        
        self.setLayout(self.grid)
                
        self.resize(500, 100)
        self.center()
        self.setWindowTitle('rePdf')    
        self.show()
    
    def initLayout(self):
        ''' initalize layout '''
        self.title     = QLabel('Select directory of editable pdf files.')
        self.dirTitle  = QLabel('Directory:')
        self.dirLine   = QLineEdit(os.getcwd())
        self.dirButton = QPushButton("Change", self)
        self.fileTitle = QLabel('File(s):')        
        self.dirButton.clicked.connect(self.showDialog)
        
    def initGrid(self):
        ''' initialize grid '''
        self.grid.addWidget(self.title, 0, 1)
        self.grid.addWidget(self.dirTitle, 1, 0)
        self.grid.addWidget(self.dirLine, 1, 1)
        self.grid.addWidget(self.dirButton, 1, 2)
        self.grid.addWidget(self.fileTitle, 2, 0)        
    
    def center(self):
        ''' the main window put on center '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def showDialog(self):
        ''' select directory box '''
        self.dirName = str(QFileDialog.getExistingDirectory(self, "Select Directory"))        
        if self.dirName:
            os.chdir(self.dirName)
            self.dirLine.setText(self.dirName)
            self.showFileList()
    
    def showFileList(self):
        ''' list filenames, and put in checkboxes '''
        self.clearLayout(self.grid)
        self.initLayout()
        self.initGrid()
        
        for en, fileName in enumerate(sorted([f for f in os.listdir('.') if os.path.isfile(f)])):            
            cb = QCheckBox(fileName, self)            
            self.grid.addWidget(cb, 2+en, 1)            
            cb.stateChanged.connect(self.fileList)
        
        self.setFixedSize(500, (en+3)*30)
        
    def fileList(self, state):
        ''' check the checkboxes '''
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
    
    def clearLayout(self, layout):
        ''' clear whole layout '''
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
