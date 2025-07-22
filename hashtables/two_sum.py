def two_sum(array,target):
    val1 = 0
    val2 = 0
    found_rem = 0
    for i in range(len(array)):
        rem = target-array[i]
        if rem in array:
            found_rem = rem
            val1 = i
    for i in range(len(array)):
        if array[i] == found_rem:
            val2 = i
    if val1 == 0 and val2 == 0:
        return ()
    else:
        return (val1, val2)

            



print(two_sum([3,2,4,7,3,1,9],8))