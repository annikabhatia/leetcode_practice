def addStrings(num1: str, num2: str) -> str:
        numDict = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        answer1 = 0
        answer2 = 0
        #looping over a string, so 'i' will start w/ first char
        for i in num1:
            answer1 = answer1*10 + numDict[i]
        for j in num2:
            answer2 = answer2*10 + numDict[j]
        return str(answer1 + answer2)
