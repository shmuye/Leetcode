def addBinary(a,b):
    aInt = int(a,2)
    bInt = int(b,2)
    result = aInt + bInt
    bitStringResult = bin(result)
    return bitStringResult[2:]

      
    
