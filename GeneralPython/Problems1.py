### https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt

def Q1():
    '''
    Question:
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
    The numbers obtained should be printed in a comma-separated sequence on a single line.
    '''
    l = []
    for i in range(2000,3200):
        if (i%7 == 0) and (i%5 != 0):
            l.append(str(i))

    print(",".join(l))

###########################################################################
def Q2():
    '''
            Question:
        Write a program which can compute the factorial of a given numbers.
        The results should be printed in a comma-separated sequence on a single line.
        Suppose the following input is supplied to the program:
        8
        Then, the output should be:
        40320

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input.

        '''
    #x = int(raw_input())  # for python 2
    x = int(input())  # for python 3
    print(fact(x))

def fact(x):

    if x==0:
        return 1
    return x*fact(x-1)


###########################################################################################################################################
def Q3():
    '''
    Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    :return:
    '''
    n = int(input())
    d = dict()
    #d = {}
    for i in range(1,n+1):
        d[i] = i*i

    print(d)

##############################################################################################
def Q4():
    '''
    Question4:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

    '''
    values = input()
    l = values.split(",")
    t = tuple(l)
    print(l)
    print(t)

##############################################################
'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class InputOutString(object):
    def __init__(self):
        self.s=""
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())

def Q5():
    strObj = InputOutString()
    strObj.getString()
    strObj.printString()

#####################################################################
'''
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. 
'''
def Q6():
    import math
    C,H = 50,30
    values = input()
    result = []
    items = [x for x in values.split(",")]
    for d in items:
        result.append(str(int(round(math.sqrt(C*2*float(d)/H)))))
    print(",".join(result))
##################################################################################################
'''
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
'''
def Q7():
    input_str = input()
    dimensions = [x for x in input_str.split(",")]
    rowNum = int(dimensions[0])
    colNum = int(dimensions[1])
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
    print("Multilist is:\n", multilist)
    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col] = row * col
    print("\nFinal multilist:\n",multilist)

#############################################################################################
'''
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

'''
def Q8():
    items = [x for x in input().split(",")]
    items.sort()
    print(",".join(items))
##################################################################################
'''
Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

'''
def Q9():
    lines = []
    while True:
        s = input()
        if s:
            lines.append(s.upper())
        else:
            break
    for sentence in lines:
        print(sentence)

########################################################################
'''
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
'''
def Q10():
    s = input()
    words = [word for word in s.split(" ")]
    print(" ".join(sorted(list(set(words)))))
############################################################################################################
'''
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
 The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''
def Q11():
    values = []
    items = [x for x in input().split(",")]
    for p in items:
        intp = int(p,2)
        print("intp = ",intp)
        if not intp%5:
            values.append(p)
    print(",".join(values))

###################################################################################
'''
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
def Q12():
    values = []
    for i in range(1000,3001):
        s = str(i)
        if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
            values.append(s)
    print(",".join(values))
##################################################################################################
'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
def Q13():
    s = input()
    d = {"DIGITS":0, "LETTERS": 0}
    for c in s:
        if c.isdigit():
            d["DIGITS"] +=1
        elif c.isalpha():
            d["LETTERS"] +=1
        else:
            pass
    print("DIGITS:", d["DIGITS"])
    print("LETTERS:", d["LETTERS"])
###############################################################################
'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
def Q14():
    s = input()
    d = {"UPPER":0, "LOWER":0}
    for c in s:
        if c.isupper():
            d["UPPER"] +=1
        elif c.islower():
            d["LOWER"] +=1
        else:
            pass
    print("UPPER:",d["UPPER"])
    print("LOWER:", d["LOWER"])
####################################################################
'''
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

'''
def Q15():
    a = input()
    n1 = int("%s" % a)
    print("n1:",n1)
    n2 = int("%s%s" % (a,a))
    print("n2:", n2)
    n3 = int("%s%s%s" % (a,a,a))
    print("n3:", n3)
    n4 = int("%s%s%s%s" % (a, a, a, a))
    print("n4:", n4)
    print("Result:", n1+n2+n3+n4)
###############################################################################
'''
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''
def Q16():
    val = input()
    values = val.split(",")
    numbers1 = [x for x in values if int(x)%2 != 0]
    numbers2 = [str(int(x)*int(x)) for x in values if int(x)%2 != 0]
    print(",".join(numbers1))
    print(",".join(numbers2))
#############################################################################
'''
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input.
 The transaction log format is shown as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
