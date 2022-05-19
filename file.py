from datetime import datetime
import os
import sys
import tarfile
import statistics

import numpy as np
import matplotlib.pyplot as plt



def printlog(message):
        logFile = open('/home/shiyue/Downloads/femu.log', 'a')
        logFile.write("{} - {}".format(datetime.now(),message))
        logFile.write("\n")
        logFile.close()

def main():
    for tracename in os.listdir("/home/shiyue/Downloads/traces"):

        traceShortName = tracename[20:22]
        path = os.path.join("/home/shiyue/Downloads/traces",tracename)
        objectCount = 10000

        with open(path) as myfile:
            lines = [next(myfile) for x in range(objectCount)] 
        linesLength = len(lines)

        getcount = 0
        gettotalSize = 0.0
        putcount = 0
        puttotalSize = 0.0
        headcount = 0
        headtotalSize = 0.0

        totalSize = 0.0
        sizelist = []
        for line in lines:

            info = line.split()
            requestType = info[1].split(".")[1]
            if(requestType == "DELETE"):
                continue
            fileSize = float(info[3])

            if (requestType == "PUT" or requestType == "HEAD"):
                putcount+=1
                puttotalSize+=fileSize
            elif(requestType == "GET"):
                getcount+=1
                gettotalSize+=fileSize
            elif(requestType == "HEAD"):
                headcount+=1
                headtotalSize+=fileSize
            totalSize +=fileSize

            newFileSize = fileSize/1024/1024 #convert file_size from B to MB
            sizelist.append(newFileSize)
        
        #CDF
        data = np.sort(sizelist)
        p = 1. * np.arange(len(data)) / float(len(data) - 1)
        # print("The CDF result is-",p)
        fig = plt.figure()
        fig.suptitle(traceShortName)
        ax2 = fig.add_subplot(111)
        ax2.plot(data, p)
        ax2.set_xlabel('Trace Size (MB)')
        ax2.set_ylabel('p')
        # plt.show()
        plt.savefig(tracename)

        print("")
        print("Trace: {} Length: {} Total trace size : {} GB".format(traceShortName,objectCount,float(totalSize/1024/1024/1024)))
        print("Trace: {} GET number: {} GET size: {} GB".format(traceShortName,getcount,float(gettotalSize/1024/1024/1024)))
        print("Trace: {} PUT number: {} PUT size: {} GB".format(traceShortName,putcount+headcount,float((puttotalSize+ headtotalSize)/1024/1024/1024)))
        print("Trace Mean Value: {} MB".format(float(totalSize/objectCount/1024/2014)))
        print("Trace Standard Deviation: {} MB".format(float(statistics.stdev(sizelist))))
        print("")

        printlog("Trace: {} Length: {} Total trace size : {} GB".format(tracename,objectCount,float(totalSize/1024/1024/1024)))
        printlog("Trace: {} GET number: {} GET size: {} GB".format(tracename,getcount,float(gettotalSize/1024/1024/1024)))
        printlog("Trace: {} PUT number: {} PUT size: {} GB".format(tracename,putcount+headcount,float((puttotalSize+ headtotalSize)/1024/1024/1024)))







if __name__ == "__main__":
    main()
