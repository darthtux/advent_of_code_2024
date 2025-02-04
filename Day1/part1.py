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

columnLength = len(column1)
line = 0

while line < columnLength:
    answerArray.append(abs(int(column1[line]) - int(column2[line])))
    line = line + 1

answerSum = 0

for i in answerArray:
    answerSum = answerSum + i


print(answerSum)