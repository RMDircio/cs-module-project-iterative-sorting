
def linear_search(arr, target):
    # for every element in the list (length of arr)
    for i in range(len(arr)):
        # if the element is the target
        if arr[i] == target:
            # return correct/true
            return True

    # otherwise - if target does is not in list(arr)
    # return no/false
    return False


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # set a start and end
    begin_index = 0
    end_index = len(arr) -1  # python has negative indices

 # while the start is less than or equal to the end
    while begin_index <= end_index:
        # set the middle value
        # middle value = start + remaining list items, then divide w/o a remainder floor division ( // 2 )
        midpoint = begin_index + (end_index - begin_index) // 2

        # compare the midpoint value (not the index) to target
        midpoint_value = arr[midpoint]

        # if middle value is equal to target
        if midpoint_value == target:
            # return the middle index
            return midpoint
        
        # if target is less ( to the left ) than middle value
        elif target < midpoint_value:
            # set the end index to the middle index - 1
            end_index = midpoint - 1

        # otherwise
        else:
            # set the start to middle index +1 - check only the items to the right
            begin_index = midpoint + 1

    # when while loop breaks if target is NOT in list
    return None




