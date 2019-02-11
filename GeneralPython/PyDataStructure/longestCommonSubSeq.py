#http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/
import numpy

def lcsLen(s1, s2):
    r = len(s1)
    c = len(s2)
    l = numpy.zeros((r+1,c+1))
    #l = [[None]*(c+1) for i in range(r+1)] 
    #print("len(s1):{} and len(s2):{}".format(r,c))
    #print("l is:{}".format(l))

    for i in range(r+1):
        for j in range(c+1):
            if i==0 or j==0:
                l[i][j] =0
            elif s1[i-1] == s2[j-1]:
                l[i][j]= l[i-1][j-1] +1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])

    return int(l[r][c]), l  # return lenght and array l

#http://www.geeksforgeeks.org/printing-longest-common-subsequence/
def lcsString(s1, s2):
    index, larray = lcsLen(s1, s2)  # index is lenght of lcs
    print("len:{} and \n l ::\n {}".format(index, larray))

    lcs = numpy.empty((int(index), ), dtype='str')

    #alt way
    # lcs = np.chararray((4,))
    # lcs[:] = ''

    i = r = larray.shape[0] - 1 
    j = c = larray.shape[1] - 1
    print("shape of larray:{}  \n And shape of lcs:{}".format(larray.shape, lcs.shape))

    while i > 0 and j > 0 :
        if s1[i-1] == s2[j-1]:
            lcs[index-1] = s1[i-1]
            #print("temp:::::::LCS string is {}".format("".join(lcs)))
            i -= 1
            j -= 1
            index -= 1
        elif larray[i-1][j] > larray[i][j-1]:
            i -= 1
        else:
            j -= 1
    print("LCS string is {}".format("".join(lcs)))



if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    #print("lcs:",lcsLen(X,Y))
    lcsString(X,Y)
