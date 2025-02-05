import importlib.util
import sys
spec = importlib.util.spec_from_file_location("advent.util", "/home/emunsell/git/advent_of_code_2024/advent/util.py")
util = importlib.util.module_from_spec(spec)
sys.modules["advent.util"] = util
spec.loader.exec_module(util)



def calculateDiff(i, j):
    diff = abs(int(i)-int(j)) 
    util.logWrite(str(diff))
    if diff > 0 and diff < 4:
        return True
    else:
        util.logWrite('False')
        return False

util.logReset()
input = util.readInput()

safeReports = 0

for i in input:
    arrayLine = i.split()
    util.logWrite(str(i))

    util.logWrite('increase or decrease')
    length = len(arrayLine) - 1
    j = 0
    passing = True
    isIncreasing = True
    isDecreasing = True
    while j < length:
        if util.increasing(arrayLine[j], arrayLine[j+1])  == False:
            isIncreasing = False
        if util.decreasing(arrayLine[j], arrayLine[j+1])  == False:
            isDecreasing = False
        if calculateDiff(arrayLine[j], arrayLine[j+1])  == False:
            passing = False
            j = length
        util.logWrite(str(passing) + " " + str(isIncreasing) + " " + str(isDecreasing))

        j = j + 1

    util.logWrite(str(passing) + " " + str(isIncreasing) + " " + str(isDecreasing))
    if passing and ( isIncreasing or isDecreasing):
        util.logWrite('passing')
        safeReports = safeReports + 1

    util.logWrite('---------')
    

print(safeReports)