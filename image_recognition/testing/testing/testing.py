
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
import time
from statistics import mean	  
from collections import Counter


#create data base
def createExamples():
    numberArrayExamples =  open("numArx.txt", 'a')
    numberWeHave = range(0,10)
    versionsWeHave = range(1,10)


    for eachNum in numberWeHave:
        for eachVer in versionsWeHave:
            #print( str(eachNum)+'.'+str(eachVer))
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)

#createExamples()

def threshold(imageArray):

    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)
       
    balance = mean(balanceAr)
    

    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
            
            
    return newAr
    


def whatNumIsThis(filePath):

    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')
    
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x = 0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x+=1
        except Exception as e:
            print(str(e))
                
    print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    print(x[0])

whatNumIsThis('images/test.png')