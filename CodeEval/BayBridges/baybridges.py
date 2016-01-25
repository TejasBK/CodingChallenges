import re
class Bridge:
    def __init__(self, latA, lonA, latB, lonB, index):
        self.latA = latA
        self.lonA = lonA
        self.latB = latB
        self.lonB = lonB
        self.index = index

    def __repr__(self):
        return str(self.index)+ ": ("+str(self.latA)+ " "+str(self.lonA)+") ("+str(self.latB)+ " "+str(self.lonB)+")"

filename = "/Users/teja2/Documents/teja_coding/CodingChallenges/BayBridges/test_baybridges.txt"

with open(filename) as f:
    bridges = []
    for test in f:
        test = test.rstrip().split(":")
        index = test[0]
        print index
        test = test[1]
        test = re.sub(r"[\(\)\[\]]","",test)
        test = test.split(",")
        newb = Bridge(float(test[0]),float(test[1]),float(test[2]),float(test[3]),index)
        print newb
        bridges.append(newb)
    sorted_bridges = sorted(bridges, key=lambda b:b.latA)
    print "\n"
    print "\n".join(str(item) for item in sorted_bridges)
