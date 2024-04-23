from PyQt5 import QtCore


class Signal:
    def __init__(self, col, X_List, Y_list, graphWdg, graphObj):
        self.pause = False #to control movement of the signal
        self.X_Coordinates = X_List
        self.Y_Coordinates = Y_list
        self.color = col
        self.Graph_Widget = graphWdg
        self.Graph_Object = graphObj
        self.X = []
        self.Y = []
        self.X_Points_Plotted = 0
        self.speed = 1
        self.Max_Value = 0
        self.Min_Value = float('inf')
       
    def Plot_Signal(self):
        self.data_line = self.Graph_Widget.plot(self.X_Coordinates[:1], self.Y_Coordinates[:1],pen=self.color)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.Update_Plot_Data)
        self.timer.start()

    def Update_Plot_Data(self):
        
        if not self.pause and self.data_line:
            self.X_Points_Plotted += self.speed
            self.Graph_Widget.setLimits(xMin=0, xMax=float('inf'))
            self.data_line.setData(self.X_Coordinates[0 : self.X_Points_Plotted + 1], self.Y_Coordinates[0 : self.X_Points_Plotted + 1])  # Update the data.
            self.Graph_Widget.getViewBox().setXRange(max(self.X_Coordinates[0: self.X_Points_Plotted + 1]) - 100, max(self.X_Coordinates[0: self.X_Points_Plotted + 1]))

            # Check if the signal has ended
            #if self.X_Points_Plotted >= len(self.X_Coordinates):

        elif self.pause:
            self.Graph_Widget.setLimits(xMin=0, xMax=self.X_Points_Plotted)
       
    def Toggle_Play_Pause(self):
        self.pause = not self.pause

