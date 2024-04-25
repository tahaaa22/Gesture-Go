from PyQt5 import QtCore
import time
from scipy.signal import freqz, lfilter, filtfilt, butter, zpk2tf

class Signal:
    def __init__(self, col, X_List, Y_list, mainwaindow, graph ):
        self.pause = False #to control movement of the signal
        self.X_Coordinates = X_List
        self.Y_Coordinates = Y_list
        self.color = col
        self.ui = mainwaindow
        self.X = []
        self.Y = []
        self.X_Points_Plotted = 0
        self.speed = 10
        self.Max_Value = 0
        self.Min_Value = 0
        self.FirstQuad_Value = 0
        self.secondQuad_Value = 0
        self.graphwidget = graph
        self.filteredYaxis= None
        self.Plot_Signal()
       
    def Plot_Signal(self):
        self.data_line = self.ui.RawSignal.plot(self.X_Coordinates[:1], self.Y_Coordinates[:1], pen=self.color)
        numerator, denominator = butter(2, 0.5, 'high', analog=False) #(Highpass Filter testing)
        self.filteredYaxis = lfilter(numerator, denominator, self.Y_Coordinates)
        self.data_line2 = self.ui.FilteredSignal.plot(self.X_Coordinates[:1], self.filteredYaxis[:1], pen="green")
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.Update_Plot_Data)
        self.timer.start()

    def Update_Plot_Data(self):
        if not self.pause and self.data_line:
            self.X_Points_Plotted += self.speed
            
            self.ui.RawSignal.setLimits(xMin=0, xMax=float('inf'))
            self.ui.FilteredSignal.setLimits(xMin=0, xMax=float('inf'))
            
            self.data_line2.setData(self.X_Coordinates[0 : self.X_Points_Plotted + 1], self.filteredYaxis[0 : self.X_Points_Plotted + 1])  # Update the data.
            self.data_line.setData(self.X_Coordinates[0 : self.X_Points_Plotted + 1], self.Y_Coordinates[0 : self.X_Points_Plotted + 1])  # Update the data.
            
            self.ui.FilteredSignal.getViewBox().setXRange(max(self.X_Coordinates[0: self.X_Points_Plotted + 1]) - 1000, max(self.X_Coordinates[0: self.X_Points_Plotted + 1]))
            self.ui.RawSignal.getViewBox().setXRange(max(self.X_Coordinates[0: self.X_Points_Plotted + 1]) - 1000, max(self.X_Coordinates[0: self.X_Points_Plotted + 1]))
            
            self.Max_Value = max(self.Y_Coordinates[0 : self.X_Points_Plotted + 1]) #forward command
            self.Min_Value = min(self.Y_Coordinates[0 : self.X_Points_Plotted + 1]) #back command
            self.FirstQuad_Value = 0.3 * self.Max_Value
            self.secondQuad_Value = 0.6 * self.Max_Value
            self.graphwidget.detectMotion()

        elif self.pause:
            self.ui.RawSignal.setLimits(xMin=0, xMax=self.X_Points_Plotted)
       
    def Toggle_Play_Pause(self):
        self.pause = not self.pause

