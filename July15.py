# Leetcode Daily Challenge
# Custom Sort String
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        strDict = {}
        finalString = ""
        for i in str:
            if(i in strDict.keys()):
                strDict[i] += 1
            else:
                strDict[i] = 1
        for j in order:
            if(j in strDict.keys()):
                finalString = finalString + j * strDict[j]
                del strDict[j]
        leftOvers = set(strDict.keys())
        for k in leftOvers:
            finalString = finalString + k * strDict[k]
        return finalString
