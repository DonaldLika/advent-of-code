import re
import os

######################### Solution ###############################

class Row():
    minLimit: int
    maxLimit: int
    letter: str
    password: str

    def __init__(self,rowString:str):
        parsedLine=rowString.split(" ")  
        self.minLimit, self.maxLimit = map(int,parsedLine[0].split("-"))
        self.letter = parsedLine[1][0]
        self.password = parsedLine[2]

    def isValid(self)->bool:
          return self.minLimit <= self.password.count(self.letter) <=self.maxLimit
   
    def isValidTobogganPassword(self)->bool:
          return self.password[self.minLimit-1] == self.letter and self.password[self.maxLimit-1] != self.letter
   

def readPasswords(passwords):
     return [Row(p) for p in passwords]

######################### Test ###############################

passwords=readPasswords('''\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
'''.splitlines())

assert sum(pwr.isValid() for pwr in passwords) == 2

assert sum(pwr.isValidTobogganPassword() for pwr in passwords) == 1

########################## Print results for part 1,2 #################################
with open("input") as f:
         filePasswords= readPasswords(f.readlines())

totalValid = sum(pwr.isValid() for pwr in filePasswords)
totalTobogganValid = sum(pwr.isValidTobogganPassword() for pwr in filePasswords)

print("Total valid passwords:", totalValid)
print("Total Toboggan valid passwords:", totalTobogganValid)