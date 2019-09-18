def nested_sum(array):
    total = 0
    for array_first in array:
        for val in array_first:
            total += val
    return total
