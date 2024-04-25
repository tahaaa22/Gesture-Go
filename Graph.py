from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import random
import Signals, wfdb # type: ignore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import time

# noinspection PyTypeChecker
class Graph:
    def __init__(self, Graph_Number, ui_mainwindow, other_graph, graph_window=None):
        self.graph_number = Graph_Number
        self.UI_Window = ui_mainwindow
        self.Graph_Window = graph_window
        self.Other_Graph = other_graph  # Reference to the other graph
        self.Paused = False
        self.CurrentSignal = None
        self.Y_Coordinates = None
        self.X_Coordinates =None
        self.forwardflag = False
        self.backwardflag = False
        self.rightflag = False
        self.leftflag = False
        self.count = 0
    
    def playVoice(self, path):
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.player.play()
        #self.UI_Window.VoiceTransition()
        time.sleep(3)
      
            
            
    def detectMotion(self):
                if self.CurrentSignal.Y_Coordinates[self.CurrentSignal.X_Points_Plotted]<= self.CurrentSignal.Max_Value and self.CurrentSignal.Y_Coordinates[self.CurrentSignal.X_Points_Plotted] > self.CurrentSignal.secondQuad_Value:
                    self.UI_Window.DirectionTransition("Assets/forward-direction.gif")
                    self.UI_Window.ThreshHold("Assets/forwardth.png")
                    if not self.forwardflag:
                        self.count+=1
                        self.playVoice("audio/moveforward.wav")
                        self.forwardflag = True
                        self.backwardflag = False
                        self.rightflag = False
                        self.leftflag = False
                elif  self.CurrentSignal.Y_Coordinates[self.CurrentSignal.X_Points_Plotted] <= self.CurrentSignal.secondQuad_Value and self.CurrentSignal.Y_Coordinates[self.CurrentSignal.X_Points_Plotted] > self.CurrentSignal.FirstQuad_Value:
                    self.UI_Window.DirectionTransition("Assets/right-direction.gif")
                    self.UI_Window.ThreshHold("Assets/rightth.png")
                    if not self.rightflag:
                        self.count+=1
                        self.playVoice("audio/moveright.wav")
                        self.rightflag = True
                        self.backwardflag = False
                        self.forwardflag = False
                        self.leftflag = False
                elif self.CurrentSignal.Y_Coordinates[self.CurrentSignal.X_Points_Plotted] > 0 and self.CurrentSignal.Y_Coordinates[self.CurrentSignal.X_Points_Plotted] <= self.CurrentSignal.FirstQuad_Value:
                    self.UI_Window.DirectionTransition("Assets/left-direction.gif")
                    self.UI_Window.ThreshHold("Assets/leftth.png")
                    if not self.leftflag:
                        self.count+=1
                        self.playVoice("audio/Turnleft.wav")
                        self.leftflag = True
                        self.backwardflag = False
                        self.rightflag = False
                        self.forwardflag = False
                elif self.CurrentSignal.Y_Coordinates[self.CurrentSignal.X_Points_Plotted] > self.CurrentSignal.Min_Value and self.CurrentSignal.Y_Coordinates[self.CurrentSignal.X_Points_Plotted] < -(self.CurrentSignal.FirstQuad_Value):
                    self.UI_Window.DirectionTransition("Assets/back-direction.gif")
                    self.UI_Window.ThreshHold("Assets/backwardth.png")
                    if not self.backwardflag:
                        self.count+=1
                        self.playVoice("audio/moveback.wav")
                        self.backwardflag = True
                        self.forwardflag = False
                        self.rightflag = False
                        self.leftflag = False
                self.UI_Window.number.setText("  "+str(self.count)+"")

 

    def Browse_Signals(self):
        File_Path, _ = QFileDialog.getOpenFileName(None, "Browse Signal", "", "All Files (*)")
        #test6.txt
        if File_Path:
            Record = wfdb.rdrecord(File_Path[:-4])
            Y_Coordinates = list(Record.p_signal[:, 0])
            X_Coordinates = list(np.arange(len(Y_Coordinates)))
            self.CurrentSignal = Signals.Signal(col = "red", X_List=X_Coordinates, Y_list=Y_Coordinates,mainwaindow =self.UI_Window, graph=self )


    def Toggle_Play_Pause(self):
        _translate = QtCore.QCoreApplication.translate

        self.Paused = not self.Paused
           
        if not self.Paused:
                self.UI_Window.PauseButton.setText(_translate("MainWindow", "Pause"))
        else:
                self.UI_Window.PauseButton.setText(_translate("MainWindow", "Play"))

        if self.CurrentSignal:
              self.CurrentSignal.pause = not self.CurrentSignal.pause
              self.Graph_Window.getViewBox().setXRange(
                    max(self.CurrentSignal.X_Coordinates[0: self.CurrentSignal.X_Points_Plotted + 1]) - 1000,
                    max(self.CurrentSignal.X_Coordinates[0: self.CurrentSignal.X_Points_Plotted + 1]))

