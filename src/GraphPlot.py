import matplotlib.pyplot as plt

class Plots:
    
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
        