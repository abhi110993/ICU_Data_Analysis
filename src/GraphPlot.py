"""

# Author: Abhishek Mishra
# MTech Student
# IIT Ropar
# Entry Number- 2018CSM1002

"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Plots:
    
    def plot3DGraph(self,x1, y1, z1,x2, y2, z2,xlabel,ylabel,zlabel,title):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x1, y1, z1, c='r', marker='o')
        ax.scatter(x2, y2, z2, c='b', marker='o')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)
        plt.title(title)
        plt.show()
        
        
    
    def combinePlot(self,x,y1,y2,xmin,xlim,ymin,ylim,instances,title,xaxisLabel,yaxisLabel):
        fig = plt.figure(instances)
        plt.plot(x, y1, label='Validation',color='red')
        plt.plot(x, y2, label='Train',color='blue')
        plt.axis([xmin, xlim, ymin, ylim])
        plt.title(title)
        plt.xlabel(xaxisLabel)
        plt.ylabel(yaxisLabel)
        plt.grid(True)
        #plt.show()
        fig.savefig("figures/"+str(instances)+'.png')
    
    def adaptablePlot(self,x,y1,y2,instances,title,xaxisLabel,yaxisLabel):
        xmin=50000
        ymin=50000
        xmax=-50000
        ymax=-50000
        for i in x:
            if i<xmin:
                xmin=i
            elif i>xmax:
                xmax=i
        for i in y1:
            if i<ymin:
                ymin=i
            elif i>ymax:
                ymax=i
        for i in y2:
            if i<ymin:
                ymin=i
            elif i>ymax:
                ymax=i
        self.combinePlot(x, y1, y2, xmin, xmax+1, ymin, ymax+1, instances, title, xaxisLabel, yaxisLabel)
    
    def makeSinglePlot(self,x,y1,xlim,ylim,instances,title,xaxisLabel,yaxisLabel):
        fig = plt.figure(instances)
        plt.plot(x, y1, label='Train',color='darkgreen')
        plt.axis([0, xlim, 0, ylim])
        plt.title(title)
        plt.xlabel(xaxisLabel)
        plt.ylabel(yaxisLabel)
        plt.grid(True)
        #plt.show()
        fig.savefig("figures/"+str(instances)+'.png')
    
    def makeDotPlot(self,x,y1,xlim,ylim,instances,title,xaxisLabel,yaxisLabel):
        fig = plt.figure(instances)
        for i in range(0,len(x)):
            if(y1[i]<=0.5):
                plt.plot(x[i][0], x[i][1],'ro', label='class 0',color='darkgreen')
            else:
                plt.plot(x[i][0], x[i][1],'ro', label='class 1',color='darkblue')
            
        #plt.plot([0, 20], [0,20],color='darkblue')
        plt.axis([0, xlim, 0, ylim])
        plt.title(title)
        plt.xlabel(xaxisLabel)
        plt.ylabel(yaxisLabel)
        plt.grid(True)
        #plt.show()
        fig.savefig("figures/"+str(instances)+'.png')
        
    def plotMeanAndVarianceGraph(self,instance,x,y,variance,xlabel,ylabel,title):
        plt.errorbar(x, y, variance, fmt='.k');
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.savefig("figures/"+str(instance)+'.png')
        plt.close()
        