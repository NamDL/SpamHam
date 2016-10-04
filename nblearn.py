#!/usr/bin/python

import os
import sys

spamCount=0
hamCount=0
spamWords=0
hamWords=0
hamSet={}
spamSet={}
stopWord=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

def checkFile(fileName,className):
    global hamWords
    global spamWords
    global hamSet
    global spamSet
    f=open(fileName, "r", encoding="latin1")
    for word in f.read().split():
        if className=="ham":
            hamSet[word] = hamSet.get(word, 0) + 1
            hamWords+=1
        else:
            spamSet[word] = spamSet.get(word, 0) + 1
            spamWords+=1

def printToFile(s):
    global hamWords
    global spamWords
    global hamSet
    global spamSet
    global spamCount
    global hamCount
    string=str(len(spamSet)+len(hamSet))+"\n"
    string+="SPAM "+str(spamCount)+" "+str(spamWords)+"\n"
    for key, value in spamSet.items():
        string+=key+":-:-:"+str(value)+"\n"
    string+="********************************\n"
    string+="HAM "+str(hamCount)+" "+str(hamWords)+"\n"
    for key, value in hamSet.items():
        string+=key+":-:-:"+str(value)+"\n"
    s.write(string)

def smoothing():
    global hamWords
    global spamWords
    global hamSet
    global spamSet
    for key, value in spamSet.items():
        if(not key in hamSet):
            hamSet[key]=1
            hamWords+=1
    for key, value in hamSet.items():
        if(not key in spamSet):
            spamSet[key]=1
            spamWords+=1
    
def main(root_dir):
    global spamCount
    global hamCount
    for root, subdirs, files in os.walk(root_dir):    
        for subdir in subdirs:
            if subdir=="ham":
                for filename in os.listdir(os.path.join(root, subdir)):
                    hamCount+=1
                    checkFile(os.path.join(root,subdir,filename),"ham")
            elif subdir=="spam":
                for filename in os.listdir(os.path.join(root, subdir)):
                    spamCount+=1
                    checkFile(os.path.join(root,subdir,filename),"spam")
    fo = open("nbmodel.txt", "a",encoding="latin1")
    smoothing()
    printToFile(fo)

main(sys.argv[1])          
        
                
        
