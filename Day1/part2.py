import importlib.util
import sys
spec = importlib.util.spec_from_file_location("advent.util", "/home/emunsell/git/advent_of_code_2024/advent/util.py")
util = importlib.util.module_from_spec(spec)
sys.modules["advent.util"] = util
spec.loader.exec_module(util)

util.logReset()
input = util.readInput()

column1 = []
column2 = []

for i in input:
    stringSplit = i.split()
    column1.append(stringSplit[0])
    column2.append(stringSplit[1])

column1.sort()
column2.sort()
answerArray = []


for i in column1:
    instances = column2.count(i)
    answerArray.append(instances)

finalCount = int(0)
columnLength = int(len(column1))
i = 0

while i < columnLength:
    finalCount = finalCount + (int(column1[i]) * int(answerArray[i]))
    i = i + 1

print(finalCount)
