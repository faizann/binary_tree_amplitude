__author__ = 'faizan'

class bintree:
    x = 0
    l = None
    r = None

    def __init__(self,x,l,r):
        self.x = x
        self.l = l
        self.r = r



tree = bintree(5,
               bintree(8,
                       bintree(12,
                               bintree(1,
                                       None,
                                       None),
                               None),
                       bintree(6,
                               None,
                               None),
                       ),
               bintree(9,
                       bintree(7,
                               bintree(2,
                                       None,
                                       None),
                               None),
                       bintree(4,
                               None,
                               bintree(3,
                                       None,
                                       None)

                       )
               )
            )


def maxdiff(maxN,minN, node):

    if node.l == None and node.r == None:
        maxN = maxN if maxN >= node.x else node.x
        minN = minN if minN <= node.x else node.x
        return (maxN,minN)
    #diffMax = abs(maxN-minN)
    maxN1 = maxN if maxN >= node.x and maxN > -1 else node.x # node.x is max if maxN is less than it
    minN1 = minN if minN <= node.x and minN > -1 else node.x # node.x is min if minN is > than it
    #print "max,min %d,%d" % (maxN1,minN1)
    maxN2 = maxN1
    minN2 = minN1
    # split paths here
    if node.l != None:
        (maxN1,minN1) = maxdiff(maxN1,minN1,node.l)

    if node.r != None:
        (maxN2,minN2) = maxdiff(maxN2,minN2,node.r)

    if abs(maxN1-minN1) > abs(maxN2 - minN2):
        return (maxN1,minN1)

    return (maxN2,minN2)


if __name__=="__main__":
    
    max,min = maxdiff(-1,-1,tree)
    print "max,min (%d,%d)" % (max,min)
    print "Solution is %d" % abs(max-min)
