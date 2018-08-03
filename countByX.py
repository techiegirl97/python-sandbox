def count_by(x, n):
    #Return a sequence of numbers counting by `x` `n` times.

    list = []    
    len = x * n
    orig = x
    
    while count < len:
        list.append(x)
        x+=orig

    return list