a=[1,2,3,4,5]
def permute(array):
    if len(array)==2:
         return [array,array[::-1]]
    returnArray = []
    for x in range(len(array)):
        tValue = array[x]
        tArray = array[:]
        del tArray[x]
        pSubArray = permute(tArray)
        for y in pSubArray:
            y.insert(0,tValue)
        returnArray+=pSubArray
    return returnArray
print permute(a)
print len(permute(a))
