def positive_sum(arr):
    positiveSum = 0
    i = 0
    for i in arr:
        if i > 0:
            positiveSum += i
        else:
            continue
    print(positiveSum)
    return(positiveSum)
    return 0