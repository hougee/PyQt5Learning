#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：窗体操作相关功能：无边框、背景透明、添加按钮、重写最小化按钮、重写关闭按钮、窗体拖拽'

__author__ = 'HouBin'

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import  QMouseEvent,QCursor
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget,QVBoxLayout,QPushButton,QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置窗体无边框和总是在最前面显示
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        # 设置背景透明
        #self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.resize(400, 200)        
        self.status=self.statusBar()
        #设置状态栏
        self.status.showMessage("这是状态栏提示", 5000)
        #设置窗口标题
        self.setWindowTitle("这是MainWindow的例子")
        #设置窗口在整个屏幕居中
        self.center()
        #垂直布局
        layout = QVBoxLayout()
        
        #添加最小化按钮
        self.btn1 = QPushButton("最小化")
        self.btn1.setCheckable(True)
        self.btn1.setObjectName("btn1")
        self.btn1.toggle()
        #按钮1添加到布局
        layout.addWidget(self.btn1)
        #关联最小化窗口功能
        self.btn1.clicked.connect(self.showMinimized)
        
        #添加关闭按钮
        self.btn2 = QPushButton("关闭")
        #self.btn2.setCheckable(True)
        self.btn2.setObjectName("btn2")
        #self.btn2.toggle()
        #按钮2添加到布局
        layout.addWidget(self.btn2)
        #关联关闭窗口功能
        self.btn2.clicked.connect(self.close)
        
        #创建widget窗口实例
        centralwidget=QWidget()
        #加载布局
        centralwidget.setLayout(layout)
        #把widget窗口加载到主窗口的中央位置
        self.setCentralWidget(centralwidget)
    #定义窗口居中函数
    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
    #重写鼠标按下函数（实现窗体拖拽第1步）
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
    #重写鼠标移动函数（实现窗体拖拽第2步）
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
    #重写鼠标抬起函数（实现窗体拖拽第3步）
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

if __name__=="__main__":
    app=QApplication(sys.argv)
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())
