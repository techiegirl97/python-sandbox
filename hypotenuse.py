def hypotenuse(a,b):

    import math
    h = round(math.sqrt(a**2 + b**2),4)
    #print(h)
    return h
	
test.expect(hypotenuse(7,4) == 8.0623)
test.expect(hypotenuse(3,4) == 5)
test.expect(hypotenuse(56,87) == 103.465)
test.expect(hypotenuse(15,19) == 24.2074)
test.expect(hypotenuse(10,10) == 14.1421)