def Q17():
    netAmount = 0
    while True:
        s = input()
        if not s:
            break
        values = s.split(" ")
        operation = values[0]
        amount = int(values[1])
        if operation=='D':
            netAmount +=amount
        elif operation=='W':
            netAmount -=amount
        else:
            pass
    print("NetAmount:", netAmount)
##########################################################
'''
Question 18
Level 3

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
 Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
def Q18():
    import re
    value = []
    items = [ x for x in input().split(",")]
    for p in items:
        if len(p)<6 and len(p)>12:
            continue
        else:
            pass
        if not re.search("[a-z]",p):
            continue
        elif not re.search("[0-9]",p):
            continue
        elif not re.search("[A-Z]",p):
            continue
        elif not re.search("[$#@]",p):
            continue
        elif re.search("\s",p):
            continue
        else:
            pass
        value.append(p)
    print(",".join(value))
######################################################################
'''
Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers.
 The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''
def Q19():
    from operator import itemgetter
    l = []
    while True:
        s = input()
        if not s:
            break
        l.append(tuple(s.split(",")))
    print(sorted(l,key=itemgetter(0,1,2)))
    print(sorted(l, key=itemgetter( 1)))
###########################################################################
'''
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
'''
def putNumbers(n=50):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j
    #for i in reverse(100):
    #   print i
def Q20():
    for i in putNumbers():
        print(i)

def Q20a():
    x = putNumbers(n=60)
    for i in x:
        print(i)

## https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
## https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

########################################################################################
'''
Question 21
Level 3

Question£º
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
 The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point.
 If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''
def Q21():
    import math
    pos = [0,0]  # like X,Y cordinate
    while True:
        s = input()
        if not s:
            break;
        movement = s.split(" ")
        direction = movement[0]
        steps = int(movement[1])
        if direction=="UP":
            pos[1] += steps
        elif direction=="DOWN":
            pos[1] -= steps
        elif direction == "LEFT":
            pos[0] -= steps
        elif direction == "RIGHT":
            pos[0] += steps
        else:
            pass
    print(int(round(math.sqrt(pos[0]**2 + pos[1]**2 ))))
###########################################################################################################
'''
Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''
def Q22():
    freq = dict()
    line = input()
    for word in line.split(" "):
        freq[word] = freq.get(word,0) + 1  # 2nd arg in get i.e 0 is for if key is not found, return 0

    words = freq.keys()
    words = sorted(words)
    for w in words:
        print("{}:{}".format(w, freq[w]))

# using default dict
def Q22a():
    from collections import defaultdict
    freq = defaultdict(int) #
    line = input()
    for word in line.split(" "):
        freq[word] +=1
    words = sorted(freq.keys())
    for w in words:
        print("{}:{}".format(w, freq[w]))
###############################################################################################
'''
Question 24
Level 1

Question:
    Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. 
    But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function
    
Hints:
    The built-in document method is __doc__

'''


def square(num):
    '''Return the square value of the input number.

    The input number must be integer.
    '''
    return num ** 2
def Q24():
    #print(int.__doc__)
    #print(abs.__doc__)
    #print(input.__doc__)
    print(square.__doc__)

################################################################################################
'''
2.10

Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
'''
def Q2_10():
    d = dict()
    for i in range(1,21):
        d[i] = i**2

    for k,v in d.items():
        print("{}:{}".format(k,v))
#################################################################################
'''
3.4

Question:
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
'''
def Q3_4():
    li = range(1,11)
    evenNo = filter(lambda x: x%2==0,li)
    print(list(evenNo))
####################################################################################
'''
3.4.1

Question:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
'''
def Q3_4_1():
    li = range(1,11)
    sq = map(lambda x : x*x, li)
    print(list(sq))
###########################################################################
'''
3.5

Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
'''
def Q3_5():
    li = range(1,11)
    evsq = map(lambda x: x*x, filter(lambda x: x%2==0, li))
    print(list(evsq))
#################################################################################
'''
Question:

By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.
'''
def Q_enu():
    li = [12, 24, 35, 70, 88, 120, 155]
    li = [ x for (i,x) in enumerate(li) if i not in [0,4,5]]
    print(li)

############################################################
############################################################
if __name__ == '__main__':
    Q_enu()
