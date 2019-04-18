# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore,QtWidgets
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Dialog例子')
        self.resize(320,400)
        #创建文本框
        self.txtName=QLineEdit(self)
        self.txtName.move(20, 20)
        self.txtName.resize(280, 20)
        self.txtAge=QLineEdit(self)
        self.txtAge.move(20, 60)
        self.txtAge.resize(280, 20)
        #创建添加按钮
        self.button = QPushButton(u'添加', parent=self)
        self.button.move(20, 100)
        self.button.resize(280, 20)
        #添加信号槽
        self.button.clicked.connect(self.add)
    def add(self):
        dialog = Dialog(parent=self)
        if dialog.exec_():
            self.txtName.setText(dialog.name())
            self.txtAge.setText(str(dialog.age()))
        dialog.destroy()

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.resize(240, 200)
        #表格布局，用来布局QLabel和QLineEdit及QSpinBox
        grid = QGridLayout()
        grid.addWidget(QLabel(u'姓名', parent=self), 0, 0, 1, 1)
        self.leName = QLineEdit(parent=self)
        grid.addWidget(self.leName, 0, 1, 1, 1)
        grid.addWidget(QLabel(u'年龄', parent=self), 1, 0, 1, 1)
        self.sbAge = QSpinBox(parent=self)
        grid.addWidget(self.sbAge, 1, 1, 1, 1)
        #创建ButtonBox，用户确定和取消
        buttonBox = QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal) # 设置为水平方向
        buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok) # 确定和取消两个按钮
        #连接信号和槽
        buttonBox.accepted.connect(self.accept) # 确定
        buttonBox.rejected.connect(self.reject) # 取消
        #垂直布局，布局表格及按钮
        layout = QVBoxLayout()
        #加入前面创建的表格布局
        layout.addLayout(grid)
        #放一个间隔对象美化布局
        spacerItem = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        #ButtonBox
        layout.addWidget(buttonBox)
        self.setLayout(layout)
    def name(self):
        return self.leName.text()
    def age(self):
        return self.sbAge.value()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
