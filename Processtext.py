import re
"""
Processes the text converted form of each pdf, converting each of them into a list, so that the classification task becomes easy
"""

portionPath = "Papers/Text/aieee-syllabus-2012.pdf.txt"

def getPortionList(portionStrList):
	for portionStr in portionStrList:
		pass


def findPortion():
	string = open(portionPath,"r").read()
	list1 = re.split("MATHEMATICS",string)
	list2 = re.split("PHYSICS",list1[1])
	math = list2[0]
	list3 = re.split("CHEMISTRY",list2[1])
	physics = list2[0]
	chemistry = list2[1].split("SYLLABUS")[0]
	portions=[]
	portions.append(math)
	portions.append(physics)
	portions.append(chemistry)
	print math+"\n"+physics+"\n"+chemistry

if __name__=="__main__":
	findPortion()



