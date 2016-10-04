#!/usr/bin/python

import os
import sys

def main(path):
    fo=open(path,"r",encoding="latin1")
    corectSpam=0
    corectHam=0
    wrongSpam=0
    wrongHam=0
    classiiedAsSpam=0
    classiiedAsHam=0
    actualSpam=0
    actualHam=0
    total=0
    for line in fo:
        total+=1
        words=line.split(" ")
        
        'Count of message classfied as Spam and Ham resp'
        if(words[0]=="spam"):
            classiiedAsSpam+=1
        if(words[0]=="ham"):
            classiiedAsHam+=1
            
        'Count of messages which are actually spam and han resp'
        if(".spam.txt" in words[1]):
            actualSpam+=1
        if(".ham.txt" in words[1]):
            actualHam+=1

        'count of messages wrongly classified as spam and ham'   
        if(words[0]=="spam" and not ".spam.txt" in words[1]):
            wrongSpam+=1
        if(words[0]=="ham" and not ".ham.txt" in words[1]):
            wrongHam+=1

        'Count of messages correctly classified as spam and ham resp'
        if(words[0]=="spam" and ".spam.txt" in words[1]):
            corectSpam+=1
        if(words[0]=="ham" and ".ham.txt" in words[1]):
            corectHam+=1
    
    print("messages correctly classified as spam"+str(corectSpam))
    print("messages correctly classified as ham "+str(corectHam))
    print("count of messages wrongly classified as spam "+str(wrongSpam))
    print("count of messages wrongly classified as ham "+str(wrongHam))
    print("Count of message classfied as spam "+str(classiiedAsSpam))
    print("Count of message classfied as ham "+str(classiiedAsHam))
    print("Count of messages which are actually spam "+str(actualSpam))
    print("Count of messages which are actually ham "+str(actualHam))
    print("\n")
    
    spamRecall=corectSpam/actualSpam
    hamRecall=corectHam/actualHam
    spamPrecision=corectSpam/classiiedAsSpam
    hamPrecision=corectHam/classiiedAsHam
    spamF1=(2*spamPrecision*spamRecall)/(spamRecall+spamPrecision)
    hamF1= (2*hamRecall*hamPrecision)/(hamPrecision+hamRecall)
    weightedAverage=((actualSpam*spamF1)/total)+((actualHam*hamF1)/total)

    print("Spam Precision "+str(spamPrecision))
    print("Spam Recall "+str(spamRecall))    
    print("Spam F1 Score "+str(spamF1))
    print("\n")
    
    print("Ham Precision "+str(hamPrecision))
    print("Ham Recall "+str(hamRecall))    
    print("Ham F1 Score "+str(hamF1))
    print("\n")

    print("Weighted Average"+str(weightedAverage))
        
main(sys.argv[1])          
        
                
        
