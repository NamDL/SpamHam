#!/usr/bin/python

import os
import math
import sys

def getSpamWordProbability(word):
    global spamWordCount
    global spamSet
    if(word in spamSet):
        return (spamSet[word]/(spamWordCount))
    
def gethamWordProbability(word):
    global hamWordCount
    global hamSet
    if(word in hamSet):
        return (hamSet[word]/(hamWordCount))
    

def classfyFile(path):
    global spamSet
    global hamSet
    spamProb=0
    hamProb=0
    f=open(path, "r", encoding="latin1")
    for word in f.read().split():
        if((word in spamSet) or (word in hamSet)):
            spamProb+=math.log(getSpamWordProbability(word))
            hamProb+=math.log(gethamWordProbability(word))
    spamProb+=classProbSpam
    hamProb+=classProbHam
    if(spamProb>=hamProb):
        return "spam"
    else:
        return "ham"
                

def main(path):
    string=""
    spamFile=0
    hamFile=0
    for root, subdirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                filePath=os.path.abspath(os.path.join(root, file))
                category=classfyFile(filePath)
                string+=category+" "+filePath+"\n"
                if(category=="spam"):
                    spamFile+=1
                else:
                    hamFile+=1
    fo=open("nboutput.txt", "a", encoding="latin1")
    fo.write(string)    

f=open("nbmodel.txt", "r", encoding="latin1")
vocabSize=int(f.readline())
spamStat=f.readline().split(" ")
spamDocCount=int(spamStat[1].strip())
spamWordCount=int(spamStat[2].strip())
hamSet={}
spamSet={}

for line in f:
    if(line.startswith("*****")):
        break
    else:
        words=line.split(":-:-:")
        spamSet[words[0]]=int(words[1].strip())
        
hamStat=f.readline().split(" ")
hamDocCount=int(hamStat[1].strip())
hamWordCount=int(hamStat[2].strip())

for line in f:
    words=line.split(":-:-:")
    hamSet[words[0]]=int(words[1].strip())

classProbSpam=math.log(spamDocCount/(spamDocCount+hamDocCount))
classProbHam=math.log(hamDocCount/(spamDocCount+hamDocCount))

main(sys.argv[1])
        
        
                
        
