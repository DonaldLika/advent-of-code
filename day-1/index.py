def findFirstCombination(totalNumbers, inputValues, summary=2020):
     if totalNumbers == 1:
        return [summary] if summary in inputValues  else None

     for n in inputValues:
        result= findFirstCombination(totalNumbers-1,inputValues,summary-n)
        if result:
            return [n,*result]