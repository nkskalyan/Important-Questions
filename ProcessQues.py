import re
import os
questionsPath = "Papers/Text/"


if __name__=="__main__":
	quesList = {}


	q_list =[]
	for (dirpath, dirnames, filenames) in os.walk(questionsPath):
	    q_list.extend(filenames)
	    
	    q_list= [questionsPath+fname for fname in q_list]
    
	    for files in q_list:
		    f = open(files,"r")
		    st = f.read()
		    st = re.sub("[\n\t]"," ",st)
		    stList = re.split("[0-9]+\.[^0-9]",st)
		    op = open(files+"_s","w")
		    op.write("".join(stList))
		    f.close()
		    op.close()
				   
