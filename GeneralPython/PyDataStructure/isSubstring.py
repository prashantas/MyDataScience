def issubstring(s1,s2):
    #check if s1 is substring of s2
    M = len(s1)
    N = len(s2)

    for i in range(N-M+1):
        for j in range(M):
            if s2[i+j] != s1[j]:
                break
            if j+1 == M:
                return i 
    return -1

if __name__ == "__main__":
    s1 = "ford"
    s2 = "avfordc"
    print(issubstring(s1,s2))
