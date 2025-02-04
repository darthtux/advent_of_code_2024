import importlib.util
import sys
spec = importlib.util.spec_from_file_location("advent.util", "/home/emunsell/git/advent_of_code_2024/advent/util.py")
util = importlib.util.module_from_spec(spec)
sys.modules["advent.util"] = util
spec.loader.exec_module(util)

util.logReset()
input = util.readInput()

