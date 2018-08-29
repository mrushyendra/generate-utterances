import re
from argparse import ArgumentParser
import os.path #can use pathlib in python3

# Given a string in the proper format, returns an array of all possible utterances by expanding the string
def generateUtterances(string, utterancesArr=[""]):
    tokensPrefilter = [x.strip() for x in splitParen(string)] #e.g. "(Send | Transfer) money" --> ["Send | Transfer", "money"]
    if len(tokensPrefilter) == 1: #Base condition for recursion, stopping when string is just one word
        utterancesArr = [tokensPrefilter[0]]
        return utterancesArr
    tokens = filter(None, tokensPrefilter)  #filter removes empty strings, usually at start or end of list

    for token in tokens:
        strings = list()
        options = splitOR(token) #e.g. : "Do a | Please do a" --> ["Do a" , "Please do a"]
        for option in options:
            strings+=generateUtterances(option) 

        newUtterancesArr = list()
        for utterance in utterancesArr:
            for string in strings:
                updatedUtterance = utterance + string + " "
                newUtterancesArr.append(updatedUtterance)
        utterancesArr = newUtterancesArr
    return utterancesArr

#Split by top level '|' token e.g. "Send some (money | cash | funds) | Transfer some money" --> ["Send some (money | cash | funds)", "Transfer some money"]
def splitOR(string):
    parenLevel = 0
    parts = list()
    part = ""

    for char in string:
        if char == '(':
            parenLevel+=1
            part+=char
        elif char == ')':
            parenLevel-=1
            part+=char
        elif char == '|':
            if parenLevel == 0:
                parts.append(part)
                part = ""
            else:
                part+=char
        else:
            part+=char
    
    parts.append(part)
    return parts

# splits a given string into parts based on top-level parentheses. e.g. "(Do a | (could you | can you ) do a ) funds transfer to (john | rahul)"
# --> ["Do a | (could you | can you) do a", "funds transfer to", "john | rahul"]
# IMPT: Assumes parentheses are balanced
def splitParen(string):
    parts = list()
    part = ""
    parenLevel = 0
    for char in string:
        if char == '(':
            parenLevel += 1
            if parenLevel == 1:
                parts.append(part) #append part collected till now and start a new part
                part = ""
            else:
                part += char
        elif char == ')':
            parenLevel -= 1
            if parenLevel == 0:
                parts.append(part)
                part = ""
            else:
                part += char
        else:
            part += char

    parts.append(part)
    return parts

parser = ArgumentParser()
parser.add_argument("inputStrFile", type=str, help="Path to file that contains the input sentence", metavar="inputStrFileName")
parser.add_argument("outputFile", type=str, help="Path to file where utterances will be written to", metavar="outputFileName")
args = parser.parse_args()

testStr = None
inputFileName = args.inputStrFile
with open(inputFileName, "r") as inputFile:
    content = inputFile.readlines()
    content = [x.strip() for x in content] #remove newline characters
    testStr = content[0]
if testStr is None:
    print("Could not read string from input file name")

utterancesArr = generateUtterances(testStr)

outputFileName = args.outputFile
with open(outputFileName, "w") as outputFile:
    for utterance in utterancesArr:
        outputFile.write(utterance + os.linesep)

#Deprecated
#os.path ensures this works for both windows and mac/linux
#outputFileDir = os.path.join("") #modify arguments to point to your file path
