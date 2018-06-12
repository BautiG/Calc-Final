import math #brings in the basic python math used in the rest of the program

yFunction = str(input("f(x)="))#asks for a function
xValue = int(input("where does your approximation start? "))#asks where the method begins
rePeat = int(input("how many times should I approximate? "))#asks how many times the process should be repeated
print("")#this just creates an empty line that makes the output look nicer
print("The approximations of y=0 (in order from first to last):")

def funcTion():
    yFunctionNew = ""
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNew += str(xValue)
        else:
            yFunctionNew += yFunction[i]
    i += 1
    
    #print(yFunctionNew)
    yFunctionNew = eval(yFunctionNew)
    #print(yFunctionNew)

def functionRight():
    rightPoint = ""
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            rightPoint += str(xValue+.001)
        else:
            rightPoint += yFunction[i]
    i += 1
    
    rightPoint = eval(rightPoint)
    #print(rightPoint)

counTer = 0
while counTer < rePeat:
    funcTion()
    functionRight()

    yFunctionNew = eval(yFunctionNew)
    rightPoint = eval(rightPoint)
    
    deriVative = (rightPoint-yFunctionNew)/.001
    
    newGuess = xValue - (yFunctionNew/deriVative)
    print(newGuess)
    xValue = newGuess
    counTer += 1
