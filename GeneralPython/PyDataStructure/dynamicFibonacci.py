def fibo(n):
    fib = [None]*n
    fib[0] = 0
    fib[1] = 1

    for i in range(2,n):
        #print(i)
        fib[i] = fib[i-1] + fib[i-2]

    print(fib)

fibo(8)
