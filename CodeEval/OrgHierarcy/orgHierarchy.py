import sys

class node:
    def __init__(self,data):
        self.data = data
        self.children = []
    def __repr__(self):
        return "%s" %(self.data)
    def add(self, child):
        self.children.append(child)

def find_node(r, n1, n2):
    if (r.data == n1.data):
        r.children.append(n2)
        return True
    for ch in r.children:
        res = find_node(ch, n1, n2)
        if (res):
            return True
    return False

def print_tree(r):
    print r.data,
    if r.children != []:
        print "[",
    numch = len(r.children)
    for i in xrange(numch):
        if (i > 0 and i < numch):
            print ",",
        print_tree(r.children[i])
        if (i == numch-1):
            print "]",
    

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    test = test.split("|")
    test = [pair.strip() for pair in test]
    roots = []
    root = None
    test = sorted(test)
    #print test
    for connection in test:
        connection = connection.strip()
        node2 = node(connection[1])
        node1 = node(connection[0])
        root = None if roots == [] else roots[0]
        if (root is None):
            node1.children.append(node2)
            root = node1
            roots.append(root)
        elif (node1.data == root.data):
            root.children.append(node2)
        else:
            for rt1 in roots:
                added = find_node(rt1, node1, node2)
                if (not added):
                    roots.append(node1)
                    node1.children.append(node2)
                    break
    for rt in roots:
        print_tree(rt)
            
        print 
test_cases.close()

