def sorted_squared(array):
    new_array =[0] * len(array)
    i = 0
    j = len(array) - 1

    for k in reversed(range(len(array))):
        sq_i = array[i] ** 2
        sq_j = array[j] ** 2
        if sq_i > sq_j:
            new_array[k] = sq_i
            i += 1
        else:
            new_array[k] = sq_j
            j -= 1
    return new_array

a = [-3,-3,7,13, 18]
b = [1, 4, 5, 7]
c = [-11, 1, 4, 5, 9]

print(sorted_squared(a))
print(sorted_squared(b))
print(sorted_squared(c))