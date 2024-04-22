from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import random
import Signals, wfdb # type: ignore

# noinspection PyTypeChecker
class Graph:
    def __init__(self, Graph_Number, ui_mainwindow, other_graph, graph_window=None):
        self.graph_number = Graph_Number
        self.UI_Window = ui_mainwindow
        self.Graph_Window = graph_window
        self.Other_Graph = other_graph  # Reference to the other graph
        self.Paused = False
        self.CurrentSignal


    def Browse_Signals(self):
        File_Path, _ = QFileDialog.getOpenFileName(None, "Browse Signal", "", "All Files (*)")
        #test6.txt
        if File_Path:
            Record = wfdb.rdrecord(File_Path[:-4])
            Y_Coordinates = list(Record.p_signal[:, 0])
            X_Coordinates = list(np.arange(len(Y_Coordinates)))
            self.CurrentSignal = Signals.Signal(col = "red", X_List=X_Coordinates, Y_list=Y_Coordinates,graphWdg=self.Graph_Window, graphObj=self)


    def Toggle_Play_Pause(self):
        _translate = QtCore.QCoreApplication.translate

        self.Paused = not self.Paused
           
        if not self.Paused:
                self.UI_Window.PauseButton.setText(_translate("MainWindow", "   Pause         "))
        else:
                self.UI_Window.PauseButton.setText(_translate("MainWindow", "   Play         "))

        if self.CurrentSignal:
              self.CurrentSignal.pause = not self.CurrentSignal.pause
              self.Graph_Window.getViewBox().setXRange(
                    max(self.CurrentSignal.X_Coordinates[0: self.CurrentSignal.X_Points_Plotted + 1]) - 100,
                    max(self.CurrentSignal.X_Coordinates[0: self.CurrentSignal.X_Points_Plotted + 1]))

