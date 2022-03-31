# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

# Use bubble sort:

def move_zeros(array):
    last_item = len(array) - 1
    for z in range(0, last_item):
        for x in range(0, last_item):
            if array[x+1] == 0:
                continue
            elif array[x] == 0:
                array[x], array[x+1] = array[x+1], array[x]
    return array
