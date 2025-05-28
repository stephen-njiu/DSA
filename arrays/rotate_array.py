def rotate_array(array, k):
    if len(array) == 0: return []
    k = k%len(array)
    temp = array[-k:]
    for i in reversed(range(0,len(array)-k)):
        array[i+k] = array[i]
    for i in range(len(temp)):
        array[i] = temp[i]
    return array

a = [3, 4, 5, 6, 7, 8]
print(rotate_array(a, 2))