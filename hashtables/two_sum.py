def two_sum_slow(array,target):
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
        return []
    else:
        return [val1, val2]
    
def two_sum_medium(array, target):
    # find min and max to define the offset for negative values
    min_val = min(array)
    max_val = max(array)
    offset = -min_val  # shift negatives into positive indices
    size = max_val - min_val + 1

    # build auxiliary array
    positions = [None] * size

    for i in range(len(array)):
        positions[array[i] + offset] = i  # map value → index

    val1 = val2 = None

    for i in range(len(array)):
        rem = target - array[i]
        idx = rem + offset
        if 0 <= idx < size and positions[idx] is not None and positions[idx] != i:
            val1 = i
            val2 = positions[idx]
            break

    if val1 is None or val2 is None:
        return []
    else:
        return [val1, val2]


def two_sum_hashtable(array, target_value):
    # create an empty dict
    hash_dict = {}
    # inverse the array value, index and store in the dict
    for i in range(len(array)):# iterating the whole array, keeping i
        find_val = target_value - array[i]
        if find_val in hash_dict:
            return [hash_dict[find_val],i]
        else:
            hash_dict[array[i]] = i # inverse storage for keys retrieval as value in O(1)
    return []# for any other case, eg. len of 1 or empty array given, then return empy array
    



            


array = [1,4,9,6,2,-3,5,3]
# array = [1,4,9,6,2,-3,5,1]
target_value = 2
print(two_sum_slow(array, target_value))
print(two_sum_medium(array, target_value))
print(two_sum_hashtable(array, target_value))
# All ok!