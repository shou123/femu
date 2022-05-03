from datetime import datetime

import os
import sys
import tarfile


def printlog(message):
        logFile = open('/home/shiyue/Downloads/femu.log', 'a')
        logFile.write("{} - {}".format(datetime.now(),message))
        logFile.write("\n")
        logFile.close()


# def compressFile():
#     for filename in os.listdir("/home/shiyue/Downloads"):


#         file_name = "/root/backup/home.tar.gz"

#         tar = tarfile.open(file_name, "w:gz")
#         os.chdir("/home")
#         for name in os.listdir("."):
#             tar.add(name)
#         tar.close()




def main():
    for tracename in os.listdir("/home/shiyue/Downloads/traces"):

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
    
        print("Trace: {} Length: {} Total trace size : {} GB".format(tracename,objectCount,float(totalSize/1024/1024/1024)))
        print("Trace: {} GET number: {} GET size: {} GB".format(tracename,getcount,float(gettotalSize/1024/1024/1024)))
        print("Trace: {} PUT number: {} PUT size: {} GB".format(tracename,putcount+headcount,float((puttotalSize+ headtotalSize)/1024/1024/1024)))
        print("")

        printlog("Trace: {} Length: {} Total trace size : {} GB".format(tracename,objectCount,float(totalSize/1024/1024/1024)))
        printlog("Trace: {} GET number: {} GET size: {} GB".format(tracename,getcount,float(gettotalSize/1024/1024/1024)))
        printlog("Trace: {} PUT number: {} PUT size: {} GB".format(tracename,putcount+headcount,float((puttotalSize+ headtotalSize)/1024/1024/1024)))







if __name__ == "__main__":
    main()
