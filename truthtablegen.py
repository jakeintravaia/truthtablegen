varnames = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
inputBits = []
outputBits = []
minTerms = []
outputs = []

def makeTable(ibc, obc):
    for x in range(0, ibc):
        inputBits.append(varnames[x])
    for x in range(ibc, (obc + ibc)):
        outputBits.append(varnames[x])
    binaryCount(ibc)

def printTable():
    fstring = ""
    sstring = ""
    tstring = ""
    for x in inputBits:
        fstring = fstring + x + " "
    fstring = fstring + "| "
    for y in outputBits:
        fstring = fstring + y + " "
    for z in range(0, len(minTerms)):
        tstring = input("Enter value for row {} ({} bits): ".format(z, len(outputBits)))
        outputs.append(list(tstring))
        tstring = ""
    print(fstring)
    print("-" * len(fstring))
    
    for x in range(0, len(minTerms)):
        print(*minTerms[x], end=" "), print("|", end=" "), print(*outputs[x])
        



def binaryCount(ibc):
    for x in range(0, pow(2, ibc)):
        minTerms.append(list("0" * (ibc - len("{0:b}".format(x))) + "{0:b}".format(x)))

def clearTable():
    inputBits = []
    outputBits = []
    minTerms = []
    outputs = []
