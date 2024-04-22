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


    def Browse_Signals(self):
        File_Path, _ = QFileDialog.getOpenFileName(None, "Browse Signal", "", "All Files (*)")
        #test6.txt
        if File_Path:
            Record = wfdb.rdrecord(File_Path[:-4])
            Y_Coordinates = list(Record.p_signal[:, 0])
            X_Coordinates = list(np.arange(len(Y_Coordinates)))
            Sample_Signal = Signals.Signal(col = "red", X_List=X_Coordinates, Y_list=Y_Coordinates,graphWdg=self.Graph_Window, graphObj=self)


    def Toggle_Play_Pause(self):
        _translate = QtCore.QCoreApplication.translate
        self.Paused = not self.Paused
        if self.Linked:
            self.Other_Graph.Paused = self.Paused
            for channel in self.Other_Graph.CHANNELS:
                if channel.Signal:
                    channel.Signal.pause = not channel.Signal.pause

            if not self.Paused:
                self.UI_Window.Play1_Button.setText(_translate("MainWindow", "   Pause         "))
                self.UI_Window.Play2_Button.setText(_translate("MainWindow", "   Pause         "))
            else:
                self.UI_Window.Play1_Button.setText(_translate("MainWindow", "   Play         "))
                self.UI_Window.Play2_Button.setText(_translate("MainWindow", "   Play         "))
        else:
            if self.graph_number == 1:
                if not self.Paused:
                    self.UI_Window.Play1_Button.setText(_translate("MainWindow", "   Pause         "))
                else:
                    self.UI_Window.Play1_Button.setText(_translate("MainWindow", "   Play         "))
            else:
                if not self.Paused:
                    self.UI_Window.Play2_Button.setText(_translate("MainWindow", "   Pause         "))
                else:
                    self.UI_Window.Play2_Button.setText(_translate("MainWindow", "   Play         "))

        for channel in self.CHANNELS:
            if channel.Signal:
                channel.Signal.pause = not channel.Signal.pause
                self.Graph_Window.getViewBox().setXRange(
                    max(channel.Signal.X_Coordinates[0: channel.Signal.X_Points_Plotted + 1]) - 100,
                    max(channel.Signal.X_Coordinates[0: channel.Signal.X_Points_Plotted + 1]))

