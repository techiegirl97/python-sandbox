def square_digits(num):
    #convert the number to an iterable string
    n = str(num)
    #convert n into an array
    arr = list(n)
    #convert the array into int
    arr = [int(i) for i in arr]
    #square each number in the int array
    squares = [x**2 for x in arr]
    #combine the array
    s = ''.join(map(str, squares))
    #convert the array into an int
    newNum = int(s)
    return newNum
    pass