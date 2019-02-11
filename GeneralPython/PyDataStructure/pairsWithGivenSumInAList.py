from collections import Counter

def getPairsCount(arr, sum):
    mapc = dict(Counter(arr))

    twice_cnt = 0 
    for i in range(len(arr)):
        if mapc.get(sum-arr[i], None) is not None:
            twice_cnt += mapc.get(sum-arr[i])
        
        # if (arr[i], arr[i]) pair satisfies the 
        # condition, then we need to ensure that 
        # the count is  decreased by one such  
        # that the (arr[i], arr[i]) pair is not 
        # considered 
        if sum-arr[i] == arr[i]:
            twice_cnt -=1
        
    return int(twice_cnt/2)

def getPairs(arr, sum):
     #https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/
     s = set()
     pairList = list()
     for i in range(len(arr)):
        temp = sum - arr[i]
        if temp>=0 and temp in s:
            pairList.append((arr[i],temp))
        s.add(arr[i])

     return pairList






if __name__ == "__main__":
    arr = [1, 5, 7, -1,2, 5,4 ] 
    sum =6 

    print("Count of pairs is", getPairsCount(arr, sum)) 
    print("#########################################")
    print("Pairs are::{}".format(getPairs(arr,sum)))
