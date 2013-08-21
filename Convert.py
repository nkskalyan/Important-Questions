import os
import re
from PyPDF2 import PdfFileReader


IN_PATH_P = "Papers/Pdf/Portions"
IN_PATH_Q = "Papers/Pdf/Questions"
OUT_PATH = "Papers/Text"
count=0
def writeFile(text):
    count=0
    filename= OUT_PATH+"/"+"ANS"+str(count)
    print filename
    count=count+1
    a=open(filename,"w")
    try:
        a.write(text)
    except:
        pass
    a.close()



#if __name__ == '__main__':
count=0
q_list =[]
for (dirpath, dirnames, filenames) in os.walk(IN_PATH_Q):
    q_list.extend(filenames)

q_list= [IN_PATH_Q+"/"+fname for fname in q_list]

#print q_list
for files in q_list:
    ip = open(files,"rb")
    print files
    
    
    try:
        pd = PdfFileReader(ip)
    except:
        print "read error"
    
    a= pd.getPage(0).extractText()
    #a = re.split(a,"[0-9]+")
    #a = "\n".join(a)
    writeFile(a)
    """
    except:
        print "print error"
        """