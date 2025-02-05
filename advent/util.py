from datetime import datetime



# simple function to get input
def readInput() -> []:
    myInput = []
    iFile = open('input.txt')
    for line in iFile:
        myInput.append(line.strip('\n'))
    return(myInput)

# simple function to write output to file
def writeOutput(output: []):
    oFile = open('output.txt','w')
    for line in output:
        oFile.write(line + '\n')
    return(True)

# Reset Log, typically run once at the beginning of the program
def logReset():
    logFile = open('log.txt','w')
    currentDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logFile.write("Starting at: " + currentDateTime + '\n')
    logFile.write('################\n')
    logFile.write('\n')

# write a line to the log file
def logWrite(output):
    logFile = open('log.txt','a')
    currentDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    logFile.write(currentDateTime + ": " + output + '\n')

def increasing(i, j):
    returnCode = False
    if int(j) > int(i): 
        returnCode = True
    return returnCode

def decreasing(i, j):
    returnCode = False
    if int(j) < int(i): 
        returnCode = True
    return returnCode