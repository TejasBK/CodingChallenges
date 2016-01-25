import re
import collections
import operator

def redblueredblue(pattern, inp):
    if (len(inp) < len(pattern)):
        return 0
    # Map unique chars and their occurrences to a dictionary
    memFreq = collections.Counter(pattern)
    #Input is the same char repeated. e.g '1111'
    if len(set(inp)) == 1:
        pat1 = r"((.+)?){" + str(len(pattern)-1)+"}"
        match = re.search(pat1,inp)
        if match:
            return 1
    #Sort dictionary entries by value
    memFreqSorted = sorted(memFreq.items(), key=operator.itemgetter(1), reverse=True)
    count = len(memFreqSorted)
    dupInp = inp
    for item in memFreqSorted:
        key = item[0]
        val = item[1]
        if (inp == ""):
            return 0
        #If occurrence = 1 then don't continue searching
        if val == 1:
            break
        count-=1
        if val > 1:
            #If keys in pattern occur next to each other abceee
            pat2 = r"" + key + "+"
            ls = re.search(pat2, pattern)
            if (len(ls.group()) > 1):
                pat3 = r"(.+)"+("\\1"*(len(ls.group())-1))
                match2 = re.search(pat3, inp)
                if match2:
                    inp = re.sub(match2.group(1),r"",inp)
            else:
                repeat = ".*\\1"*(val-1)
                pat4 = r"(.+)" + repeat
                match3 = re.search(pat4, inp)
                if match3:
                    inp = re.sub(match3.group(1),r"", inp)
            if (inp == dupInp):#If no matching pattern was found in inp
                return 0
    if ((count == 0 and inp == "") or (count >0 and inp != "")):
        return 1
    return 0 

if __name__=="__main__":
    fileName = "/Users/teja2/Downloads/test_cases_omjs2ksa"
    for i in xrange(1,13):
        inpFileName = fileName + "/input0"+"{0:02d}".format(i)+ ".txt"
        inpFile = open(inpFileName,"r")
        pattern = inpFile.next().rstrip('\n')
        inp = inpFile.next().rstrip('\n')
        print "====================="
        print pattern, inp
        result = redblueredblue(pattern, inp)
        outFileName = fileName + "/output0"+"{0:02d}".format(i)+ ".txt"
        outFile = open(outFileName,"r")
        out = int(outFile.next().rstrip('\n'))
        print "Output desired = ",out
        print "Output obtained = ", result

    inpFile.close()
    outFile.close()
