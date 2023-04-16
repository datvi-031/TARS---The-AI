from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
import random

class Ui_MainWindow(object):
    def __init__(self):
       super().__init__()
       self.clicked_values = []

    def cell_constraints(self, styleSheet, cellName, cell):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(cell.sizePolicy().hasHeightForWidth())
        cell.setSizePolicy(sizePolicy)
        cell.setMinimumSize(QtCore.QSize(100, 100))
        cell.setStyleSheet(styleSheet)
        cell.setText("")
        cell.setObjectName(cellName)

    def grid_one(self):
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 351, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_top_10 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_top_10.setContentsMargins(0, 0, 0, 0)
        self.grid_top_10.setObjectName("grid_top_10")

        self.cell = [0 for _ in range(9)]
        self.cellName = ["cell_1", "cell_2", "cell_3", "cell_4", "cell_5", "cell_6", "cell_7", "cell_8", "cell_9"]
        self.styleSheet = "border : 2px solid rgb(47, 218, 190);"
        for x in range(9):
            self.cell[x] = QtWidgets.QPushButton(self.gridLayoutWidget)
            self.cell_constraints(self.styleSheet, self.cellName[x], self.cell[x])
            self.grid_top_10.addWidget(self.cell[x], x//3, x%3, 1, 1)

        return self.cell, self.cellName

    def grid_two(self):
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(380, 40, 351, 321))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.grid_top_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_top_13.setContentsMargins(0, 0, 0, 0)
        self.grid_top_13.setObjectName("grid_top_13")

        self.cell = [0 for _ in range(9)]
        self.cellName = ["cell_10", "cell_11", "cell_12", "cell_13", "cell_14", "cell_15", "cell_16", "cell_17", "cell_18"]
        self.styleSheet = "border : 2px solid rgb(237, 245, 13);"
        for x in range(9):
            self.cell[x] = QtWidgets.QPushButton(self.gridLayoutWidget_2)
            self.cell_constraints(self.styleSheet, self.cellName[x], self.cell[x])
            self.grid_top_13.addWidget(self.cell[x], x//3, x%3, 1, 1)

        return self.cell, self.cellName

    def grid_three(self):
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(750, 40, 351, 321))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.grid_top_16 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.grid_top_16.setContentsMargins(0, 0, 0, 0)
        self.grid_top_16.setObjectName("grid_top_16")

        self.cell = [0 for _ in range(9)]
        self.cellName = ["cell_19", "cell_20", "cell_21", "cell_22", "cell_23", "cell_24", "cell_25", "cell_26", "cell_27"]
        self.styleSheet = "border : 2px solid rgb(252, 37, 37);"
        for x in range(9):
            self.cell[x] = QtWidgets.QPushButton(self.gridLayoutWidget_3)
            self.cell_constraints(self.styleSheet, self.cellName[x], self.cell[x])
            self.grid_top_16.addWidget(self.cell[x], x//3, x%3, 1, 1)

        return self.cell, self.cellName

    def grid_four(self):
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 370, 351, 321))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.grid_top_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.grid_top_12.setContentsMargins(0, 0, 0, 0)
        self.grid_top_12.setObjectName("grid_top_12")

        self.cell = [0 for _ in range(9)]
        self.cellName = ["cell_1", "cell_2", "cell_3", "cell_10", "cell_11", "cell_12", "cell_19", "cell_20", "cell_21"]
        self.styleSheet = "border : 2px solid rgb(239, 68, 68);"
        for x in range(9):
            self.cell[x] = QtWidgets.QPushButton(self.gridLayoutWidget_4)
            self.cell_constraints(self.styleSheet, self.cellName[x], self.cell[x])
            self.grid_top_12.addWidget(self.cell[x], x//3, x%3, 1, 1)

        return self.cell, self.cellName

    def grid_five(self):
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(380, 370, 351, 321))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.grid_top_17 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.grid_top_17.setContentsMargins(0, 0, 0, 0)
        self.grid_top_17.setObjectName("grid_top_17")

        self.cell = [0 for _ in range(9)]
        self.cellName = ["cell_4", "cell_5", "cell_6", "cell_13", "cell_14", "cell_15", "cell_22", "cell_23", "cell_24"]
        self.styleSheet = "border : 2px solid white;"
        for x in range(9):
            self.cell[x] = QtWidgets.QPushButton(self.gridLayoutWidget_5)
            self.cell_constraints(self.styleSheet, self.cellName[x], self.cell[x])
            self.grid_top_17.addWidget(self.cell[x], x//3, x%3, 1, 1)

        return self.cell, self.cellName

    def grid_six(self):
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(750, 370, 351, 321))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.grid_top_14 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.grid_top_14.setContentsMargins(0, 0, 0, 0)
        self.grid_top_14.setObjectName("grid_top_14")

        self.cell = [0 for _ in range(9)]
        self.cellName = ["cell_7", "cell_8", "cell_9", "cell_16", "cell_17", "cell_18", "cell_25", "cell_26", "cell_27"]
        self.styleSheet = "border : 2px solid blue;"
        for x in range(9):
            self.cell[x] = QtWidgets.QPushButton(self.gridLayoutWidget_6)
            self.cell_constraints(self.styleSheet, self.cellName[x], self.cell[x])
            self.grid_top_14.addWidget(self.cell[x], x//3, x%3, 1, 1)

        return self.cell, self.cellName

    def grid_seven(self):
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(10, 700, 351, 316))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.grid_top_15 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.grid_top_15.setContentsMargins(0, 0, 0, 0)
        self.grid_top_15.setObjectName("grid_top_15")

        self.cell = [0 for _ in range(9)]
        self.cellName = ["cell_1", "cell_10", "cell_19", "cell_4", "cell_13", "cell_22", "cell_7", "cell_16", "cell_25"]
        self.styleSheet = "border : 2px solid rgb(228, 45, 235);"
        for x in range(9):
            self.cell[x] = QtWidgets.QPushButton(self.gridLayoutWidget_7)
            self.cell_constraints(self.styleSheet, self.cellName[x], self.cell[x])
            self.grid_top_15.addWidget(self.cell[x], x//3, x%3, 1, 1)

        return self.cell, self.cellName

    def grid_eight(self):
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(380, 700, 351, 316))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.grid_top_1 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.grid_top_1.setContentsMargins(0, 0, 0, 0)
        self.grid_top_1.setObjectName("grid_top_1")
        
        self.cell = [0 for _ in range(9)]
        self.cellName = ["cell_2", "cell_11", "cell_20", "cell_5", "cell_14", "cell_23", "cell_8", "cell_17", "cell_26"]
        self.styleSheet = "border : 2px solid rgb(255, 147, 27);"
        for x in range(9):
            self.cell[x] = QtWidgets.QPushButton(self.gridLayoutWidget_8)
            self.cell_constraints(self.styleSheet, self.cellName[x], self.cell[x])
            self.grid_top_1.addWidget(self.cell[x], x//3, x%3, 1, 1)

        return self.cell, self.cellName

    def grid_nine(self):
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(750, 700, 351, 316))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.grid_top_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.grid_top_11.setContentsMargins(0, 0, 0, 0)
        self.grid_top_11.setObjectName("grid_top_11")

        self.cell = [0 for _ in range(9)]
        self.cellName = ["cell_3", "cell_12", "cell_21", "cell_6", "cell_15", "cell_24", "cell_9", "cell_18", "cell_27"]
        self.styleSheet = "border : 2px solid rgb(146, 255, 7);"
        for x in range(9):
            self.cell[x] = QtWidgets.QPushButton(self.gridLayoutWidget_9)
            self.cell_constraints(self.styleSheet, self.cellName[x], self.cell[x])
            self.grid_top_11.addWidget(self.cell[x], x//3, x%3, 1, 1)

        return self.cell, self.cellName

    def changeLabel(self, button):
        self.label = QLabel(button)
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.label)
        h_layout.addStretch()

        v_layout = QtWidgets.QVBoxLayout()
        v_layout.addStretch()
        v_layout.addLayout(h_layout)
        v_layout.addStretch()

        # Set the layout on the button
        button.setLayout(v_layout)
        self.label.setText("O")
        self.label.setStyleSheet("font-size: 50px; border: none; color: blue;")
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)

    def change_background_ai(self, x, y, z):
        self.button_ai_seleceted_style = "background-color: #00308F;"
        if x == 0:
            if y == 0:
                if z == 0:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_1")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                elif z == 1:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_2")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                else:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_3")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
            elif y == 1:
                if z == 0:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_4")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                elif z == 1:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_5")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                else:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_6")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
            else:
                if z == 0:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_7")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                elif z == 1:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_8")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                else:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_9")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
        elif x == 1:
            if y == 0:
                if z == 0:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_10")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                elif z == 1:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_11")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                else:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_12")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
            elif y == 1:
                if z == 0:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_13")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                elif z == 1:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_14")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                else:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_15")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
            else:
                if z == 0:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_16")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                elif z == 1:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_17")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                else:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_18")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
        else:
            if y == 0:
                if z == 0:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_19")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                elif z == 1:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_20")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                else:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_21")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
            elif y == 1:
                if z == 0:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_22")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                elif z == 1:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_23")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                else:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_24")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
            else:
                if z == 0:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_25")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                elif z == 1:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_26")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)
                else:
                    buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, "cell_27")
                    for button in buttons:
                        self.changeLabel(button)
                        button.setEnabled(False)

    def clickButtons(self, ai):
        self.gridOne[0][0].clicked.connect(lambda : self.change_background(self.gridOne[0][0], ai))
        self.gridOne[0][1].clicked.connect(lambda : self.change_background(self.gridOne[0][1], ai))
        self.gridOne[0][2].clicked.connect(lambda : self.change_background(self.gridOne[0][2], ai))
        self.gridOne[0][3].clicked.connect(lambda : self.change_background(self.gridOne[0][3], ai))
        self.gridOne[0][4].clicked.connect(lambda : self.change_background(self.gridOne[0][4], ai))
        self.gridOne[0][5].clicked.connect(lambda : self.change_background(self.gridOne[0][5], ai))
        self.gridOne[0][6].clicked.connect(lambda : self.change_background(self.gridOne[0][6], ai))
        self.gridOne[0][7].clicked.connect(lambda : self.change_background(self.gridOne[0][7], ai))
        self.gridOne[0][8].clicked.connect(lambda : self.change_background(self.gridOne[0][8], ai))

        self.gridTwo[0][0].clicked.connect(lambda : self.change_background(self.gridTwo[0][0], ai))
        self.gridTwo[0][1].clicked.connect(lambda : self.change_background(self.gridTwo[0][1], ai))
        self.gridTwo[0][2].clicked.connect(lambda : self.change_background(self.gridTwo[0][2], ai))
        self.gridTwo[0][3].clicked.connect(lambda : self.change_background(self.gridTwo[0][3], ai))
        self.gridTwo[0][4].clicked.connect(lambda : self.change_background(self.gridTwo[0][4], ai))
        self.gridTwo[0][5].clicked.connect(lambda : self.change_background(self.gridTwo[0][5], ai))
        self.gridTwo[0][6].clicked.connect(lambda : self.change_background(self.gridTwo[0][6], ai))
        self.gridTwo[0][7].clicked.connect(lambda : self.change_background(self.gridTwo[0][7], ai))
        self.gridTwo[0][8].clicked.connect(lambda : self.change_background(self.gridTwo[0][8], ai))

        self.gridThree[0][0].clicked.connect(lambda : self.change_background(self.gridThree[0][0], ai))
        self.gridThree[0][1].clicked.connect(lambda : self.change_background(self.gridThree[0][1], ai))
        self.gridThree[0][2].clicked.connect(lambda : self.change_background(self.gridThree[0][2], ai))
        self.gridThree[0][3].clicked.connect(lambda : self.change_background(self.gridThree[0][3], ai))
        self.gridThree[0][4].clicked.connect(lambda : self.change_background(self.gridThree[0][4], ai))
        self.gridThree[0][5].clicked.connect(lambda : self.change_background(self.gridThree[0][5], ai))
        self.gridThree[0][6].clicked.connect(lambda : self.change_background(self.gridThree[0][6], ai))
        self.gridThree[0][7].clicked.connect(lambda : self.change_background(self.gridThree[0][7], ai))
        self.gridThree[0][8].clicked.connect(lambda : self.change_background(self.gridThree[0][8], ai))

        self.gridFour[0][0].clicked.connect(lambda : self.change_background(self.gridFour[0][0], ai))
        self.gridFour[0][1].clicked.connect(lambda : self.change_background(self.gridFour[0][1], ai))
        self.gridFour[0][2].clicked.connect(lambda : self.change_background(self.gridFour[0][2], ai))
        self.gridFour[0][3].clicked.connect(lambda : self.change_background(self.gridFour[0][3], ai))
        self.gridFour[0][4].clicked.connect(lambda : self.change_background(self.gridFour[0][4], ai))
        self.gridFour[0][5].clicked.connect(lambda : self.change_background(self.gridFour[0][5], ai))
        self.gridFour[0][6].clicked.connect(lambda : self.change_background(self.gridFour[0][6], ai))
        self.gridFour[0][7].clicked.connect(lambda : self.change_background(self.gridFour[0][7], ai))
        self.gridFour[0][8].clicked.connect(lambda : self.change_background(self.gridFour[0][8], ai))

        self.gridFive[0][0].clicked.connect(lambda : self.change_background(self.gridFive[0][0], ai))
        self.gridFive[0][1].clicked.connect(lambda : self.change_background(self.gridFive[0][1], ai))
        self.gridFive[0][2].clicked.connect(lambda : self.change_background(self.gridFive[0][2], ai))
        self.gridFive[0][3].clicked.connect(lambda : self.change_background(self.gridFive[0][3], ai))
        self.gridFive[0][4].clicked.connect(lambda : self.change_background(self.gridFive[0][4], ai))
        self.gridFive[0][5].clicked.connect(lambda : self.change_background(self.gridFive[0][5], ai))
        self.gridFive[0][6].clicked.connect(lambda : self.change_background(self.gridFive[0][6], ai))
        self.gridFive[0][7].clicked.connect(lambda : self.change_background(self.gridFive[0][7], ai))
        self.gridFive[0][8].clicked.connect(lambda : self.change_background(self.gridFive[0][8], ai))

        self.gridSix[0][0].clicked.connect(lambda : self.change_background(self.gridSix[0][0], ai))
        self.gridSix[0][1].clicked.connect(lambda : self.change_background(self.gridSix[0][1], ai))
        self.gridSix[0][2].clicked.connect(lambda : self.change_background(self.gridSix[0][2], ai))
        self.gridSix[0][3].clicked.connect(lambda : self.change_background(self.gridSix[0][3], ai))
        self.gridSix[0][4].clicked.connect(lambda : self.change_background(self.gridSix[0][4], ai))
        self.gridSix[0][5].clicked.connect(lambda : self.change_background(self.gridSix[0][5], ai))
        self.gridSix[0][6].clicked.connect(lambda : self.change_background(self.gridSix[0][6], ai))
        self.gridSix[0][7].clicked.connect(lambda : self.change_background(self.gridSix[0][7], ai))
        self.gridSix[0][8].clicked.connect(lambda : self.change_background(self.gridSix[0][8], ai))

        self.gridSeven[0][0].clicked.connect(lambda : self.change_background(self.gridSeven[0][0], ai))
        self.gridSeven[0][1].clicked.connect(lambda : self.change_background(self.gridSeven[0][1], ai))
        self.gridSeven[0][2].clicked.connect(lambda : self.change_background(self.gridSeven[0][2], ai))
        self.gridSeven[0][3].clicked.connect(lambda : self.change_background(self.gridSeven[0][3], ai))
        self.gridSeven[0][4].clicked.connect(lambda : self.change_background(self.gridSeven[0][4], ai))
        self.gridSeven[0][5].clicked.connect(lambda : self.change_background(self.gridSeven[0][5], ai))
        self.gridSeven[0][6].clicked.connect(lambda : self.change_background(self.gridSeven[0][6], ai))
        self.gridSeven[0][7].clicked.connect(lambda : self.change_background(self.gridSeven[0][7], ai))
        self.gridSeven[0][8].clicked.connect(lambda : self.change_background(self.gridSeven[0][8], ai))

        self.gridEight[0][0].clicked.connect(lambda : self.change_background(self.gridEight[0][0], ai))
        self.gridEight[0][1].clicked.connect(lambda : self.change_background(self.gridEight[0][1], ai))
        self.gridEight[0][2].clicked.connect(lambda : self.change_background(self.gridEight[0][2], ai))
        self.gridEight[0][3].clicked.connect(lambda : self.change_background(self.gridEight[0][3], ai))
        self.gridEight[0][4].clicked.connect(lambda : self.change_background(self.gridEight[0][4], ai))
        self.gridEight[0][5].clicked.connect(lambda : self.change_background(self.gridEight[0][5], ai))
        self.gridEight[0][6].clicked.connect(lambda : self.change_background(self.gridEight[0][6], ai))
        self.gridEight[0][7].clicked.connect(lambda : self.change_background(self.gridEight[0][7], ai))
        self.gridEight[0][8].clicked.connect(lambda : self.change_background(self.gridEight[0][8], ai))

        self.gridNine[0][0].clicked.connect(lambda : self.change_background(self.gridNine[0][0], ai))
        self.gridNine[0][1].clicked.connect(lambda : self.change_background(self.gridNine[0][1], ai))
        self.gridNine[0][2].clicked.connect(lambda : self.change_background(self.gridNine[0][2], ai))
        self.gridNine[0][3].clicked.connect(lambda : self.change_background(self.gridNine[0][3], ai))
        self.gridNine[0][4].clicked.connect(lambda : self.change_background(self.gridNine[0][4], ai))
        self.gridNine[0][5].clicked.connect(lambda : self.change_background(self.gridNine[0][5], ai))
        self.gridNine[0][6].clicked.connect(lambda : self.change_background(self.gridNine[0][6], ai))
        self.gridNine[0][7].clicked.connect(lambda : self.change_background(self.gridNine[0][7], ai))
        self.gridNine[0][8].clicked.connect(lambda : self.change_background(self.gridNine[0][8], ai))

    def get_indices(self, objName):
        if objName == "cell_1":
            self.x, self.y, self.z = 0, 0, 0
        elif objName == "cell_2":
            self.x, self.y, self.z = 0, 0, 1
        elif objName == "cell_3":
            self.x, self.y, self.z = 0, 0, 2
        elif objName == "cell_4":
            self.x, self.y, self.z = 0, 1, 0
        elif objName == "cell_5":
            self.x, self.y, self.z = 0, 1, 1
        elif objName == "cell_6":
            self.x, self.y, self.z = 0, 1, 2
        elif objName == "cell_7":
            self.x, self.y, self.z = 0, 2, 0
        elif objName == "cell_8":
            self.x, self.y, self.z = 0, 2, 1
        elif objName == "cell_9":
            self.x, self.y, self.z = 0, 2, 2
        elif objName == "cell_10":
            self.x, self.y, self.z = 1, 0, 0
        elif objName == "cell_11":
            self.x, self.y, self.z = 1, 0, 1
        elif objName == "cell_12":
            self.x, self.y, self.z = 1, 0, 2
        elif objName == "cell_13":
            self.x, self.y, self.z = 1, 1, 0
        elif objName == "cell_14":
            self.x, self.y, self.z = 1, 1, 1
        elif objName == "cell_15":
            self.x, self.y, self.z = 1, 1, 2
        elif objName == "cell_16":
            self.x, self.y, self.z = 1, 2, 0
        elif objName == "cell_17":
            self.x, self.y, self.z = 1, 2, 1
        elif objName == "cell_18":
            self.x, self.y, self.z = 1, 2, 2
        elif objName == "cell_19":
            self.x, self.y, self.z = 2, 0, 0
        elif objName == "cell_20":
            self.x, self.y, self.z = 2, 0, 1
        elif objName == "cell_21":
            self.x, self.y, self.z = 2, 0, 2
        elif objName == "cell_22":
            self.x, self.y, self.z = 2, 1, 0
        elif objName == "cell_23":
            self.x, self.y, self.z = 2, 1, 1
        elif objName == "cell_24":
            self.x, self.y, self.z = 2, 1, 2
        elif objName == "cell_25":
            self.x, self.y, self.z = 2, 2, 0
        elif objName == "cell_26":
            self.x, self.y, self.z = 2, 2, 1
        elif objName == "cell_27":
            self.x, self.y, self.z = 2, 2, 2
        return self.x, self.y, self.z

    def setupUi(self, MainWindow):
        ai = Tic_tac_toe()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1889, 1075)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1150, 520, 721, 181))
        self.groupBox.setStyleSheet("")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1150, 30, 721, 441))
        self.groupBox_2.setStyleSheet("")

        # self.groupBox_2.setTitle("Instructions")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 70, 392, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 381, 23))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 240, 391, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(30, 200, 381, 23))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(30, 380, 411, 23))
        self.label_11.setObjectName("label_11")
        
        
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1150, 760, 721, 241))

        # self.groupBox_3.setTitle("Message from TARS")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(70, 100, 521, 51))
        self.label_12.setStyleSheet("font-size : 30px;")
        self.label_12.setObjectName("label_12")
        

        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(0, -20, 1121, 1061))
        self.groupBox_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")

        self.gridEight = list(self.grid_eight())
        self.gridThree = list(self.grid_three())
        self.gridNine = list(self.grid_nine())
        self.gridOne = list(self.grid_one())
        self.gridFour = list(self.grid_four())
        self.gridFive = list(self.grid_five())
        self.gridSeven = list(self.grid_seven())
        self.gridSix = list(self.grid_six())
        self.gridTwo = list(self.grid_two())

        self.disable_grid(self.gridTwo[0])
        self.disable_grid(self.gridSix[0])
        self.disable_grid(self.gridSeven[0])
        self.disable_grid(self.gridFive[0])
        self.disable_grid(self.gridOne[0])
        self.disable_grid(self.gridFour[0])
        self.disable_grid(self.gridNine[0])
        self.disable_grid(self.gridEight[0])
        self.disable_grid(self.gridThree[0])

        # USER INFORMATION
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(20, 20, 516, 141))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_10)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_10)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_10)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_10)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        # submit button
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_10)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        # reset button
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_10)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)

        cells_lst = [self.gridOne[0], self.gridTwo[0], self.gridThree[0], self.gridFour[0], self.gridFive[0], self.gridSix[0], self.gridSeven[0], self.gridEight[0], self.gridNine[0]]
        self.clickButtons(ai)

        # action on submit button
        self.pushButton.clicked.connect(lambda : self.submit_form(ai, cells_lst, self.label_12))

        # action on reset button
        # self.pushButton.clicked.connect(lambda : self.reset_form(ai, cells_lst))


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def disable_grid(self, cells):
        for cell in cells:
            cell.setEnabled(False)
            cell.setStyleSheet("border: 1px solid white")

    def change_background(self, sender, ai):
        self.x = self.y = self.z = -1
        objName = sender.objectName()

        buttons = self.centralwidget.findChildren(QtWidgets.QPushButton, objName)
        for button in buttons:
            self.label = QLabel(button)
            h_layout = QtWidgets.QHBoxLayout()
            h_layout.addStretch()
            h_layout.addWidget(self.label)
            h_layout.addStretch()

            v_layout = QtWidgets.QVBoxLayout()
            v_layout.addStretch()
            v_layout.addLayout(h_layout)
            v_layout.addStretch()

            # Set the layout on the button
            button.setLayout(v_layout)
            self.label.setText("X")
            self.label.setStyleSheet("font-size: 50px; border: none; color: white;")
            self.label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.label.setAlignment(Qt.AlignCenter)

            button.setEnabled(False)

        x, y, z = self.get_indices(objName)
        print("x: {}, y = {}, z = {}".format(x, y, z))

        # FEED x, y, z TO THE AI ALGORITHM
        ai.user(x, y, z)
        
        # GET THE DATA FROM AI ALGORITHM AND CALL THE FUNCTION change_background_ai();
        tup = ai.pc()
        if tup[0] == -1 and tup[1] == -1 and tup[2] == -1:
            return
        self.change_background_ai(tup[0], tup[1], tup[2])

    def enable_board(self, cells_lst):
        cnt = 0
        for grid in cells_lst:
            cnt+=1
            for cell in grid:
                if cnt == 1:
                    cell.setStyleSheet("border : 2px solid rgb(47, 218, 190);")
                elif cnt == 2:
                    cell.setStyleSheet("border : 2px solid rgb(237, 245, 13);")
                elif cnt == 3:
                    cell.setStyleSheet("border : 2px solid rgb(252, 37, 37);")
                elif cnt == 4:
                    cell.setStyleSheet("border : 2px solid rgb(239, 68, 68);")
                elif cnt == 5:
                    cell.setStyleSheet("border : 2px solid white;")
                elif cnt == 6:
                    cell.setStyleSheet("border : 2px solid blue;")
                elif cnt == 7:
                    cell.setStyleSheet("border : 2px solid rgb(228, 45, 235);")
                elif cnt == 8:
                    cell.setStyleSheet("border : 2px solid rgb(255, 147, 27);")
                elif cnt == 9:
                    cell.setStyleSheet("border : 2px solid rgb(146, 255, 7);")
                cell.setEnabled(True)

    def submit_form(self, ai, cells_lst, label):
        name = self.lineEdit.text()
        selection = self.comboBox.currentText()
        print("Name: {}".format(name))
        print("selection:..{}".format(selection))

        if name == "":
            return
        self.enable_board(cells_lst) 
        if selection != "  you":
            tup = ai.choice(2)
            if len(tup) == 4:
                self.change_background_ai(tup[0], tup[1], tup[2])
                return
            self.change_background_ai(tup[0], tup[1], tup[2])
            label.setText("Hello {}, its Your Turn now".format(name))
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "        Name        "))
        self.comboBox.setItemText(0, _translate("MainWindow", " TARS (The Artificial Intelligence)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "  you"))
        self.label_2.setText(_translate("MainWindow", "          First"))
        self.pushButton.setText(_translate("MainWindow", "Play"))
        self.pushButton_2.setText(_translate("MainWindow", "reset"))
        self.label_5.setText(_translate("MainWindow", "1.   Enter your name."))
        self.label_6.setText(_translate("MainWindow", "2.   Select who is going to start the game."))
        self.label_4.setText(_translate("MainWindow", "3.   Board Enables when you do 1, 2"))
        self.label_3.setText(_translate("MainWindow", "Hello, You are playing with TARS (The AI)"))
        self.label_7.setText(_translate("MainWindow", "1.   Make a diagonal."))
        self.label_8.setText(_translate("MainWindow", "2.   Make a row."))
        self.label_9.setText(_translate("MainWindow", "3.   Make a column."))
        self.label_10.setText(_translate("MainWindow", "You are the winner  if you can"))
        self.label_11.setText(_translate("MainWindow", "In any of identically colored  [ 3 x 3 ] Squares"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Message from TARS (Artificial Intelligence)"))
        self.label_12.setText(_translate("MainWindow", "Hello Name, Its Your Turn NOW"))

class Tic_tac_toe:
    def __init__(self):
        self.board = [[['*' for k in range(3)] for j in range(3)] for i in range(3)]
        self.moves = 0
        # choice = int(input("User Start the game: 1\nComputer Start the game: 2\n\nYour Choice:  "))
        self.stop = False
    
    def choice(self, choice):
        if(choice == 1):
            self.user()
        else:
            return self.pc()
    
    def print_board(self):
        print("Layer1: ")
        for y in range(0,3):
            for z in range(0,3):
                print(self.board[0][y][z],end=" ")
            print("",end="\n")
        print("Layer2: ")
        for y in range(0,3):
            for z in range(0,3):
                print(self.board[1][y][z],end=" ")
            print("",end="\n")
        print("Layer3: ")
        for y in range(0,3):
            for z in range(0,3):
                print(self.board[2][y][z],end=" ")
            print("",end="\n") 

    def print_tboard(self):
        print("Layer1: ")
        for y in range(0,3):
            for z in range(0,3):
                print(self.tboard[0][y][z],end=" ")
            print("",end="\n")

    def check_won(self,ch,cboard):
        # Two dimensional wins
        for x in range(0,3):
            for y in range(0,3):
                cnt = 0
                for z in range(0,3):
                    if cboard[x][y][z] == ch:
                        cnt+=1
                if(cnt == 3):
                    return True
            for z in range(0,3):
                cnt = 0
                for y in range(0,3):
                    if cboard[x][y][z] == ch:
                        cnt+=1
                if(cnt == 3):
                    return True
            cnt = 0
            for yz in range(0,3):
                if cboard[x][yz][yz] == ch:
                    cnt+=1
            if cnt==3:
                return True

            y = 2;z = 0;cnt = 0;
            for i in range(0,3):
                if cboard[x][y][z] == ch:
                    cnt+=1
                y -= 1
                z += 1
            if cnt==3:
                return True

        #Face Diagonal Wins
        if cboard[0][0][0] == ch and cboard[0][1][1] == ch and cboard[0][2][2] == ch:
            return True
        if cboard[1][0][0] == ch and cboard[1][1][1] == ch and cboard[1][2][2] == ch:
            return True
        if cboard[2][0][0] == ch and cboard[2][1][1] == ch and cboard[2][2][2] == ch:
            return True
        if cboard[0][2][0] == ch and cboard[0][1][1] == ch and cboard[0][0][2] == ch:
            return True
        if cboard[1][2][0] == ch and cboard[1][1][1] == ch and cboard[1][0][2] == ch:
            return True
        if cboard[2][2][0] == ch and cboard[2][1][1] == ch and cboard[2][0][2] == ch:
            return True
        if cboard[0][2][0] == ch and cboard[1][1][0] == ch and cboard[2][0][0] == ch:
            return True
        if cboard[0][2][1] == ch and cboard[1][1][1] == ch and cboard[2][0][1] == ch:
            return True
        if cboard[0][2][2] == ch and cboard[1][1][2] == ch and cboard[2][0][2] == ch:
            return True
        if cboard[0][0][0] == ch and cboard[1][1][0] == ch and cboard[2][2][0] == ch:
            return True
        if cboard[0][0][1] == ch and cboard[1][1][1] == ch and cboard[2][2][1] == ch:
            return True
        if cboard[0][0][2] == ch and cboard[1][1][2] == ch and cboard[2][2][2] == ch:
            return True

        #Main Diagonal Wins
        if cboard[1][1][1] != ch:
            return False
        if cboard[0][0][0] == ch and cboard[2][2][2] == ch:
            return True
        if cboard[0][0][2] == ch and cboard[2][2][0] == ch:
            return True
        if cboard[2][0][0] == ch and cboard[0][2][2] == ch:
            return True
        if cboard[2][0][2] == ch and cboard[0][2][0] == ch:
            return True
            
        return False

    def check_moves_left(self,cboard):
        # for i in range(0,3):
        i = 0
        for j in range(0,3):
            for k in range(0,3):
                if cboard[i][j][k] == '*':
                    return False
        return True

    def user(self, x, y, z):
        if self.moves == 9:
            print("Game Ended in Draw!")
            self.stop = True
            return
        
        self.board[x][y][z] = 'x'
        self.moves += 1
        self.print_board()
        result = self.check_won('x',self.board)
        if result == True:
            print("Congratulations! You won the game.")
            self.stop = True
            return

    def max_node(self,minimal):
        result = self.check_won('x', self.tboard)
        if result == True:
            return -1
        no_moves = self.check_moves_left(self.tboard)
        if no_moves == True:
            return 0
        maximal = -1000
        # for i in range(0,3):
        i = 0
        for j in range(0,3):
            for k in range(0,3):
                if maximal>=minimal:
                    print("AB pruning")
                    return minimal
                if self.tboard[i][j][k] == '*':
                    self.tboard[i][j][k] = 'o'
                    cval = self.min_node(maximal)
                    if cval > maximal:
                        maximal = cval
                        print("maximal = {}, minimal = {}".format(maximal,minimal))
                    self.tboard[i][j][k] = '*'
        return maximal

    def min_node(self,maximal):
        result = self.check_won('o',self.tboard)
        if result == True:
            return 1
        no_moves = self.check_moves_left(self.tboard)
        if no_moves == True:
            return 0
        minimal = 1000
        # for i in range(0,3):
        i = 0
        for j in range(0,3):
            for k in range(0,3):
                if minimal<=maximal:
                    print("AB pruning");
                    return maximal
                if self.tboard[i][j][k] == '*':
                    self.tboard[i][j][k] = 'x'
                    cval = self.max_node(minimal)
                    if cval < minimal:
                        minimal = cval
                    self.tboard[i][j][k] = '*'
        return minimal

    def evaluate(self):
        x = -1;y = -1;z = -1;
        
        self.tboard = [[['*' for k in range(3)] for j in range(3)] for i in range(3)]

        for i in range(0,3):
            for j in range(0,3):
                for k in range(0,3):
                    self.tboard[i][j][k] = self.board[i][j][k]

        maximal = -1000
        # for i in range(0,3):
        i = 0
        for j in range(0,3):
            for k in range(0,3):
                if self.tboard[i][j][k] == '*':
                    self.tboard[i][j][k] = 'o'
                    cval = self.min_node(maximal)
                    if cval > maximal:
                        x = i;y = j;z = k;
                        maximal = cval
                    self.tboard[i][j][k] = '*'

        return x,y,z

    def pc(self):
        if self.moves == 9:
            print("Game Ended in Draw!")
            self.stop = True
            return -1, -1, -1
        x,y,z = self.evaluate()
        self.board[x][y][z] = 'o'
        self.moves += 1
        self.print_board()
        result = self.check_won('o',self.board)
        if result == True:
            print("Computer has won the game.")
            self.stop = True
            return x, y, z, True
        return x, y, z

    def turn(self,ispc):
        if ispc == True:
            self.pc()
        while True:
            if self.stop == True:
                break
            self.user()
            if self.stop == True:
                break
            self.pc()
        pass 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
