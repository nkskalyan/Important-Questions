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
		elif type(content)==None:
			pass
		elif type(content)==dict:
			print content
		else:
			file.write(content)
		file.close()

#In the PDf read, there is no space between unit name and first topic.
#Replace the same using this function
def SeparateWhiteSpace(str):
	toReplace=re.findall("[A-Z][a-z]+[A-Z]",str)
	#print toReplace
	for text in toReplace:
		#Replacement for the word without space
		replacedText = text[:len(text)-1]+"::::"+text[len(text)-1]
		#print replacedText
		str =  re.sub(text,replacedText,str)
		
	#print str
	return str

#Returns portions for each subject as a list, split based on units
def getPortionDictList(portionDict):
	splitPortDict={}
	for subject,portion in portionDict.iteritems():
		port = re.split("UNIT [0-9]+:",portion)
		if port:
			splitPortDict[subject+"_split"]=port
		#Just for testing, To be removed
	WriteDictToFile(splitPortDict)
	return splitPortDict

#Does basic removal of whitespaces and separation of portion for each subject
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
	portions["math"]=SeparateWhiteSpace(math)
	portions["physics"]=SeparateWhiteSpace(physics)
	portions["chemistry"]=SeparateWhiteSpace(chemistry)

	#Just for testing, To be removed
	WriteDictToFile(portions)
	
	return portions
	

if __name__=="__main__":
	finalPortions={}
	portionDict = findPortion()
	portionDict = getPortionDictList(portionDict)
	for subject,portionList in portionDict.iteritems():
		unit={}
		for unitPortions in portionList:
			if not unitPortions:
				continue
			tempList = unitPortions.split(":::")
			unitName = tempList[0]
			if len(tempList)<2:#TEsting. Won't work for physics
				continue 
			splitTopic = tempList[1].split(',')	#The topics in the unit are split
			for topic in splitTopic:
				unit[topic] = unitName
		finalPortions[subject+"_test"] = unit
	WriteDictToFile(finalPortions)


