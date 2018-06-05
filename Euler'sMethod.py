import math #brings in the basic python math used in the rest of the program

yPrime = str(input("f ' (x,y)="))#asks for a derivative
xValue = int(input("at what x value does your approximation start? "))
yValue = int(input("at what y value does your approximation start? "))
dX = float(input("what is the value of dx? "))
rePeat = int(input("how many times should I approximate? "))#asks how many times the process should be repeated
print("")#this just creates an empty line that makes the output look nicer
print("The approximations(in order from first to last):")

def deriVative():
    yPrimeNew = ""
    for i in range(len(yPrime)):
        if yPrime[i] != "x" and yPrime[i] != "y":
            yPrimeNew += yPrime[i]
        if yPrime[i] == "x":
            yPrimeNew += str(xValue)
        if yPrime[i] == "y":
            yPrimeNew += str(yValue)
    i += 1
    
    yPrimeNew = eval(yPrimeNew)

print("(",xValue,",",yValue,")")
counTer = 0
while counTer < rePeat:
    deriVative()
    
    yPrimeNew = eval(yPrimeNew)
    
    dY = (yPrimeNew)*dX
    
    newX = xValue + dX
    newY = yValue + dY
    print("(",newX,",",newY,")")
    
    xValue = newX
    yValue = newY
    
    counTer += 1
