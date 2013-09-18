import os
import re
from PyPDF2 import PdfFileReader


IN_PATH_P = "Papers/Pdf/Portions"
IN_PATH_Q = "Papers/Pdf/Questions/First_Page"
OUT_PATH = "Papers/Text"
count=0
def writeFile(text,fileName):
    count=0
    filename= OUT_PATH+"/"+fileName
    #print filename
    count=count+1
    a=open(filename,"w")
    if text:    
        a.write(text.encode("UTF-8"))  
    else:
	print fileName+"  Failed"

	a.close()



def ReadPDF(path):
	count=0
	q_list =[]
	for (dirpath, dirnames, filenames) in os.walk(path):
	    q_list.extend(filenames)

	q_list= [path+"/"+fname for fname in q_list]

	print q_list
	for files in q_list:
	    ip = open(files,"rb")
	    print files
	    
	    
	    try:
		pd = PdfFileReader(ip)
	    except:
		print "read error"
	    a=""
	    for x in xrange(0,pd.getNumPages()):
		a = a + pd.getPage(x).extractText()+'\n'
	    #print a
	    #a = re.split(a,"[0-9]+")
	    #a = "\n".join(a)
	    writeFile(a,files.split('/')[-1]+".txt")
	    """
	    except:
		print "print error"
		"""

if __name__ == '__main__':
	ReadPDF(IN_PATH_P)
	ReadPDF(IN_PATH_Q)
