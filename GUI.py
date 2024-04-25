import Graph
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys
from pyqtgraph import PlotWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget


graph_1 = None

class RawSignalWidget(PlotWidget):
    def __init__(self):
        super().__init__() 

    def mouseDoubleClickEvent(self, event):
              graph_1.Browse_Signals()


class GUI(object):
        def __init__(self): 
                # of the plot widget of the Top Graph.
                self.Graph_1 = Graph.Graph(1, self, None)
                self.Graph_2 = Graph.Graph(2, self, None)
                # Every graph has to be able to access the other one as they can be Linked
                self.Graph_1.Other_Graph = self.Graph_2
                self.Graph_2.Other_Graph = self.Graph_1
                
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1055, 971)
                MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
                MainWindow.setStyleSheet(" background-repeat: no-repeat;\n"
                "/*background-image: url(C://Users//Ahmed Taha//Downloads//background.png);*/\n"
                "background-size: contain;\n"
                "background-color: #1e1e2f;")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setStyleSheet("background-repeat: no-repeat;\n"
                "background-position: center;\n"
                "background-size: contain;")
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout.setObjectName("gridLayout")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_4.addItem(spacerItem)
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                font = QtGui.QFont()
                font.setPointSize(33)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("color: white;\n"
                "background-image:white;")
                self.label_3.setObjectName("label_3")
                self.horizontalLayout_4.addWidget(self.label_3)
                spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_4.addItem(spacerItem1)
                self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
                self.Signals = QtWidgets.QGroupBox(self.centralwidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.Signals.sizePolicy().hasHeightForWidth())
                self.Signals.setSizePolicy(sizePolicy)
                self.Signals.setMinimumSize(QtCore.QSize(0, 488))
                self.Signals.setStyleSheet("border: 1.2px solid white;\n"
                "border-radius: 15px;\n"
                "border-style: outset;\n"
                "border-radius: 15px;")
                self.Signals.setObjectName("Signals")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.Signals)
                self.verticalLayout.setObjectName("verticalLayout")
                self.horizontalLayout = QtWidgets.QHBoxLayout()
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.label_2 = QtWidgets.QLabel(self.Signals)
                font = QtGui.QFont()
                font.setPointSize(19)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("color: rgb(255, 255, 255); border:none;")
                self.label_2.setObjectName("label_2")
                self.horizontalLayout.addWidget(self.label_2)
                spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout.addItem(spacerItem2)
                self.verticalLayout.addLayout(self.horizontalLayout)
                self.RawSignal = RawSignalWidget()
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.RawSignal.sizePolicy().hasHeightForWidth())
                self.RawSignal.setSizePolicy(sizePolicy)
                self.RawSignal.setMinimumSize(QtCore.QSize(0, 161))
                self.RawSignal.setStyleSheet("border: none;")
                self.RawSignal.setObjectName("RawSignal")
                #self.RawSignal.plot_widget.mouseDoubleClickEvent = self.Graph_1.Browse_Signals()
                self.verticalLayout.addWidget(self.RawSignal)
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.label = QtWidgets.QLabel(self.Signals)
                font = QtGui.QFont()
                font.setPointSize(19)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setStyleSheet("color: rgb(255, 255, 255); border:none;")
                self.label.setObjectName("label")
                self.horizontalLayout_2.addWidget(self.label)
                spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_2.addItem(spacerItem3)
                self.verticalLayout.addLayout(self.horizontalLayout_2)
                self.FilteredSignal = PlotWidget(self.Signals)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.FilteredSignal.sizePolicy().hasHeightForWidth())
                self.FilteredSignal.setSizePolicy(sizePolicy)
                self.FilteredSignal.setMinimumSize(QtCore.QSize(0, 161))
                self.FilteredSignal.setStyleSheet("border: none;")
                self.FilteredSignal.setObjectName("FilteredSignal")
                #self.FilteredSignal.doubleClicked.connect(self.Graph_1.Browse_Signals)
                self.verticalLayout.addWidget(self.FilteredSignal)
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.PEAKSlabel = QtWidgets.QLabel(self.Signals)
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                font.setWeight(75)
                self.PEAKSlabel.setFont(font)
                self.PEAKSlabel.setStyleSheet("color : white;\n"
        "")
                self.PEAKSlabel.setObjectName("PEAKSlabel")
                self.horizontalLayout_6.addWidget(self.PEAKSlabel)
                self.number = QtWidgets.QLineEdit(self.Signals)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.number.sizePolicy().hasHeightForWidth())
                self.number.setSizePolicy(sizePolicy)
                self.number.setMaximumSize(QtCore.QSize(45, 16777215))
                font = QtGui.QFont()
                font.setBold(True)
                font.setPointSize(13)
                font.setWeight(75)
                self.number.setFont(font)
                self.number.setStyleSheet("color:white;\n")
                self.number.setObjectName("number")
                self.horizontalLayout_6.addWidget(self.number)
                spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_6.addItem(spacerItem4)
                self.PauseButton = QtWidgets.QPushButton(self.Signals, clicked = lambda : self.Graph_1.Toggle_Play_Pause())
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.PauseButton.sizePolicy().hasHeightForWidth())
                self.PauseButton.setSizePolicy(sizePolicy)
                self.PauseButton.setMinimumSize(QtCore.QSize(167, 36))
                self.PauseButton.setMaximumSize(QtCore.QSize(501, 16777215))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(50)
                self.PauseButton.setFont(font)
                self.PauseButton.setStyleSheet("color:white;\n"
                "background-color: rgb(53, 107, 161);")
                self.PauseButton.setObjectName("PauseButton")
                self.horizontalLayout_6.addWidget(self.PauseButton)
                self.verticalLayout.addLayout(self.horizontalLayout_6)
                self.gridLayout.addWidget(self.Signals, 1, 0, 1, 1)
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_5.addItem(spacerItem5)
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                font = QtGui.QFont()
                font.setPointSize(24)
                font.setBold(True)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("color: #ffffff;\n"
                " background-image: none;")
                self.label_4.setObjectName("label_4")
                self.horizontalLayout_5.addWidget(self.label_4)
                spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_5.addItem(spacerItem6)
                self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
                self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
                self.groupBox.setSizePolicy(sizePolicy)
                self.groupBox.setMinimumSize(QtCore.QSize(639, 329))
                self.groupBox.setMaximumSize(QtCore.QSize(16777215, 352))
                self.groupBox.setStyleSheet("\n"
                "border:none;\n"
                "background-color: transparent;\n"
                "background-color: transparent")
                self.groupBox.setObjectName("groupBox")
                self.commandsBox = QtWidgets.QHBoxLayout(self.groupBox)
                self.commandsBox.setObjectName("commandsBox")
                spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
                self.commandsBox.addItem(spacerItem7)
                self.comandBox = QtWidgets.QGroupBox(self.groupBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.comandBox.sizePolicy().hasHeightForWidth())
                self.comandBox.setSizePolicy(sizePolicy)
                self.comandBox.setMinimumSize(QtCore.QSize(701, 329))
                self.comandBox.setMaximumSize(QtCore.QSize(455, 329))
                self.comandBox.setStyleSheet("\n"
                "border:none;\n"
                "border-style: outset;\n"
                "border-radius: 15px;")
                self.comandBox.setTitle("")
                self.comandBox.setObjectName("comandBox")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.comandBox)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.directionImage = QtWidgets.QLabel(self.comandBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.directionImage.sizePolicy().hasHeightForWidth())
                self.directionImage.setSizePolicy(sizePolicy)
                self.directionImage.setMaximumSize(QtCore.QSize(344, 16777215))
                self.directionImage.setStyleSheet("border: 1.2px solid #ffffff;")
                self.directionImage.setText("")
                self.directionImage.setPixmap(QtGui.QPixmap("Assets/direction.png"))
                self.directionImage.setScaledContents(True)
                self.directionImage.setObjectName("directionImage")
                self.horizontalLayout_3.addWidget(self.directionImage)
                ########################################################################################################
                self.voiceImage = QtWidgets.QLabel(self.comandBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.voiceImage.sizePolicy().hasHeightForWidth())
                self.voiceImage.setSizePolicy(sizePolicy)
                self.voiceImage.setMinimumSize(QtCore.QSize(321, 0))
                self.voiceImage.setMaximumSize(QtCore.QSize(708, 16777215))
                self.voiceImage.setStyleSheet("border: 1.2px solid #ffffff;\n"
                "background: transparent;\n"
                "background-color: transparent;")
                self.voiceImage.setText("")
                self.voiceImage.setPixmap(QtGui.QPixmap("Assets/stop.png"))
                self.voiceImage.setScaledContents(True)
                self.voiceImage.setObjectName("voiceImage")
                self.horizontalLayout_3.addWidget(self.voiceImage)
                #########################################################################################################
                self.commandsBox.addWidget(self.comandBox)
                spacerItem8 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
                self.commandsBox.addItem(spacerItem8)
                self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 1)
                MainWindow.setCentralWidget(self.centralwidget)
                #self.VoiceTransition()
                #self.DirectionTransition()

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                self.Graph_1.Graph_Window = self.RawSignal
                self.Graph_2.Graph_Window = self.FilteredSignal
                
        def ThreshHold(self,threshhold):
         self.voiceImage.setPixmap(QtGui.QPixmap(threshhold))
                
                                    
        def DirectionTransition(self, current):
                # Load the GIF file
                movie = QMovie(current)
                # Set the movie to the label
                self.directionImage.setMovie(movie)
                movie.start()

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_3.setText(_translate("MainWindow", "Gesture-Go"))
                self.label_2.setText(_translate("MainWindow", "Raw Signal"))
                self.label.setText(_translate("MainWindow", "Filtered Signal"))
                self.PauseButton.setText(_translate("MainWindow", " Pause "))
                self.PEAKSlabel.setText(_translate("MainWindow", "Number of Flexions:"))
                self.label_4.setText(_translate("MainWindow", "Current Command"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI()
    graph_1 = ui.Graph_1
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
