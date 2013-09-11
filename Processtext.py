import re
"""
Processes the text converted form of each pdf, converting each of them into a list, so that the classification task becomes easy
"""

portionPath = "Papers/Text/aieee-syllabus-2012.pdf.txt"

def WriteDictToFile(fileDict):
	for fileName,content in fileDict.iteritems():
		file = open(fileName, "w")
		if type(content)==list:
			file.write("\n".join(content))
		else:
			file.write(content)




def getPortionList(portionStrList):
	for portionStr in portionStrList:
		pass


def findPortion():
	string = open(portionPath,"r").read()
	unformattedList = re.split("MATHEMATICS",string)
	#Remove unwanted stuff before Math
	unformattedList = re.split("PHYSICS",unformattedList[1])
	#First part of remaining is math
	math = unformattedList[0]
	unformattedList = re.split("CHEMISTRY",unformattedList[1])
	physics = unformattedList[0]
	chemistry = unformattedList[1].split("SYLLABUS")[0]
	portions={}
	portions["math"]=math
	portions["physics"]=physics
	portions["chemistry"]=chemistry
	WriteDictToFile(portions)
	#print math+"\n"+physics+"\n"+chemistry

if __name__=="__main__":
	findPortion()



