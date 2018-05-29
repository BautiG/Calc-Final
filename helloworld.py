import math #brings in the basic python math used in the rest of the program

yFunction = str(input("f(x)="))#asks for a function
yPrime = str(input("f ' (x)="))#asks for a derivative
xValue = int(input("where does your approximation start? "))#asks where the method begins
rePeat = int(input("how many times should I approximate? "))#asks how many times the process should be repeated
print("")#this just creates an empty line that makes the output look nicer
print("The approximations of x=0 (in order from first to last):")

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

def deriVative():
    yPrimeNew = ""
    for i in range(len(yPrime)):
        if yPrime[i] == "x":
            yPrimeNew += str(xValue)
        else:
            yPrimeNew += yPrime[i]
    i += 1
    
    #print(yPrimeNew)
    yPrimeNew = eval(yPrimeNew)
    #print(yPrimeNew)


counTer = 0
while counTer < rePeat:
    funcTion()
    deriVative()

    yFunctionNew = eval(yFunctionNew)
    yPrimeNew = eval(yPrimeNew)
    
    newGuess = xValue - (yFunctionNew/yPrimeNew)
    print(newGuess)
    xValue = newGuess
    counTer += 1
